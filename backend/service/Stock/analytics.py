from models.Stock.company import Company
from models.Stock.product import Product
from models.Stock.transfer import ProductTransfer
from models.Stock.write_off import WriteOff

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