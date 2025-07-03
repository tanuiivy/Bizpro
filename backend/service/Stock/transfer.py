from extensions import db
from models.Stock.product import Product
from models.Stock.transfer import ProductTransfer

def create_transfer(product_id, transfer_quantity, from_location, to_location, remarks=None):
    # Check if product exists
    product = Product.query.get(product_id)
    if not product:
        return None

    new_transfer = ProductTransfer(
        product_id=product_id,
        transfer_quantity=transfer_quantity,
        from_location=from_location,
        to_location=to_location,
        remarks=remarks
    )
    db.session.add(new_transfer)
    db.session.commit()
    return new_transfer

def get_transfer_by_id(transfer_id):
    return ProductTransfer.query.get(transfer_id)

def get_all_transfers():
    return ProductTransfer.query.all()

def get_transfers_by_product_id(product_id):
    return ProductTransfer.query.filter_by(product_id=product_id).all()

def update_transfer(transfer_id, transfer_quantity=None, from_location=None, to_location=None, remarks=None):
    transfer = ProductTransfer.query.get(transfer_id)
    if not transfer:
        return None

    if transfer_quantity is not None:
        transfer.transfer_quantity = transfer_quantity
    if from_location is not None:
        transfer.from_location = from_location
    if to_location is not None:
        transfer.to_location = to_location
    if remarks is not None:
        transfer.remarks = remarks
    db.session.commit()
    return transfer

def delete_transfer(transfer_id):
    transfer = ProductTransfer.query.get(transfer_id)
    if not transfer:
        return False

    db.session.delete(transfer)
    db.session.commit()
    return True
