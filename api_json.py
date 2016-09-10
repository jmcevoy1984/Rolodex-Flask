from flask import abort
from app import app, db
from models import Staff_Member, Users
from flask_restful import Api, Resource, reqparse, fields, marshal_with, marshal

#Apply the Api fuction to the imported 'app' and then return the modified app to 'api'
api = Api(app)

#API JSON ROUTES

'''--------User Resources-------'''

#Creates a dictionary of 'fields' to be used by the marshal function (or marshal_with decorator) for output.
#When using this function any field/attribute not listed here will be ignored when outputting the model.

user_fields = {

	'id' : fields.Raw,
	'email' : fields.String,
	'password' : fields.String,
	'staff_id' : fields.Raw,
	'profile_image_uri' : fields.String,
	'profile_thumb_uri' : fields.String

}

staff_fields = {
	
	'id' : fields.Raw,
	'first_name' : fields.String,
	'last_name' : fields.String,
	'team': fields.String,
	'team_lead' : fields.String,
	'location' : fields.String,
	'active_regions' : fields.String,
	'role' : fields.String,
	'manager' : fields.String,
	'phone_number' : fields.String,
	'duties' : fields.String,
	'extension' : fields.String,
	'office_hours' : fields.String

}

#Defining API resources
#----------------------

#Create a 'UserList' class that subclasses "Resource".
#Uses the 'reqparse' object to parse the request and ensure it is valid.

class UserListAPI(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('email', type = str, help = 'No User email provided',
location = 'json')
		self.reqparse.add_argument('password', type = str, help = 'No User password provided',
			location = 'json')
		super(UserListAPI, self).__init__()

	def post(self):
		args = self.reqparse.parse_args()
		if Users.query.filter_by(email=args['email']).first():
			abort(409)
		else:
			user = Users(args['email'], args['password'])
			db.session.add(user)
			db.session.commit()
			user.staff_id = user.id
			member = Staff_Member()
			member.id = user.id
			db.session.add(member)
			db.session.commit()
			return { 'result' : True }, 201

	def get(self):
		if not Users.query.all():
			abort(404)
		else:
			all_users = Users.query.all()
			output_users = []
			for user in all_users:
				output_users.append(marshal(user, user_fields))
		return { 'Users' : output_users }, 200


class UserAPI(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('email', type = str, location = 'json')
		self.reqparse.add_argument('password', type = str, location = 'json')
		super(UserAPI, self).__init__()

	@marshal_with(user_fields)
	def get(self, id):
		print(id)
		id = int(id)
		if not Users.query.get(id):
			abort(404)
		else:
			user = Users.query.get(id)
		return user, 200

	def put(self, id):
		if not Users.query.get(id):
			abort(404)
		else:
			user = Users.query.get(id)
			args = self.reqparse.parse_args()
			for key, value in args.items():
				if hasattr(user, key) and key != 'staff_id':
					setattr(user, key, value)
			db.session.commit()
		return { 'result': True }, 200

	def delete(self, id):
		if not Users.query.get(id):
			abort(404)
		else:
			db.session.delete(id)
			db.session.commit()
		return { 'result' : True }, 200

#-------Staff----------

class StaffListAPI(Resource):
		
	def get(self):
		if not Staff_Member.query.all():
			abort(404)
		else:
			all_members = Staff_Member.query.all()
			output_members = []
			for member in all_members:
				output_members.append(marshal(member, staff_fields))
		return { 'Members' : output_members }, 200


class MemberAPI(Resource):
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('first_name', type = str, default='', location = 'json')
		self.reqparse.add_argument('last_name', type = str, default='', location = 'json')
		self.reqparse.add_argument('team', type = str, default='', location = 'json')
		self.reqparse.add_argument('manager', type = str, default='', location = 'json')
		self.reqparse.add_argument('team_lead', type = str, default='', location = 'json')
		self.reqparse.add_argument('role', type = str, default='', location = 'json')
		self.reqparse.add_argument('extension', type = str, default='', location = 'json')
		self.reqparse.add_argument('phone_number', type = str, default='', location = 'json')
		self.reqparse.add_argument('location', type = str, default='', location = 'json')
		self.reqparse.add_argument('active_regions', type = str, default='', location = 'json')
		self.reqparse.add_argument('office_hours', type = str, default='', location = 'json')
		self.reqparse.add_argument('duties', type = str, default='', location = 'json')
		super(MemberAPI, self).__init__()

	@marshal_with(staff_fields)
	def get(self, id):
		type(id)
		id = int(id)
		if not Staff_Member.query.get(id):
			abort(404)
		else:
			member = Staff_Member.query.get(id)
		return member, 200

	def put(self, id):
		if not Staff_Member.query.get(id):
			abort(404)
		else:
			member = Staff_Member.query.get(id)
			args = self.reqparse.parse_args()
			for key, value in args.items():
				if hasattr(member, key) and value:
					setattr(member, key, value.title())
			db.session.commit()
		return { 'result': True }, 200

	def delete(self, id):
		if not Staff_Member.query.get(id):
			abort(404)
		else:
			db.session.delete(id)
			db.session.commit()
		return { 'result' : True }, 200

#Adding the objects, routes and endpoints to the API
api.add_resource(UserListAPI, '/api/users', endpoint='users')
api.add_resource(UserAPI, '/api/users/<int:id>', endpoint='user')
api.add_resource(StaffListAPI, '/api/staff', endpoint='staff')
api.add_resource(MemberAPI, '/api/staff/<int:id>', endpoint='member')