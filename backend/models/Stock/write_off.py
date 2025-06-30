from extensions import db, SerializerMixin
from datetime import datetime

class WriteOff(db.Model, SerializerMixin):
    __tablename__ = "write_off"

    write_off_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    write_off_quantity = db.Column(db.Float, nullable=False)
    buying_price = db.Column(db.Float, nullable=False)
    expiry_date = db.Column(db.Date, nullable=True)
    remarks = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # relationship
    product = db.relationship("Product", backref="write_offs")

    def __repr__(self):
        return f"<WriteOff {self.product_id} qty {self.write_off_quantity}>"

