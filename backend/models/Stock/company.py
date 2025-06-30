from extensions import db, SerializerMixin
from datetime import datetime

class Company(db.Model, SerializerMixin):
    __tablename__ = "companies"

    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False, unique=True)
    company_email = db.Column(db.String(100), nullable=False, unique=True)
    company_phone = db.Column(db.String(20), nullable=False)
    company_phone_2 = db.Column(db.String(20), nullable=True)
    county = db.Column(db.String(50), nullable=False)
    sub_county = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    company_address = db.Column(db.String(200), nullable=False)
    company_address_2 = db.Column(db.String(200), nullable=True)
    zip_code = db.Column(db.String(20), nullable=True)
    #shop_name= db.Column(db.String(100), nullable=False)
    #store_name = db.Column(db.String(100), nullable=False)
    #shelf_names = db.Column(db.ARRAY(db.String), nullable=True)
    stores = db.relationship("Store", backref="company", lazy=True)
    product_category = db.Column(db.String(255), nullable=True)
    product_sub_category = db.Column(db.String(255), nullable=True)
    vat = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Company {self.company_name}>"


