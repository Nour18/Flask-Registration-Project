import pytest
from myapp import app, db
from myapp.models import User


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.app_context():
        db.create_all()
        with app.test_client() as client:
            yield client
        db.drop_all()

def test_register_user(client):
    response = client.post('/register', json={
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'phone_number': '1234567890',
        'password': 'password123'
    })
    assert response.status_code == 201
    assert b'User registered successfully' in response.data

def test_missing_field(client):
    response = client.post('/register', json={
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'password': 'password123'
    })
    assert response.status_code == 400
    assert b'phone_number is required' in response.data

def test_duplicate_email(client):
    client.post('/register', json={
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'phone_number': '1234567890',
        'password': 'password123'
    })
    response = client.post('/register', json={
        'first_name': 'Jane',
        'last_name': 'Smith',
        'email': 'john.doe@example.com',
        'phone_number': '0987654321',
        'password': 'newpassword456'
    })
    assert response.status_code == 400
    assert b'Email already registered' in response.data

def test_invalid_phone_number(client):
    response = client.post('/register', json={
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'phone_number': 'invalid_phone',
        'password': 'password123'
    })
    assert response.status_code == 400
    assert b'Invalid phone number format' in response.data 
def test_invalid_email_format(client):
    invalid_emails = [
        'plainaddress',
        'missingatsign.com',
        '@missingusername.com',
        'username@.com',
        'user@domain',
        'user@domain,com'
    ]

    for email in invalid_emails:
        response = client.post('/register', json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': email,
            'phone_number': '1234567890',
            'password': 'password123'
        })
        assert response.status_code == 400
        assert b'Invalid email address' in response.data

def test_valid_email_format(client):
    valid_emails = [
        'user@example.com',
        'user.name@example.co',
        'user_name@example.com',
        'user-name@example.com',
        'username@example.com'
    ]

    for email in valid_emails:
        response = client.post('/register', json={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': email,
            'phone_number': '1234567890',
            'password': 'password123'
        })
        assert response.status_code == 201
        assert b'User registered successfully' in response.data