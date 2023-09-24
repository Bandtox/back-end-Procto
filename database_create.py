# Import necessary modules and objects from the 'app' package
from app import db, app

# Create a new application context to work with the Flask app
with app.app_context():

    # Use SQLAlchemy's db.create_all() to create the database tables
    db.create_all()

# This script initializes the database schema by creating necessary tables.
# It is typically run once to set up the database structure.
# The 'app.app_context()' ensures that the script operates within the context of the Flask application.
