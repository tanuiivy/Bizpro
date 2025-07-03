from extensions import db, SerializerMixin
from sqlalchemy import Enum
from models.Stock.company import Company
from datetime import datetime

class Customer(db.Model, SerializerMixin):
    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.company_id'), nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(50), nullable=True)
    purchase_type = db.Column(Enum("wholesale", "retail", "vip", "others", name="purchase_type_enum"),default="retail",nullable=False)
    payment_method = db.Column(Enum("cash", "card", "check", name="payment_method_enum"),default="cash",nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship
    postings = db.relationship("CustomerPosting", backref="customer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Customer {self.fullname}>"
