from flask_sqlalchemy import SQLAlchemy

# Capital letters for global scope/global variable
DB = SQLAlchemy()

# Twitter users that we analyze
class User(DB.Model):
    # Setting primary key as id for BOTH USERS AND TWEETS
    # Using BigInteger instead of Integer because the 
    #  twitter IDs are big since twitter has a lot of tweets
    id = DB.Column(DB.BigInteger, primary_key = True)
    
    # Nullable = False means the entry is required
    #  (we need a username to be entered)
    name = DB.Column(DB.String(15), nullable = False)
    newest_tweet_id = DB.Column(DB.BigInteger)
    
    def __repr__(self):
        return '<User {}>'.format(self.name)
    
class Tweet(DB.Model):
    # Setting primary key as id for BOTH USERS AND TWEETS
    # Using BigInteger instead of Integer because the 
    #  twitter IDs are big since twitter has a lot of tweets
    id = DB.Column(DB.BigInteger, primary_key = True)
    # Unicode so we can have emojis as well (up to 500 chars)
    #  because links can be embedded
    text = DB.Column(DB.Unicode(500))
    
    # PickleType = Python standard library package for 
    #  serializing things (saving them for later) 
    #  (serializing takes something (object) and puts it into
    #  memory, translates it into string and then 
    #  deserializes for reverse). It helps us 'magically' 
    #  save the python list of floats)
    #  nullabe = False so we can't save things(tweets) without embeddings
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable = False)
    user = DB.relationship('User', backref = DB.backref('tweets', lazy = True))
    
    def __repr__(self):
        return '<Tweet {}>'.format(self.text)