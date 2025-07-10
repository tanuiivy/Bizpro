from extensions import db
from models.Supplier import Supplier
from models.Supplier import Invoice

#create a new supplier
def create_supplier(data):
    new_supplier = Supplier(
        supplier_name=data.get('supplier_name'),
        supplier_email=data.get('supplier_email'),
        supplier_phone=data.get('supplier_phone'),
        supplier_address=data.get('supplier_address'),
        supplier_balance=data.get('supplier_balance', 0.0),
        contact_person=data.get('contact_person'),
        contact_person_no=data.get('contact_person_no'),
        package_mode=data.get('package_mode'),
        vat=data.get('vat', False),
        stock=data.get('stock', False),
        utility=data.get('utility', False),
        #image_path=data.get('image_path')
    )
    
    db.session.add(new_supplier)
    db.session.commit()
    return new_supplier

#read- get all suppliers
def get_all_suppliers():
    return Supplier.query.all()

#read- get a supplier by id
def get_supplier_by_id(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    return supplier

#read- get most recent supplier
def get_most_recent_supplier():
    supplier = Supplier.query.order_by(Supplier.updated_at.desc()).first()
    return supplier

#read- get supplier by invoice status
def get_suppliers_by_invoice_status(status):
    suppliers = Supplier.query.join(Supplier.invoices).filter(Invoice.status == status).all()
    return suppliers

#update a supplier
def update_supplier(supplier, data):
    for key, value in data.items():
        setattr(supplier, key, value)
    db.session.commit()
    return supplier

#delete a supplier
def delete_supplier(supplier):
    db.session.delete(supplier)
    db.session.commit()
    