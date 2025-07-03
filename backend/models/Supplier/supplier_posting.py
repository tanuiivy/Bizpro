#individual financial postings for suppliers
from extensions import db, SerializerMixin
from models.Stock.product import Product
from models.Stock.company import Company

class SupplierPosting(db.Model, SerializerMixin):
    __tablename__ = 'supplier_postings'

    posting_id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.company_id'), nullable=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    posting_date = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    # Relationships
    supplier = db.relationship('Supplier', backref='postings')
    product = db.relationship('Product', backref='supplier_postings')
    company = db.relationship('Company', backref='supplier_postings')

    def __repr__(self):
        return f'<SupplierPosting {self.posting_id} for Supplier {self.supplier_id}>'