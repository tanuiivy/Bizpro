from models.Customer.customer import Customer
from models.Customer.customerposting import CustomerPosting
from extensions import db
from sqlalchemy import func

# Total revenue
def get_total_customer_revenue():
    return db.session.query(func.sum(CustomerPosting.amount)).filter_by(status="paid").scalar() or 0

# Pending payments
def get_pending_payments():
    return db.session.query(func.sum(CustomerPosting.amount)).filter_by(status="pending").scalar() or 0

# Total postings
def get_total_postings():
    return CustomerPosting.query.count()

# Total customers
def get_total_customers():
    return Customer.query.count()

# Helper to extract top item per customer
def _get_top_item_per_customer(group_field):
    data = (
        db.session.query(
            CustomerPosting.customer_id,
            Customer.fullname,
            getattr(CustomerPosting, group_field),
            func.sum(CustomerPosting.amount).label("total_amount")
        )
        .join(Customer, Customer.customer_id == CustomerPosting.customer_id)
        .group_by(CustomerPosting.customer_id, getattr(CustomerPosting, group_field), Customer.fullname)
        .order_by(CustomerPosting.customer_id, func.sum(CustomerPosting.amount).desc())
        .all()
    )

    result = {}
    for row in data:
        if row.customer_id not in result:
            result[row.customer_id] = {
                "customer_id": row.customer_id,
                "customer_name": row.fullname,
                f"top_{group_field}_id": getattr(row, group_field),
                "total_amount": row.total_amount,
            }
    return list(result.values())

# Top company per customer
def get_top_company_per_customer():
    return _get_top_item_per_customer("company_id")

# Top product per customer
def get_top_product_per_customer():
    return _get_top_item_per_customer("product_id")
