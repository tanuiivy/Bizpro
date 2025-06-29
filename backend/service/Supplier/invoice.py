from extensions import db
from models.Supplier.invoice import Invoice

#create a new supplier invoice
def create_invoice(data):
    new_invoice = Invoice(**data)
    db.session.add(new_invoice)
    db.session.commit()
    return new_invoice

#read- get all invoices
def get_all_invoices():
    return Invoice.query.all()

#read- get invoice by id 
def get_invoice_by_id(invoice_id):
    return Invoice.query.get_or_404(invoice_id)

#read- get invoices by supplier id
def get_invoices_by_supplier(supplier_id):
    return Invoice.query.filter_by(supplier_id=supplier_id).all()

#update an invoice
def update_invoice(invoice, data):
    for key, value in data.items():
        setattr(invoice, key, value)
    db.session.commit()
    return invoice
    
#delete an invoice
def delete_invoice(invoice):
    db.session.delete(invoice)
    db.session.commit()
