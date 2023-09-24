from app import db  # Import the database instance from the 'app' module

class Note(db.Model):  # Define a SQLAlchemy model named 'Note'
    id = db.Column(db.Integer, primary_key=True)  # Define an integer primary key field for the note
    title = db.Column(db.String(100))  # Define a string field for the note title (maximum length 100 characters)
    content = db.Column(db.Text)  # Define a text field for the note content (for longer text)

    def __repr__(self):
        return f'<Note {self.title}>'  # Define a representation for the Note object (used for debugging)
