# Flask Registration Project

This project is a simple Flask application with user registration functionality, including backend API endpoints, validation, and front-end integration. It also includes unit tests to ensure the application's reliability.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Code Documentation](#code-documentation)
- [Running the Application](#running-the-application)
- [Running Unit Tests](#running-unit-tests)
- [Database](#database)

## Prerequisites

- Python 3.12+
- Pip

## Installation

To set up this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Nour18/Flask-Registration-Project.git
    cd Flask-Registration-Project
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Start the Flask server**:
    ```bash
    python wsgi.py
    ```

## Code Documentation

### Backend

- **`myapp/__init__.py`**: Sets up the Flask application and configure routes.
- **`myapp/models.py`**: Defines the SQLAlchemy models for the application, including the `User` model.
- **`myapp/routes.py`**: Handles routing and user registration logic.

### Frontend

- **`myapp/templates/hompepage.html`**: The homepage with a welcome message and a sign-up button.
- **`myapp/templates/registration.html`**: The registration form where users can sign up.
- **`myapp/static/css/style.css`**: CSS file for styling the front-end pages.

### Unit Tests

- **`myapp/tests/test_app.py`**: Contains unit tests for the application using `pytest`.

## Running the Application

1. **Start the Flask development server**:
    ```bash
    flask run
    ```
   By default, the application will be available at `http://127.0.0.1:5000`.

2. **Navigate to the homepage**:
    Open your browser and go to `http://127.0.0.1:5000`.

## Running Unit Tests

1. **Ensure the virtual environment is activated** (if you created one).

2. **Run the tests**:
    ```bash
    pytest
    ```
   This command will discover and run all test cases defined in the `tests` directory.

## Database
The application uses SQLite for the database. The schema is defined using SQLAlchemy and is created automatically when the application starts.
