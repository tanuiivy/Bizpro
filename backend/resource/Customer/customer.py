from flask_restful import Resource
from flask import request
from schema.Customer import CustomerSchema
from service.Customer.customer import (
    create_customer,
    get_all_customers,
    get_customer_by_id,
    get_customers_by_company,
    get_customers_by_payment_method,
    get_customers_by_purchase_type,
    update_customer,
    delete_customer
)

# Initialize schemas
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

#create and get all customers
class CustomerListResource(Resource):
    def post(self):
        data = request.get_json()

        company_id = data.get("company_id")
        fullname = data.get("fullname")
        email = data.get("email")
        phone = data.get("phone")
        purchase_type = data.get("purchase_type", "retail")
        payment_method = data.get("payment_method", "cash")

        new_customer = create_customer(
            company_id,
            fullname,
            email,
            phone,
            purchase_type,
            payment_method
        )

        return customer_schema.dump(new_customer), 201

    def get(self):
        customers = get_all_customers()
        return customers_schema.dump(customers), 200

# get, update, and delete individual customer
class CustomerResource(Resource):
    def get(self, customer_id):
        customer = get_customer_by_id(customer_id)
        if not customer:
            return {"message": "Customer not found"}, 404
        return customer_schema.dump(customer), 200

    def put(self, customer_id):
        data = request.get_json()

        fullname = data.get("fullname")
        email = data.get("email")
        phone = data.get("phone")
        purchase_type = data.get("purchase_type")
        payment_method = data.get("payment_method")

        updated_customer = update_customer(
            customer_id,
            fullname,
            email,
            phone,
            purchase_type,
            payment_method
        )

        if not updated_customer:
            return {"message": "Customer not found"}, 404

        return customer_schema.dump(updated_customer), 200

    def delete(self, customer_id):
        success = delete_customer(customer_id)
        if not success:
            return {"message": "Customer not found"}, 404
        return {"message": "Customer deleted successfully"}, 200

# get customers by company
class CustomersByCompanyResource(Resource):
    def get(self, company_id):
        customers = get_customers_by_company(company_id)
        return customers_schema.dump(customers), 200

# get customers by payment method
class CustomersByPaymentMethodResource(Resource):
    def get(self, payment_method):
        customers = get_customers_by_payment_method(payment_method)
        return customers_schema.dump(customers), 200

# get customers by purchase type
class CustomersByPurchaseTypeResource(Resource):
    def get(self, purchase_type):
        customers = get_customers_by_purchase_type(purchase_type)
        return customers_schema.dump(customers), 200
