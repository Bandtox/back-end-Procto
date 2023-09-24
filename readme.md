# Web Application Project

This is a simple web application project that includes both frontend and backend components. The project is designed to demonstrate a basic web application structure with a navigation bar, a form, and a confirmation box. It uses HTML, CSS, and Python with the Flask framework.

## Features

- Navigation bar with links
- Form for user input

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your local machine.
- Flask installed. You can install it using `pip`:

    ```bash
    pip install Flask Flask-SQLAlchemy
    ```
- or run the given code

    ```bash
    pip install -r requirements.txt
    ```
## Getting Started

To get this project up and running on your local machine, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd backend-flask
    ```
3. Create Database by running database_create.py (Required to run at first instance only)

    ```bash
    python database_create.py
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to view the application.

## Usage

- Navigate the application using the links in the navigation bar.
- Fill out the form with your information and submit it.
- Experience the confirmation box when interacting with the application.


## Acknowledgments

- [Flask](https://flask.palletsprojects.com/en/2.1.x/): The web framework used in this project.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): The markup language for creating web pages.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS): The styling language for web pages.
- [GitHub](https://github.com/): Hosting and version control for open-source projects.

