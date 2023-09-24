from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Note  # Import the 'Note' model

@app.route('/')  # Define a route for the home page
def index():
    notes = Note.query.all()  # Query all notes from the database
    return render_template('view_notes.html', notes=notes)  # Render the 'view_notes.html' template and pass notes data

@app.route('/create', methods=['GET', 'POST'])  # Define a route for creating a new note
def create_note():
    if request.method == 'POST':  # Check if the request method is POST
        title = request.form['title']  # Get the title from the form
        content = request.form['content']  # Get the content from the form
        if title and content:  # Check if both title and content are provided
            note = Note(title=title, content=content)  # Create a new 'Note' object
            db.session.add(note)  # Add the new note to the database session
            db.session.commit()  # Commit the changes to the database
            return redirect(url_for('index'))  # Redirect to the home page after creating the note
    return render_template('create_note.html')  # Render the 'create_note.html' template for creating a new note

@app.route('/edit/<int:id>', methods=['GET', 'POST'])  # Define a route for editing a note
def edit_note(id):
    note = Note.query.get(id)  # Retrieve the note by its ID
    if request.method == 'POST':  # Check if the request method is POST
        note.title = request.form['title']  # Update the note title
        note.content = request.form['content']  # Update the note content
        db.session.commit()  # Commit the changes to the database
        return redirect(url_for('index'))  # Redirect to the home page after editing the note
    return render_template('edit_note.html', note=note)  # Render the 'edit_note.html' template for editing a note

@app.route('/delete/<int:id>', methods=['POST'])  # Define a route for deleting a note (POST method)
def delete_note(id):
    note = Note.query.get(id)  # Retrieve the note by its ID
    db.session.delete(note)  # Delete the note from the database
    db.session.commit()  # Commit the changes to the database
    return redirect(url_for('index'))  # Redirect to the home page after deleting the note

@app.route('/delete/<int:id>', methods=['GET', 'POST'])  # Define a route for confirming note deletion
def delete_confirm(id):
    note = Note.query.get(id)  # Retrieve the note by its ID
    if request.method == 'POST':  # Check if the request method is POST
        db.session.delete(note)  # Delete the note from the database
        db.session.commit()  # Commit the changes to the database
        return redirect(url_for('index'))  # Redirect to the home page after confirming deletion
    return render_template('delete_confirm.html', note=note)  # Render the 'delete_confirm.html' template for confirmation

if __name__ == '__main__':
    app.run()  # Run the Flask application if this script is executed directly
