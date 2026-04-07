from flask import request
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt
from app import db
from app.models import User
from app.services import facade

api = Namespace('admin', description='Admin operations')

@api.route('/users/')
class AdminUserCreate(Resource):
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = request.json or {}
        email = user_data.get('email')
        password = user_data.get('password')

        if not email or not password:
            return {'error': 'Email and password are required'}, 400

        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        new_user = User(email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User created successfully', 'user_id': new_user.id}, 201
