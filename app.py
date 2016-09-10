from flask import Flask, jsonify, abort, request, make_response, url_for, render_template, flash, redirect
from database import db
from models import Staff_Member, Users
from flask.ext.login import LoginManager, login_user, login_required, logout_user
import os.path
from PIL import Image
from flask_uploads import UploadSet, IMAGES, configure_uploads
#from flask_bootstrap import Bootstrap
#from flask_nav import Nav
#from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from forms import LoginForm

app = Flask(__name__)
app.debug = True
app.config.from_pyfile('config.py')


import api_json
#api = Api(app)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
#Bootstrap(app)

images_folder = '/static/img/'
image_directory = os.getcwd() + images_folder
image_size = (128, 128)
thumbnail_size = (64, 64)

#app.config['UPLOADED_PHOTOS_DEST'] = image_directory

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

'''nav = Nav()

nav.register_element('top', Navbar(
	"Memory",
	Link('Google', 'login'),
	Subgroup(
		'Docs',
		Link('Flask-Bootstrap', 'http://pythonhosted.org/Flask-Bootstrap'),
		Link('Flask-AppConfig', 'https://github.com/mbr/flask-appconfig')
)))

nav.init_app(app)'''

teams_list = [
	'Accounts Team',
	'Development Team',
	'Grow Team',
	'Marketing Team',
	'Operations Team',
	'Sales Team',
	'Support Team'
]

@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	success = ''
	if request.args.get('result'):
		if request.args.get('result') == 'True':
			success = True;
	form = LoginForm()
	if form.is_submitted():
		if form.validate():
			#if form.validate_on_submit():
			if Users.query.filter_by(email=form['email']._value()).first():
				user = Users.query.filter_by(email=form['email']._value()).first()
				if user.password == form['password']._value():
					login_user(user)
					for attr, value in user.staff.__dict__.items():
						if value == "":
							return redirect(url_for('update', id=user.id))
					return redirect(url_for('search'))
				else:
					flash('Invalid Credentials. Please Try Again.', 'error')
			else:
				flash('Invalid Credentials. Please Try Again.', 'error')
		else:
			flash('Invalid Credentials. Please Try Again.', 'error')
	if success:
		flash('Successfully registered. Please log in.', 'success')
	return render_template("login.html", form=form)

@app.route('/logout')
def logout():
	logout_user()
	flash('You have successfully logged out.', 'success')
	return redirect(url_for('login'))

@app.route('/register', methods=['GET'])
def register():
	logout_user()
	return render_template('register.html')

@app.route('/search')
@login_required
def search():
	return render_template('search.html', teams=teams_list)

@app.route('/member/<id>', methods=["GET"])
@login_required
def get_member(id):
	if not Users.query.get(id):
		abort(404)
	return render_template("member.html", id=id, teams=teams_list)

@app.route('/update/<id>', methods=['GET'])
@login_required
def update(id):
	if not Users.query.get(id):
		abort(404)
	return render_template("update.html", id=id, teams=teams_list)


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        #try:
        filename = photos.save(request.files['photo'])
        #except:
            #print("Error: Unable to upload image.")
            #abort(500)
        try:
            uploaded_image = Image.open(image_directory+filename)
        except:
            print("Error: Unable to open image file.")
            abort(500)
        try:
        	filetype_index = filename.rfind('.')
        	filename = filename[0:filetype_index]
        	resized_image = uploaded_image.resize(image_size, Image.ANTIALIAS)
        	resized_image.save(image_directory+filename+'.png', 'PNG')
        except:
            print("Error: Unable to save converted image.")
            abort(500)
        try:
            #uploaded_image.thumbnail(thumbnail_size)
        	thumbnail_image = uploaded_image.resize(thumbnail_size, Image.ANTIALIAS)
        	#filetype_index = filename.rfind('.')
        	#filename = filename[0:filetype_index]
        	thumbnail_image.save(image_directory+filename+'_thumb.png', 'PNG')
        except:
            print("Error: Unable to save thumbnail image.")
        #flash(filename+" successfully uploaded")
        return jsonify({
        	'Result': True,
        	'Image URI': image_directory+filename+'.png',
        	'Thumbnail URI': image_directory+filename+'_thumb.png'
        	}), 200