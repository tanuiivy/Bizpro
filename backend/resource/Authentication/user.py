from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from service.Authentication.user import create_user, set_user_password, authenticate_user
from models.Authentication.user import User

class CreateUserResource(Resource):
    @jwt_required()
    def post(self):
        current_user_id = get_jwt_identity()
        admin = User.query.get(int(current_user_id))
        if not admin or admin.role != "admin":
            return {"message": "Only admin can create users"}, 403

        data = request.json
        email = data.get("email")
        username = data.get("username")
        role = data.get("role", "supplier")
        new_user = create_user(email, role, username)
        return {"message": "User created", "user": new_user.to_dict()}, 201

class SetPasswordResource(Resource):
    def post(self, user_id):
        data = request.json
        email = data.get("email")
        password = data.get("password")
        user = set_user_password(user_id, password)
        if not user:
            return {"message": "User not found"}, 404
        return {"message": "Password set successfully"}, 200

class LoginResource(Resource):
    def post(self):
        data = request.json
        email = data.get("email")
        password = data.get("password")
        user = authenticate_user(email, password)
        if not user:
            return {"message": "Invalid email or password"}, 401
        access_token = create_access_token(identity=str(user.id))
        return {"access_token": access_token, "role": user.role}, 200

class ForgotPasswordResource(Resource):
    def post(self):
        data = request.json
        email = data.get("email")
        user = User.query.filter_by(email=email).first()
        if not user:
            return {"message": "Email not found"}, 404

        reset_token = create_access_token(identity=str(user.id))
        return {"message": "Password reset instructions sent", "token": reset_token}, 200

class UserListResource(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        admin = User.query.get(int(current_user_id))
        if not admin or admin.role != "admin":
            return {"message": "Only admin can view users"}, 403

        users = User.query.all()
        return {"users": [user.to_dict() for user in users]}, 200

class DeleteUserResource(Resource):
    @jwt_required()
    def delete(self, user_id):
        current_user_id = get_jwt_identity()
        admin = User.query.get(int(current_user_id))
        if not admin or admin.role != "admin":
            return {"message": "Only admin can delete users"}, 403

        user = User.query.get(int(user_id))
        if not user:
            return {"message": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200