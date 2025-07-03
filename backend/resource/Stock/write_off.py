from flask_restful import Resource
from flask import request
from schema.Stock import WriteOffSchema
from service.Stock.write_off import (
    create_write_off,
    get_all_write_offs,
    get_write_off_by_id,
    get_write_offs_by_product_id,
    update_write_off,
    delete_write_off,
)

# schema instance
write_off_schema = WriteOffSchema()
write_offs_schema = WriteOffSchema(many=True)

# create a writeoff and get all
class WriteOffListResource(Resource):
    def post(self):
        data = request.get_json()

        product_id = data.get("product_id")
        write_off_quantity = data.get("write_off_quantity")
        buying_price = data.get("buying_price")
        expiry_date = data.get("expiry_date")
        remarks = data.get("remarks")

        write_off = create_write_off(product_id, write_off_quantity, buying_price, expiry_date, remarks)
        if not write_off:
            return {"message": "Product not found"}, 404

        return write_off_schema.dump(write_off), 201

    def get(self):
        write_offs = get_all_write_offs()
        return write_offs_schema.dump(write_offs), 200

# get a single write off
class WriteOffResource(Resource):
    def get(self, write_off_id):
        write_off = get_write_off_by_id(write_off_id)
        if not write_off:
            return {"message": "Write-off not found"}, 404
        return write_off_schema.dump(write_off), 200

    def put(self, write_off_id):
        data = request.get_json()

        write_off_quantity = data.get("write_off_quantity")
        buying_price = data.get("buying_price")
        expiry_date = data.get("expiry_date")
        remarks = data.get("remarks")

        write_off = update_write_off(write_off_id, write_off_quantity, buying_price, expiry_date, remarks)
        if not write_off:
            return {"message": "Write-off not found"}, 404

        return write_off_schema.dump(write_off), 200

    def delete(self, write_off_id):
        success = delete_write_off(write_off_id)
        if not success:
            return {"message": "Write-off not found"}, 404
        return {"message": "Write-off deleted successfully"}, 200

# get all writeoffs for a product
class WriteOffsByProductResource(Resource):
    def get(self, product_id):
        write_offs = get_write_offs_by_product_id(product_id)
        return write_offs_schema.dump(write_offs), 200
