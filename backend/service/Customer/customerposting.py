from models.Customer.customerposting import CustomerPosting
from extensions import db

# Create
def create_customer_posting(customer_id, product_id, company_id, purchase_type, amount, description, status="pending", payment_date=None):
    posting = CustomerPosting(
        customer_id=customer_id,
        product_id=product_id,
        company_id=company_id,
        purchase_type=purchase_type,
        amount=amount,
        description=description,
        status=status,
        payment_date=payment_date
    )
    db.session.add(posting)
    db.session.commit()
    return posting

# Get all
def get_all_customer_postings():
    return CustomerPosting.query.all()

# Get by ID
def get_customer_posting_by_id(posting_id):
    return CustomerPosting.query.get(posting_id)

# Get by customer
def get_customer_postings_by_customer(customer_id):
    return CustomerPosting.query.filter_by(customer_id=customer_id).all()

# Get by company
def get_customer_postings_by_company(company_id):
    return CustomerPosting.query.filter_by(company_id=company_id).all()

# Update
def update_customer_posting(posting_id, purchase_type=None, amount=None, description=None, status=None, payment_date=None):
    posting = CustomerPosting.query.get(posting_id)
    if not posting:
        return None

    if purchase_type:
        posting.purchase_type = purchase_type
    if amount is not None:
        posting.amount = amount
    if description:
        posting.description = description
    if status:
        posting.status = status
    if payment_date:
        posting.payment_date = payment_date

    db.session.commit()
    return posting

# Delete
def delete_customer_posting(posting_id):
    posting = CustomerPosting.query.get(posting_id)
    if not posting:
        return False

    db.session.delete(posting)
    db.session.commit()
    return True
