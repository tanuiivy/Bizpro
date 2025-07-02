from models.Stock.product import Product
from models.Stock.reference import (
    ProductCategory, ProductSubCategory, Shop, Store, Shelf, PackageMode
)
from extensions import db

def create_package_mode(package_mode_name):
    new_mode = PackageMode(package_mode=package_mode_name)
    db.session.add(new_mode)
    db.session.commit()
    return new_mode

def get_package_mode_by_product_id(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    return product.package_mode

def update_package_mode_by_product_id(product_id, package_mode_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    package_mode = PackageMode.query.get(package_mode_id)
    if not package_mode:
        return None
    product.package_mode_id = package_mode_id
    db.session.commit()
    return product.package_mode

def remove_package_mode_from_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    product.package_mode_id = None
    db.session.commit()
    return product


def create_category(category_name):
    new_category = ProductCategory(product_category=category_name)
    db.session.add(new_category)
    db.session.commit()
    return new_category

def get_category_by_product_id(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    return product.product_category

def update_category_by_product_id(product_id, category_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    category = ProductCategory.query.get(category_id)
    if not category:
        return None
    product.product_category_id = category_id
    db.session.commit()
    return product.product_category

def remove_category_from_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    product.product_category_id = None
    db.session.commit()
    return product


def create_sub_category(sub_category_name):
    new_sub = ProductSubCategory(product_sub_category=sub_category_name)
    db.session.add(new_sub)
    db.session.commit()
    return new_sub

def get_sub_category_by_product_id(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    return product.product_sub_category

def update_sub_category_by_product_id(product_id, sub_category_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    sub_category = ProductSubCategory.query.get(sub_category_id)
    if not sub_category:
        return None
    product.product_sub_category_id = sub_category_id
    db.session.commit()
    return product.product_sub_category

def remove_sub_category_from_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    product.product_sub_category_id = None
    db.session.commit()
    return product


def create_shop(shop_name, company_id=None):
    new_shop = Shop(shop_name=shop_name, company_id=company_id)
    db.session.add(new_shop)
    db.session.commit()
    return new_shop

def get_shop_by_product_id(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    return product.shop

def update_shop_by_product_id(product_id, shop_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    shop = Shop.query.get(shop_id)
    if not shop:
        return None
    product.shop_id = shop_id
    db.session.commit()
    return product.shop

def remove_shop_from_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    product.shop_id = None
    db.session.commit()
    return product


def create_store(store_name, company_id):
    new_store = Store(store_name=store_name, company_id=company_id)
    db.session.add(new_store)
    db.session.commit()
    return new_store

def get_store_by_product_id(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    return product.store

def update_store_by_product_id(product_id, store_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    store = Store.query.get(store_id)
    if not store:
        return None
    product.store_id = store_id
    db.session.commit()
    return product.store

def remove_store_from_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    product.store_id = None
    db.session.commit()
    return product

# ====================================================
# 🔹 SHELF
# ====================================================

def create_shelf(shelf_name, store_id):
    new_shelf = Shelf(shelf_name=shelf_name, store_id=store_id)
    db.session.add(new_shelf)
    db.session.commit()
    return new_shelf

def get_shelf_by_product_id(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    return product.shelf

def update_shelf_by_product_id(product_id, shelf_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    shelf = Shelf.query.get(shelf_id)
    if not shelf:
        return None
    product.shelf_id = shelf_id
    db.session.commit()
    return product.shelf

def remove_shelf_from_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return None
    product.shelf_id = None
    db.session.commit()
    return product
