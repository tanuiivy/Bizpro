from flask_restful import Resource
from flask import request
from schema.Stock import (
    ProductCategorySchema,
    ProductSubCategorySchema,
    ShopSchema,
    StoreSchema,
    ShelfSchema,
    PackageModeSchema
)
from service.Stock.reference import (
    create_category, get_category_by_product_id, update_category_by_product_id, remove_category_from_product,
    create_sub_category, get_sub_category_by_product_id, update_sub_category_by_product_id, remove_sub_category_from_product,
    create_shop, get_shop_by_product_id, update_shop_by_product_id, remove_shop_from_product,
    create_store, get_store_by_product_id, update_store_by_product_id, remove_store_from_product,
    create_shelf, get_shelf_by_product_id, update_shelf_by_product_id, remove_shelf_from_product,
    create_package_mode, get_package_mode_by_product_id, update_package_mode_by_product_id, remove_package_mode_from_product
)
#schema instance
category_schema = ProductCategorySchema()
subcategory_schema = ProductSubCategorySchema()
shop_schema = ShopSchema()
store_schema = StoreSchema()
shelf_schema = ShelfSchema()
package_mode_schema = PackageModeSchema()


# ===============Category=============#
class CategoryListResource(Resource):
    def post(self):
        data = request.get_json()
        name = data.get("product_category")
        if not name:
            return {"message": "Category name is required"}, 400
        category = create_category(name)
        return category_schema.dump(category), 201

class CategoryByProductResource(Resource):
    def get(self, product_id):
        category = get_category_by_product_id(product_id)
        if not category:
            return {"message": "Product or category not found"}, 404
        return category_schema.dump(category), 200

    def put(self, product_id):
        data = request.get_json()
        category_id = data.get("category_id")
        if not category_id:
            return {"message": "Category ID is required"}, 400
        updated_category = update_category_by_product_id(product_id, category_id)
        if not updated_category:
            return {"message": "Product or category not found"}, 404
        return category_schema.dump(updated_category), 200

    def delete(self, product_id):
        product = remove_category_from_product(product_id)
        if not product:
            return {"message": "Product not found"}, 404
        return {"message": "Category removed from product"}, 200

# ===============SubCategory=============#
class SubCategoryListResource(Resource):
    def post(self):
        data = request.get_json()
        name = data.get("product_sub_category")
        if not name:
            return {"message": "Sub-category name is required"}, 400
        sub_category = create_sub_category(name)
        return subcategory_schema.dump(sub_category), 201

class SubCategoryByProductResource(Resource):
    def get(self, product_id):
        sub_category = get_sub_category_by_product_id(product_id)
        if not sub_category:
            return {"message": "Product or sub-category not found"}, 404
        return subcategory_schema.dump(sub_category), 200

    def put(self, product_id):
        data = request.get_json()
        sub_category_id = data.get("sub_category_id")
        if not sub_category_id:
            return {"message": "Sub-category ID is required"}, 400
        updated = update_sub_category_by_product_id(product_id, sub_category_id)
        if not updated:
            return {"message": "Product or sub-category not found"}, 404
        return subcategory_schema.dump(updated), 200

    def delete(self, product_id):
        product = remove_sub_category_from_product(product_id)
        if not product:
            return {"message": "Product not found"}, 404
        return {"message": "Sub-category removed from product"}, 200

# ===============Shop=============#
class ShopListResource(Resource):
    def post(self):
        data = request.get_json()
        name = data.get("shop_name")
        company_id = data.get("company_id")
        if not name:
            return {"message": "Shop name is required"}, 400
        shop = create_shop(name, company_id)
        return shop_schema.dump(shop), 201

class ShopByProductResource(Resource):
    def get(self, product_id):
        shop = get_shop_by_product_id(product_id)
        if not shop:
            return {"message": "Product or shop not found"}, 404
        return shop_schema.dump(shop), 200

    def put(self, product_id):
        data = request.get_json()
        shop_id = data.get("shop_id")
        if not shop_id:
            return {"message": "Shop ID is required"}, 400
        updated = update_shop_by_product_id(product_id, shop_id)
        if not updated:
            return {"message": "Product or shop not found"}, 404
        return shop_schema.dump(updated), 200

    def delete(self, product_id):
        product = remove_shop_from_product(product_id)
        if not product:
            return {"message": "Product not found"}, 404
        return {"message": "Shop removed from product"}, 200

# ===============Store===============#
class StoreListResource(Resource):
    def post(self):
        data = request.get_json()
        name = data.get("store_name")
        company_id = data.get("company_id")
        if not name or not company_id:
            return {"message": "Store name and company ID are required"}, 400
        store = create_store(name, company_id)
        return store_schema.dump(store), 201

class StoreByProductResource(Resource):
    def get(self, product_id):
        store = get_store_by_product_id(product_id)
        if not store:
            return {"message": "Product or store not found"}, 404
        return store_schema.dump(store), 200

    def put(self, product_id):
        data = request.get_json()
        store_id = data.get("store_id")
        if not store_id:
            return {"message": "Store ID is required"}, 400
        updated = update_store_by_product_id(product_id, store_id)
        if not updated:
            return {"message": "Product or store not found"}, 404
        return store_schema.dump(updated), 200

    def delete(self, product_id):
        product = remove_store_from_product(product_id)
        if not product:
            return {"message": "Product not found"}, 404
        return {"message": "Store removed from product"}, 200

# ===============Store=============#
class ShelfListResource(Resource):
    def post(self):
        data = request.get_json()
        name = data.get("shelf_name")
        store_id = data.get("store_id")
        if not name or not store_id:
            return {"message": "Shelf name and store ID are required"}, 400
        shelf = create_shelf(name, store_id)
        return shelf_schema.dump(shelf), 201

class ShelfByProductResource(Resource):
    def get(self, product_id):
        shelf = get_shelf_by_product_id(product_id)
        if not shelf:
            return {"message": "Product or shelf not found"}, 404
        return shelf_schema.dump(shelf), 200

    def put(self, product_id):
        data = request.get_json()
        shelf_id = data.get("shelf_id")
        if not shelf_id:
            return {"message": "Shelf ID is required"}, 400
        updated = update_shelf_by_product_id(product_id, shelf_id)
        if not updated:
            return {"message": "Product or shelf not found"}, 404
        return shelf_schema.dump(updated), 200

    def delete(self, product_id):
        product = remove_shelf_from_product(product_id)
        if not product:
            return {"message": "Product not found"}, 404
        return {"message": "Shelf removed from product"}, 200

# ===============Package Mode=============#
class PackageModeListResource(Resource):
    def post(self):
        data = request.get_json()
        name = data.get("package_mode")
        if not name:
            return {"message": "Package mode name is required"}, 400
        mode = create_package_mode(name)
        return package_mode_schema.dump(mode), 201

class PackageModeByProductResource(Resource):
    def get(self, product_id):
        mode = get_package_mode_by_product_id(product_id)
        if not mode:
            return {"message": "Product or package mode not found"}, 404
        return package_mode_schema.dump(mode), 200

    def put(self, product_id):
        data = request.get_json()
        package_mode_id = data.get("package_mode_id")
        if not package_mode_id:
            return {"message": "Package mode ID is required"}, 400
        updated = update_package_mode_by_product_id(product_id, package_mode_id)
        if not updated:
            return {"message": "Product or package mode not found"}, 404
        return package_mode_schema.dump(updated), 200

    def delete(self, product_id):
        product = remove_package_mode_from_product(product_id)
        if not product:
            return {"message": "Product not found"}, 404
        return {"message": "Package mode removed from product"}, 200
