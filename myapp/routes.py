
from flask import render_template, request, jsonify, redirect, url_for
from myapp import app, db
from myapp.models import User
import re

@app.route('/')
def index():
    return render_template('homepage.html')

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()  
        required_fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']
        errors = []
        for field in required_fields:
            if not data.get(field):
                errors.append(f'{field} is required')
        if errors:
            return jsonify({'error': errors}), 400

        if User.query.filter_by(email=data['email']).first():
            return jsonify({'Error': 'Email already registered','data':data}), 400
        
        if not re.match(r'^\+?1?\d{9,15}$', data['phone_number']):
            return jsonify({'Error': 'Invalid phone number format'}), 400
        
        if not is_valid_email(data['email']):
            return jsonify({'Error': 'Invalid email address'}), 400
        
        new_user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            phone_number=data['phone_number']
        )
        new_user.set_password(data['password'])

        try:
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'Message': 'User registered successfully'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'Error': 'Server error'}), 500

    return render_template('registeration.html')  
