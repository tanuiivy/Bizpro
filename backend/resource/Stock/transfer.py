from flask_restful import Resource
from flask import request
from schema.Stock import ProductTransferSchema
from service.Stock.transfer import (
    create_transfer,
    get_all_transfers,
    get_transfer_by_id,
    get_transfers_by_product_id,
    update_transfer,
    delete_transfer,
)

# schema instance
transfer_schema = ProductTransferSchema()
transfers_schema = ProductTransferSchema(many=True)

#create a transfer and get all
class TransferListResource(Resource):
    def post(self):
        data = request.get_json()

        product_id = data.get("product_id")
        transfer_quantity = data.get("transfer_quantity")
        from_location = data.get("from_location")
        to_location = data.get("to_location")
        status = data.get("status", "pending")
        remarks = data.get("remarks")

        transfer = create_transfer(product_id, transfer_quantity, from_location, to_location, status, remarks)
        if not transfer:
            return {"message": "Product not found"}, 404

        return transfer_schema.dump(transfer), 201

    def get(self):
        transfers = get_all_transfers()
        return transfers_schema.dump(transfers), 200

# get a single transfer
class TransferResource(Resource):
    def get(self, transfer_id):
        transfer = get_transfer_by_id(transfer_id)
        if not transfer:
            return {"message": "Transfer not found"}, 404
        return transfer_schema.dump(transfer), 200

    def put(self, transfer_id):
        data = request.get_json()

        transfer_quantity = data.get("transfer_quantity")
        from_location = data.get("from_location")
        to_location = data.get("to_location")
        status = data.get("status")
        remarks = data.get("remarks")

        transfer = update_transfer(transfer_id, transfer_quantity, from_location, to_location, status, remarks)
        if not transfer:
            return {"message": "Transfer not found"}, 404

        return transfer_schema.dump(transfer), 200

    def delete(self, transfer_id):
        success = delete_transfer(transfer_id)
        if not success:
            return {"message": "Transfer not found"}, 404
        return {"message": "Transfer deleted successfully"}, 200

# transfer by product
class TransfersByProductResource(Resource):
    def get(self, product_id):
        transfers = get_transfers_by_product_id(product_id)
        return transfers_schema.dump(transfers), 200

#get transfer by status
class TransfersByStatusResource(Resource):
    def get(self, status):
        transfers = get_transfers_by_status(status)
        if not transfers:
            return {"message": "No transfers found with this status"}, 404
        return transfers_schema.dump(transfers), 200

