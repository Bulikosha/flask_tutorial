from flask import Blueprint
from flask import render_template

from models import Post

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def index():
	posts = Post.query.all()
	return render_template('posts/index.html', posts=posts)

# example: http://localhost/blog/first-post - "first-post" translates to decorater and function then translates to query expression
@posts.route('/<slug>') # text between < > is name of parameter as in following function's argument
def post_detail(slug):
	post = Post.query.filter(Post.slug == slug).first() #since initial slug is unique we need to use 'first()'
	return render_template('posts/post_detail.html', post=post)
