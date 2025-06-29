from extensions import db, SerializerMixin

class Invoice(db.Model, SerializerMixin):
    __tablename__ = 'invoices'

    invoice_id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'), nullable=False)
    invoice_number = db.Column(db.String(50), nullable=False, unique=True)
    amount = db.Column(db.Float, nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    due_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pending')

    # Relationships
    supplier = db.relationship('Supplier', backref=db.backref('invoices', lazy=True))
    def __repr__(self):
        return f'<Invoice {self.invoice_number} for Supplier {self.supplier_id}>'