# Import the 'app' object from the 'app' module
from app import app

# Check if this script is the main entry point for the application
if __name__ == '__main__':
    # Run the Flask application with debugging enabled
    app.run(debug=True)
