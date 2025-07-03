from extensions import db
from models.Customer import PaymentForm

# Create a payment
def create_payment(customer_id, posting_id, product_id, company_id, amount_paid, payment_method, payment_date=None, notes=None):
    payment = PaymentForm(
        customer_id=customer_id,
        posting_id=posting_id,
        product_id=product_id,
        company_id=company_id,
        amount_paid=amount_paid,
        payment_method=payment_method,
        payment_date=payment_date,
        notes=notes
    )
    db.session.add(payment)
    db.session.commit()
    return payment

# Get all payments
def get_all_payments():
    return PaymentForm.query.all()

# Get payment by id
def get_payment_by_id(payment_id):
    return PaymentForm.query.get(payment_id)

# Get payments by customer
def get_payments_by_customer(customer_id):
    return PaymentForm.query.filter_by(customer_id=customer_id).all()

# Get payments by company
def get_payments_by_company(company_id):
    return PaymentForm.query.filter_by(company_id=company_id).all()

# Update a payment
def update_payment(payment_id, amount_paid=None, payment_method=None, payment_date=None, notes=None):
    payment = PaymentForm.query.get(payment_id)
    if not payment:
        return None
    
    if amount_paid is not None:
        payment.amount_paid = amount_paid
    if payment_method is not None:
        payment.payment_method = payment_method
    if payment_date is not None:
        payment.payment_date = payment_date
    if notes is not None:
        payment.notes = notes

    db.session.commit()
    return payment

# Delete a payment
def delete_payment(payment_id):
    payment = PaymentForm.query.get(payment_id)
    if not payment:
        return False

    db.session.delete(payment)
    db.session.commit()
    return True
