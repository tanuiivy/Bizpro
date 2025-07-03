from flask_restful import Resource
from service.Customer.analytics import (
    get_total_customer_revenue,
    get_pending_payments,
    get_total_postings,
    get_total_customers,
    get_top_company_per_customer,
    get_top_product_per_customer,
)

class TotalCustomerRevenueResource(Resource):
    def get(self):
        return {"total_customer_revenue": get_total_customer_revenue()}, 200

class PendingPaymentsResource(Resource):
    def get(self):
        return {"pending_payments": get_pending_payments()}, 200

class TotalPostingsResource(Resource):
    def get(self):
        return {"total_postings": get_total_postings()}, 200

class TotalCustomersResource(Resource):
    def get(self):
        return {"total_customers": get_total_customers()}, 200

class TopCompanyPerCustomerResource(Resource):
    def get(self):
        return {"data": get_top_company_per_customer()}, 200

class TopProductPerCustomerResource(Resource):
    def get(self):
        return {"data": get_top_product_per_customer()}, 200
