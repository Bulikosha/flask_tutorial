from app import app
from app import db

from posts.blueprint import posts

import view

app.register_blueprint(posts, url_prefix='/blog') #registration of blue print in our app. 
#First argument = instance variable of Blueprint module, second argument = is a piece of our URL


if __name__=='__main__':
	app.run()