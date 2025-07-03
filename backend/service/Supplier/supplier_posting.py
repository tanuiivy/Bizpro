from extensions import db
from models.Supplier.supplier_posting import SupplierPosting

#create a new supplier posting
def create_supplier_posting(data):
    new_posting = SupplierPosting(**data)
    db.session.add(new_posting)
    db.session.commit()
    return new_posting

#read- get all supplier postings
def get_all_supplier_postings():
    return SupplierPosting.query.all()

#read- get supplier posting by id
def get_supplier_posting_by_id(posting_id):
    return SupplierPosting.query.get_or_404(posting_id)

#read- get postings by supplier id
def get_postings_by_supplier(supplier_id):
    return SupplierPosting.query.filter_by(supplier_id=supplier_id).all()

#read- get postings by product id
def get_postings_by_product(product_id):
    return SupplierPosting.query.filter_by(product_id=product_id).all()
    
#read- get postings by company id
def get_postings_by_company(company_id):
    return SupplierPosting.query.filter_by(company_id=company_id).all()

#update a supplier posting
def update_supplier_posting(posting, data):
    for key, value in data.items():
        setattr(posting, key, value)
    db.session.commit()
    return posting
    
#delete a supplier posting
def delete_supplier_posting(posting):
    db.session.delete(posting)
    db.session.commit()
