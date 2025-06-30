from extensions import db
from models.Supplier import Supplier
from models.Supplier import Invoice

#create a new supplier
def create_supplier(data):
    #new_supplier = Supplier(**data)
    db.session.add(data)
    db.session.commit()
    return data

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
    