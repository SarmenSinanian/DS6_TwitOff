from flask_sqlalchemy import SQLAlchemy

# Capital letters for global scope/global variable
DB = SQLAlchemy()

# Twitter users that we analyze
class User(DB.Model):
    # Setting primary key as id for BOTH USERS AND TWEETS
    id = DB.Column(DB.Integer, primary_key = True)
    
    # Nullable = False means the entry is required
    #  (we need a username to be entered)
    name = DB.Column(DB.String(15), nullable = False)
    # Setting primary key as id for BOTH USERS AND TWEETS
class Tweet(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    # Unicode so we can have emojis as well (up to 280 chars)
    text = DB.Column(DB.Unicode(280))