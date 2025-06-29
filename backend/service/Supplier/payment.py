from extensions import db
from models.Supplier.payments import Payment

#create a new payment
def create_payment(data):
    new_payment = Payment(**data)
    db.session.add(new_payment)
    db.session.commit()
    return new_payment

#read- get all payments 
def get_all_payments():
    return Payment.query.all()

#read- get payment by id
def get_payment_by_id(payment_id):
    return Payment.query.get_or_404(payment_id)

#read- get payments by supplier id
def get_payments_by_supplier(supplier_id):
    return Payment.query.filter_by(supplier_id=supplier_id).all()

#update a payment
def update_payment(payment, data):
    for key, value in data.items():
        setattr(payment, key, value)
    db.session.commit()
    return payment
    
#delete a payment
def delete_payment(payment):
    db.session.delete(payment)
    db.session.commit()
