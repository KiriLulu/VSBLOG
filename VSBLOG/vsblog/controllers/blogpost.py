from os import path
from flask import Blueprint,url_for,render_template
from ..models import Post

blogpost_blueprint = Blueprint(
								'blogpost',
								__name__,
								template_folder=path.join(path.pardir,'templates','blogpost'),
								url_prefix='/blogpost'
								)
								
@blogpost_blueprint.route('/')
def home():
	posts = Post.query.order_by(Post.published_date.desc()).all()
	return render_template('blogpost/home.html',posts = posts)

@blogpost_blueprint.route('/post/<string:post_id>')
def post(post_id):
	post = Post.query.filter_by(Post.id == post_id).first()
	return render_template('blogpost/post.html',post = post)
	