#individual financial postings for suppliers
from extensions import db, SerializerMixin

class SupplierPosting(db.Model, SerializerMixin):
    __tablename__ = 'supplier_postings'

    posting_id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    posting_date = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    # Relationships
    supplier = db.relationship('Supplier', backref='postings')

    def __repr__(self):
        return f'<SupplierPosting {self.posting_id} for Supplier {self.supplier_id}>'