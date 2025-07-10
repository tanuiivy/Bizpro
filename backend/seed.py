from extensions import db
from models.Authentication import User
from app import create_app

app = create_app()

with app.app_context():
    # Check if admin already exists
    admin = User.query.filter_by(email="admin@bizpro.com").first()
    if not admin:
        admin = User(email="admin@bizpro.com", role="admin")
        admin.set_password("admin@123") 
        db.session.add(admin)
        db.session.commit()
        print("Admin created: admin@bizpro.com / admin@123")
    else:
        print(" Admin already exists")
