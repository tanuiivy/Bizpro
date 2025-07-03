from flask_restful import Resource
from flask import request
from schema.Stock import ProductSchema
from service.Stock.product import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product,
)
#schema instance
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

#single product and get all
class ProductListResource(Resource):
    def post(self):
        data = request.get_json()
        product = create_product(data)
        return product_schema.dump(product), 201

    def get(self):
        products = get_all_products()
        return products_schema.dump(products), 200

#single product
class ProductResource(Resource):
    def get(self, product_id):
        product = get_product_by_id(product_id)
        if not product:
            return {"message": "Product not found"}, 404
        return product_schema.dump(product), 200

    def put(self, product_id):
        data = request.get_json()
        product = update_product(product_id, data)
        if not product:
            return {"message": "Product not found"}, 404
        return product_schema.dump(product), 200

    def delete(self, product_id):
        product = delete_product(product_id)
        if not product:
            return {"message": "Product not found"}, 404
        return {"message": "Product deleted successfully"}, 200

#company by name
class ProductByNameResource(Resource):
    def get(self, name):
        product = get_product_by_name(name)
        if not product:
            return {"message": "Product not found"}, 404
        return product_schema.dump(product), 200
