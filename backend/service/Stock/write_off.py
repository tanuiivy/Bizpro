from extensions import db
from models.Stock.product import Product
from models.Stock.write_off import WriteOff

def create_write_off(product_id, write_off_quantity, buying_price, expiry_date=None, remarks=None):
    # Check if product exists
    product = Product.query.get(product_id)
    if not product:
        return None

    new_write_off = WriteOff(
        product_id=product_id,
        write_off_quantity=write_off_quantity,
        buying_price=buying_price,
        expiry_date=expiry_date,
        remarks=remarks
    )
    db.session.add(new_write_off)
    db.session.commit()
    return new_write_off

def get_write_off_by_id(write_off_id):
    return WriteOff.query.get(write_off_id)

def get_all_write_offs():
    return WriteOff.query.all()

def get_write_offs_by_product_id(product_id):
    return WriteOff.query.filter_by(product_id=product_id).all()


def update_write_off(write_off_id, write_off_quantity=None, buying_price=None, expiry_date=None, remarks=None):
    write_off = WriteOff.query.get(write_off_id)
    if not write_off:
        return None

    if write_off_quantity is not None:
        write_off.write_off_quantity = write_off_quantity
    if buying_price is not None:
        write_off.buying_price = buying_price
    if expiry_date is not None:
        write_off.expiry_date = expiry_date
    if remarks is not None:
        write_off.remarks = remarks

    db.session.commit()
    return write_off

def delete_write_off(write_off_id):
    write_off = WriteOff.query.get(write_off_id)
    if not write_off:
        return False

    db.session.delete(write_off)
    db.session.commit()
    return True
