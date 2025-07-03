from flask_restful import Resource
from service.Supplier.analytics import (
    get_total_companies,
    get_total_products,
    get_pending_transfers,
    get_total_write_offs
)

class TotalCompaniesResource(Resource):
    def get(self):
        return {"total_companies": get_total_companies()}, 200

class TotalProductsResource(Resource):
    def get(self):
        return {"total_products": get_total_products()}, 200

class PendingTransfersResource(Resource):
    def get(self):
        return {"pending_transfers": get_pending_transfers()}, 200

class TotalWriteOffsResource(Resource):
    def get(self):
        return {"total_write_offs": get_total_write_offs()}, 200
