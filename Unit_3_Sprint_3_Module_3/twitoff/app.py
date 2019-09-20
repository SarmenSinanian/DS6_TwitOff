from decouple import config
from flask import Flask, render_template, request
from .models import DB, User

# Make our own app factory that adds configuaration
#  and routing:
def create_app():
    # Creating the server:
    app = Flask(__name__)
    
    # Add configuration here later:
    #  Using _URI because it is a more general category
    #   than URL.
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    
    # Reset the ENV with a new one?
    app.config['ENV'] = config('ENV')
    
    # Stop tracking modifications
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Now the database knows about the app
    DB.init_app(app)
    
    # Create the route:
    @app.route('/')
    
    # Define the function:
    def root():
        users = User.query.all()
        return render_template('base.html', title = 'Home', users = users)
    
    # For convenience: reset() drops everything and starts
    #  everything, users blanked out. Taken out of public 
    #  version of app. In future implementation, we could
    #  allow the reset for admins if we have user functions.
    #  Done with app 'decorator' @loginrequired
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template ('base.html', title = 'DB RESET!', user = [])

    return app