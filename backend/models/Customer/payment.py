from extensions import db, SerializerMixin
from sqlalchemy import Enum
from models.Stock.product import Product
from models.Stock.company import Company
from datetime import datetime

class PaymentForm(db.Model, SerializerMixin):
    __tablename__ = "payment_forms"

    payment_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    posting_id = db.Column(db.Integer, db.ForeignKey('customer_postings.customer_postings_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.company_id'), nullable=False)
    amount_paid = db.Column(db.Float, nullable=False)
    payment_method = db.Column(Enum("cash", "card", "check", name="payment_method_enum"), nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    posting = db.relationship("CustomerPosting", backref="payments")

    def __repr__(self):
        return f"<PaymentForm {self.payment_id} - Customer {self.customer_id} - Product {self.product_id} - Company {self.company_id}>"
