#reference.py for the things in product that say add new
from extensions import db
from datetime import datetime

class ProductCategory(db.Model):
    __tablename__ = "product_categories"
    category_id = db.Column(db.Integer, primary_key=True)
    product_category = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    products = db.relationship("Product", backref="product_category", lazy=True)

class ProductSubCategory(db.Model):
    __tablename__ = "product_sub_categories"
    sub_category_id = db.Column(db.Integer, primary_key=True)
    product_sub_category = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    products = db.relationship("Product", backref="product_sub_category", lazy=True)

class Shop(db.Model):
    __tablename__ = "shops"
    shop_id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    products = db.relationship("Product", backref="shop", lazy=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.company_id'))

class Store(db.Model):
    __tablename__ = "stores"
    store_id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.company_id'), nullable=False)
    store_name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    products = db.relationship("Product", backref="store", lazy=True)
    shelves = db.relationship("Shelf", backref="store", lazy=True)

class Shelf(db.Model):
    __tablename__ = "shelves"
    shelf_id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'))
    shelf_name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    products = db.relationship("Product", backref="shelf", lazy=True)

class PackageMode(db.Model):
    __tablename__ = "package_modes"
    package_mode_id = db.Column(db.Integer, primary_key=True)
    package_mode = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    products = db.relationship("Product", backref="package_mode", lazy=True)
