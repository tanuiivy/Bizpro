from flask_restful import Resource
from service.Stock.analytics import (
    get_total_companies,
    get_total_products,
    get_total_transfers,
    get_pending_transfers,
    get_total_write_offs,
    get_customers_per_company,
    get_customers_per_product
)

class TotalCompaniesResource(Resource):
    def get(self):
        return {"total_companies": get_total_companies()}, 200

class TotalProductsResource(Resource):
    def get(self):
        return {"total_products": get_total_products()}, 200

class TotalTransfersResource(Resource):
    def get(self):
        return {"total_transfers": get_total_transfers()}, 200

class PendingTransfersResource(Resource):
    def get(self):
        return {"pending_transfers": get_pending_transfers()}, 200

class TotalWriteOffsResource(Resource):
    def get(self):
        return {"total_write_offs": get_total_write_offs()}, 200

class CustomersPerCompanyResource(Resource):
    def get(self):
        data = get_customers_per_company()
        return {"customers_per_company": data}, 200

class CustomersPerProductResource(Resource):
    def get(self):
        data = get_customers_per_product()
        return {"customers_per_product": data}, 200
