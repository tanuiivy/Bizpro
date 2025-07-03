from extensions import db
from models.Stock.product import Product

# Create a new product
def create_product(data):
    new_product = Product(
        product_name = data['product_name'],
        product_description = data.get('product_description'),
        part_number = data.get('part_number'),
        barcode = data.get('barcode'),
        buying_price = data['buying_price'],
        wholesale_price = data['wholesale_price'],
        retail_price = data['retail_price'],
        product_type = data['product_type'],
        product_category_id = data['product_category_id'],
        product_sub_category_id = data.get('product_sub_category_id'),
        shop_id = data['shop_id'],
        store_id = data['store_id'],
        shelf_id = data.get('shelf_id'),
        package_mode_id = data.get('package_mode_id'),
        shelf_names = data.get('shelf_names'),
        shop_quantity = data.get('shop_quantity', 0),
        store_quantity = data.get('store_quantity', 0),
        component = data.get('component', False),
        hot_list = data.get('hot_list', False),
        dormant = data.get('dormant', False),
        apply_vat = data.get('apply_vat', False)
    )

    db.session.add(new_product)
    db.session.commit()
    return new_product

# Get all products
def get_all_products():
    return Product.query.all()

# Get product by ID
def get_product_by_id(product_id):
    return Product.query.get(product_id)

def get_product_by_name(name):
    return Product.query.filter_by(product_name=name).first()

# Update product by ID
def update_product(product_id, data):
    product = Product.query.get(product_id)
    if not product:
        return None

    product.product_name = data['product_name']
    product.product_description = data.get('product_description')
    product.part_number = data.get('part_number')
    product.barcode = data.get('barcode')
    product.buying_price = data['buying_price']
    product.wholesale_price = data['wholesale_price']
    product.retail_price = data['retail_price']
    product.product_type = data['product_type']
    product.product_category_id = data['product_category_id']
    product.product_sub_category_id = data.get('product_sub_category_id')
    product.shop_id = data['shop_id']
    product.store_id = data['store_id']
    product.shelf_id = data.get('shelf_id')
    product.package_mode_id = data.get('package_mode_id')
    product.shelf_names = data.get('shelf_names')
    product.shop_quantity = data.get('shop_quantity', 0)
    product.store_quantity = data.get('store_quantity', 0)
    product.component = data.get('component', False)
    product.hot_list = data.get('hot_list', False)
    product.dormant = data.get('dormant', False)
    product.apply_vat = data.get('apply_vat', False)

    db.session.commit()
    return product

# Delete product by ID
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None

    db.session.delete(product)
    db.session.commit()
    return product
