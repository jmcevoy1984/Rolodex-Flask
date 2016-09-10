from database import db
from flask.ext.login import UserMixin
from config import basedir

class Users(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(15), nullable=False)
	staff_id = db.Column(db.Integer, db.ForeignKey('staff__member.id'))
	profile_image_uri = db.Column(db.String(200))
	profile_thumb_uri = db.Column(db.String(200))
	
	#define relationship
	staff = db.relationship('Staff_Member', backref=db.backref("user", uselist=False), cascade="all, delete-orphan", single_parent=True, foreign_keys=[staff_id])

	def __init__(self, email='', password='', staff_id=None, profile_image_uri='/static/img/default.png', profile_thumb_uri='/static/img/default_thumb.png'):
		self.email = email
		self.password = password
		self.staff_id = staff_id
		self.profile_image_uri = profile_image_uri
		self.profile_thumb_uri = profile_thumb_uri

	def __repr__(self):
		return "id: {}, email: {}".format(self.id, self.email)
	
class Staff_Member(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	#user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	first_name = db.Column(db.String(25), default='')
	last_name = db.Column(db.String(30), default='')
	team = db.Column(db.String(40), default='')
	manager = db.Column(db.String(55), default='')
	team_lead = db.Column(db.String(55), default='')
	role = db.Column(db.String(60), default='')
	extension = db.Column(db.String(6), default='')
	phone_number = db.Column(db.String(14), default='')
	location = db.Column(db.String(60), default='')
	active_regions = db.Column(db.String(200), default='')
	office_hours = db.Column(db.String(200), default='')
	duties = db.Column(db.String(600), default='')
	
	#define relationship
	#user = db.relationship('User', backref=db.backref("staff_member", uselist=False), foreign_keys=[user_id])
	
	def __init__(
	self,
	first_name='', 
	last_name='', 
	team='', 
	manager='', 
	team_lead='',
	role='',
	extension='',
	phone_number='',
	location='',
	active_regions='',
	office_hours='',
	duties=''
	#user_id = ''
	):
		self.first_name = first_name
		self.last_name = last_name
		self.team = team
		self.manager = manager
		self.team_lead = team_lead
		self.role = role
		self.extension = extension
		self.phone_number = phone_number
		self.location = location
		self.active_regions = active_regions
		self.office_hours = office_hours
		self.duties = duties
		#self.user_id = user_id
		
	def __repr__(self):
		return "id: {}, name: {}".format(self.id, (self.first_name+self.last_name))
