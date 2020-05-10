from app import db
from datetime import datetime
import re

def slugify(s):
	#function to convert post title to URL
	pattern = r'[^\w+]' # every non-letter character is selected
	return re.sub(pattern, '-', s) # and changed to '-' symbol

class Post(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140))
	slug = db.Column(db.String(140), unique=True) # it is URL
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args, **kwargs)
		self.generate_slug()

	def generate_slug(self):
		if self.title:
			self.slug = slugify(self.title)

	def __repr__(self):
		# function to represent output to readible view
		return '<Post id: {}, title: {}>'.format(self.id, self.title)

