from extensions import db, SerializerMixin
from sqlalchemy import Enum
from models.Stock.product import Product
from models.Stock.company import Company
from datetime import datetime

class CustomerPosting(db.Model, SerializerMixin):
    __tablename__ = "customer_postings"

    customer_postings_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.company_id'), nullable=False)
    purchase_type = db.Column(Enum("wholesale", "retail", "vip", "others", name="purchase_type_enum"),default="retail",nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    status = db.Column(Enum("paid", "pending", name="posting_status_enum"), default="pending", nullable=False)
    payment_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    product = db.relationship("Product", backref="customer_postings")

    def __repr__(self):
        return f"<CustomerPosting {self.customer_postings_id} - Customer {self.customer_id} - Company {self.company_id}>"
