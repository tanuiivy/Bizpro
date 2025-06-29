from extensions import db, SerializerMixin

class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    method = db.Column(db.String(50))
    reference = db.Column(db.String(255))

    supplier = db.relationship('Supplier', backref=db.backref('payments', lazy=True))

    def __repr__(self):
        return f'<Payment {self.id} - {self.amount}>'
