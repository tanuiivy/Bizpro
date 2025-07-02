from models.Stock.conversion import ProductConversion
from extensions import db

def create_conversion(data):
    conversion = ProductConversion(
        from_product_id = data["from_product_id"],
        to_product_id = data["to_product_id"],
        unit_before = data["unit_before"],
        conversion_quantity = data["conversion_quantity"],
        unit_after = data["unit_after"],
    )
    db.session.add(conversion)
    db.session.commit()
    return conversion

def get_all_conversions():
    return ProductConversion.query.all()

def get_conversion_by_id(conversion_id):
    return ProductConversion.query.get(conversion_id)

def update_conversion(conversion_id, data):
    conversion = ProductConversion.query.get(conversion_id)
    if not conversion:
        return None
    for key, value in data.items():
        if hasattr(conversion, key):
            setattr(conversion, key, value)
    db.session.commit()
    return conversion

def delete_conversion(conversion_id):
    conversion = ProductConversion.query.get(conversion_id)
    if not conversion:
        return None
    db.session.delete(conversion)
    db.session.commit()
    return conversion
