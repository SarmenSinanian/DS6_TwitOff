# Initialize entry point for flask app
from .app import create_app

# In CAPS because it is a global variable
APP = create_app()