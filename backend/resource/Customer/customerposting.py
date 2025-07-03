from flask_restful import Resource
from flask import request
from schema.Customer import CustomerPostingSchema
from service.Customer.customerposting import (
    create_customer_posting,
    get_all_customer_postings,
    get_customer_posting_by_id,
    get_customer_postings_by_customer,
    get_customer_postings_by_company,
    update_customer_posting,
    delete_customer_posting
)

# Schema instances
posting_schema = CustomerPostingSchema()
postings_schema = CustomerPostingSchema(many=True)

# Create and get all postings
class CustomerPostingListResource(Resource):
    def post(self):
        data = request.get_json()

        customer_id = data.get("customer_id")
        product_id = data.get("product_id")
        company_id = data.get("company_id")
        purchase_type = data.get("purchase_type", "retail")
        amount = data.get("amount")
        description = data.get("description")
        status = data.get("status", "pending")
        payment_date = data.get("payment_date")

        posting = create_customer_posting(
            customer_id,
            product_id,
            company_id,
            purchase_type,
            amount,
            description,
            status,
            payment_date
        )

        return posting_schema.dump(posting), 201

    def get(self):
        postings = get_all_customer_postings()
        return postings_schema.dump(postings), 200

# Get, update, delete by ID
class CustomerPostingResource(Resource):
    def get(self, posting_id):
        posting = get_customer_posting_by_id(posting_id)
        if not posting:
            return {"message": "Posting not found"}, 404
        return posting_schema.dump(posting), 200

    def put(self, posting_id):
        data = request.get_json()

        purchase_type = data.get("purchase_type")
        amount = data.get("amount")
        description = data.get("description")
        status = data.get("status")
        payment_date = data.get("payment_date")

        updated = update_customer_posting(
            posting_id,
            purchase_type,
            amount,
            description,
            status,
            payment_date
        )
        if not updated:
            return {"message": "Posting not found"}, 404

        return posting_schema.dump(updated), 200

    def delete(self, posting_id):
        success = delete_customer_posting(posting_id)
        if not success:
            return {"message": "Posting not found"}, 404
        return {"message": "Posting deleted successfully"}, 200

# Get by customer
class CustomerPostingsByCustomerResource(Resource):
    def get(self, customer_id):
        postings = get_customer_postings_by_customer(customer_id)
        return postings_schema.dump(postings), 200

# Get by company
class CustomerPostingsByCompanyResource(Resource):
    def get(self, company_id):
        postings = get_customer_postings_by_company(company_id)
        return postings_schema.dump(postings), 200
