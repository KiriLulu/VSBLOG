from flask import Flask

from vsblog.extensions import f_admin
from vsblog.models import db,bcrypt,User,Post,Comment,Tag,Role
from vsblog.controllers.admin import CustomView,CustomModelView,PostView
from vsblog.controllers.blogpost import blogpost_blueprint
from vsblog.controllers.main import main_blueprint

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config_name)
	
	db.init_app(app)
	bcrypt.init_app(app)
	f_admin.init_app(app)
	f_admin.add_view(CustomView(name="Gate"))
	models = [User,Comment,Tag,Role]
	for model in models:
		f_admin.add_view(CustomModelView(model,db.session,category='Models'))
		
	f_admin.add_view(PostView(Post,db.session,category='PostManager'))
	
	app.register_blueprint(blogpost_blueprint)
	app.register_blueprint(main_blueprint)
	return app