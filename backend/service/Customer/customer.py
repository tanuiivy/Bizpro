from extensions import db
from models.Customer.customer import Customer

# Create a customer
def create_customer(company_id, fullname, email=None, phone=None, purchase_type="retail", payment_method="cash"):
    new_customer = Customer(
        company_id=company_id,
        fullname=fullname,
        email=email,
        phone=phone,
        purchase_type=purchase_type,
        payment_method=payment_method
    )
    db.session.add(new_customer)
    db.session.commit()
    return new_customer

# Get all customers
def get_all_customers():
    return Customer.query.all()

# Get customer by ID
def get_customer_by_id(customer_id):
    return Customer.query.get(customer_id)

# Get customers by company
def get_customers_by_company(company_id):
    return Customer.query.filter_by(company_id=company_id).all()

# Get customers by payment method
def get_customers_by_payment_method(payment_method):
    return Customer.query.filter_by(payment_method=payment_method).all()

# Get customers by purchase type
def get_customers_by_purchase_type(purchase_type):
    return Customer.query.filter_by(purchase_type=purchase_type).all()

# Update customer
def update_customer(customer_id, fullname=None, email=None, phone=None, purchase_type=None, payment_method=None):
    customer = Customer.query.get(customer_id)
    if not customer:
        return None

    if fullname is not None:
        customer.fullname = fullname
    if email is not None:
        customer.email = email
    if phone is not None:
        customer.phone = phone
    if purchase_type is not None:
        customer.purchase_type = purchase_type
    if payment_method is not None:
        customer.payment_method = payment_method

    db.session.commit()
    return customer

# Delete customer
def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return False

    db.session.delete(customer)
    db.session.commit()
    return True
