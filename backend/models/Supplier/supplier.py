from extensions import db, SerializerMixin

class Supplier(db.Model, SerializerMixin):
    __tablename__= 'suppliers'

    supplier_id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255))
    supplier_name = db.Column(db.String(100), nullable=False)
    supplier_email = db.Column(db.String(100), nullable=False, unique=True)
    supplier_phone = db.Column(db.String(10), nullable=False, unique=True)
    supplier_address = db.Column(db.String(200), nullable=False)
    supplier_balance = db.Column(db.Float,nullable=False, default=0.0)
    contact_person = db.Column(db.String(100), nullable=False)
    contact_person_no = db.Column(db.String(10), nullable=False)
    package_mode = db.Column(db.Text)
    vat = db.Column(db.Boolean, default=False)
    stock = db.Column(db.Boolean, default=False)
    utility = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now(), server_default=db.func.now())

    def __repr__(self):
        return f'<Supplier {self.supplier_name}>'