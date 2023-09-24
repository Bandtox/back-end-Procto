from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Create a Flask web application instance

# Configure the database URI for SQLAlchemy to use SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'

# Create an SQLAlchemy database instance connected to the Flask app
db = SQLAlchemy(app)

from app import routes  # Import the routes module to define application routes
