from extensions import db, SerializerMixin
from .reference import ProductCategory, ProductSubCategory, Shop, Store, Shelf, PackageMode
from datetime import datetime

class Product(db.Model, SerializerMixin):
    __tablename__= "products"

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False, unique=True)   
    product_description = db.Column(db.String(255), nullable=True)
    part_number = db.Column(db.String(50), nullable=True)
    barcode = db.Column(db.String(50), nullable=True, unique=True)
    buying_price = db.Column(db.Float, nullable=False)
    wholesale_price = db.Column(db.Float, nullable=False)
    retail_price = db.Column(db.Float, nullable=False)
    product_type = db.Column(db.String(50), nullable=False)
    # Foreign keys to reference tables
    product_category_id = db.Column(db.Integer, db.ForeignKey('product_categories.category_id'), nullable=False)
    product_sub_category_id = db.Column(db.Integer, db.ForeignKey('product_sub_categories.sub_category_id'), nullable=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.shop_id'), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=False)
    shelf_id = db.Column(db.Integer, db.ForeignKey('shelves.shelf_id'))
    package_mode_id = db.Column(db.Integer, db.ForeignKey('package_modes.package_mode_id'), nullable=True)
    shelf_names = db.Column(db.ARRAY(db.String), nullable=True)
    shop_quantity = db.Column(db.Integer, nullable=False, default=0) 
    store_quantity = db.Column(db.Integer, nullable=False, default=0) 
    #checkboxes
    component = db.Column(db.Boolean, default=False)
    hot_list= db.Column(db.Boolean, default=False)
    dormant = db.Column(db.Boolean, default=False)
    apply_vat = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Product {self.product_name}>"