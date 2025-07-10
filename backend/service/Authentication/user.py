from models.Authentication.user import User
from extensions import db

def create_user(email, role="supplier", username=None):
    new_user = User(email=email, role=role, username=username)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def set_user_password(user_id, password):
    user = User.query.get(user_id)
    if user:
        user.set_password(password)
        db.session.commit()
    return user

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None