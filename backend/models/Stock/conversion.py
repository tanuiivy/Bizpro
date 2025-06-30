from extensions import db, SerializerMixin
from datetime import datetime

class ProductConversion(db.Model, SerializerMixin):
    __tablename__ = "product_conversion"

    conversion_id = db.Column(db.Integer, primary_key=True)
    from_product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    to_product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    unit_before = db.Column(db.String(50), nullable=False)
    conversion_quantity = db.Column(db.Float, nullable=False)
    unit_after = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # relationships
    from_product = db.relationship("Product", foreign_keys=[from_product_id], backref="conversions_from")
    to_product = db.relationship("Product", foreign_keys=[to_product_id], backref="conversions_to")

    def __repr__(self):
        return f"<ProductConversion from {self.from_product_id} to {self.to_product_id}>"
