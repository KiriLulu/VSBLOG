from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from uuid import uuid4

db = SQLAlchemy()
bcrypt  = Bcrypt()

users_roles = db.Table('users_roles',
						db.Column('users_id',db.String(45),db.ForeignKey('users.id')),
						db.Column('roles_id',db.String(45),db.ForeignKey('roles.id'))
						)
posts_tags = db.Table('posts_tags',
					   db.Column('posts_id',db.String(45),db.ForeignKey('posts.id')),
					   db.Column('tags_id',db.String(45),db.ForeignKey('tags.id'))
					   )

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.String(45),primary_key = True)
	username = db.Column(db.String(255),unique = True)
	hash_password = db.Column(db.String(255))
	roles = db.relationship(
			'Role',
			secondary = users_roles,
			backref = db.backref('users',lazy = 'dynamic'))
	
	def __init__(self,username=None,password='default'):
		self.id = str(uuid4())
		self.username = username
		self.hash_password = self.password(password)
		
	def __repr__(self):
		return "< Model User'{}'>".format(self.username)
		

	def password(self,password):
		return bcrypt.generate_password_hash(password)
	
	def confirm_password(self,password):
		return bcrypt.check_password_hash(self.hash_password,password)
	

class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.String(45),primary_key = True)
	title = db.Column(db.String(255))
	text = db.Column(db.Text())
	published_date = db.Column(db.DateTime)
	tags = db.relationship(
			'Tag',
			secondary = posts_tags,
			backref = db.backref('posts',lazy = 'dynamic'))
			
	comments = db.relationship(
			'Comment',
			backref = 'posts',
			lazy = 'dynamic'
			)
			
	def __init__(self,title=None):
		self.id = str(uuid4())
		self.title = title
		
	def __repr__(self):
		return "< Model Post'{}' >".format(self.title)
	

class Tag(db.Model):
	__tablename__ = 'tags'
	id = db.Column(db.String(45),primary_key = True)
	name = db.Column(db.String(225),unique = True)
	description = db.Column(db.String(255))
	
	def __init__(self,name=None):
		self.id = str(uuid4())
		self.name = name
		
	def __repr__(self):
		return "< Model Tag'{}' >".format(self.name)
	

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.String(45),primary_key = True)
	name = db.Column(db.String(225),unique = True)
	description = db.Column(db.String(255))
	
	def __init__(self,name=None):
		self.id = str(uuid4())
		self.name = name
		
	def __repr__(self):
		return "< Model Role'{}' >".format(self.name)
	

class Comment(db.Model):
	__tablename__ = 'comments'
	id = db.Column(db.String(45),primary_key = True)
	title = db.Column(db.String(225))
	contents = db.Column(db.Text())
	published_date = db.Column(db.DateTime)
	post_id = db.Column(db.String(45),db.ForeignKey('posts.id'))
	
	def __init__(self,title=None):
		self.id = str(uuid4())
		self.title = title
		
	def __repr__(self):
		return "< Model Comment'{}' >".format(self.title)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
