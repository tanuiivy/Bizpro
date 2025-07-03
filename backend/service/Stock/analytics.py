from models.Stock.company import Company
from models.Stock.product import Product
from models.Stock.transfer import ProductTransfer
from models.Stock.write_off import WriteOff
from models.Customer.customer import Customer
from models.Customer.customerposting import CustomerPosting

def get_total_companies():
    return Company.query.count()

def get_total_products():
    return Product.query.count()

def get_total_transfers():
    return ProductTransfer.query.count()

def get_pending_transfers():
    return ProductTransfer.query.filter_by(status="pending").count()

def get_total_write_offs():
    return WriteOff.query.count()

def get_customers_per_company():
    data = (
        db.session.query(Customer.company_id, db.func.count(Customer.customer_id))
        .group_by(Customer.company_id)
        .all()
    )
    # returns list of tuples: (company_id, count)
    return [{"company_id": cid, "customer_count": count} for cid, count in data]

def get_customers_per_product():
    data = (
        db.session.query(CustomerPosting.product_id, db.func.count(db.distinct(CustomerPosting.customer_id)))
        .group_by(CustomerPosting.product_id)
        .all()
    )
    return [{"product_id": pid, "customer_count": count} for pid, count in data]

