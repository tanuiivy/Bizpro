from extensions import db, SerializerMixin
from datetime import datetime

class ProductTransfer(db.Model, SerializerMixin):
    __tablename__ = "product_transfer"

    transfer_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    transfer_quantity = db.Column(db.Float, nullable=False)
    from_location = db.Column(db.String(100), nullable=False) 
    to_location = db.Column(db.String(100), nullable=False) 
    remarks = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # relationship
    product = db.relationship("Product", backref="transfers")

    def __repr__(self):
        return f"<ProductTransfer {self.product_id} from {self.from_location} to {self.to_location}>"
