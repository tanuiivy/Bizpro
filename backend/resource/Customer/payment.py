from flask_restful import Resource
from flask import request
from schema.Customer import PaymentFormSchema
from service.Customer.payment import (
    create_payment,
    get_all_payments,
    get_payment_by_id,
    get_payments_by_customer,
    get_payments_by_company,
    update_payment,
    delete_payment
)

# Schema
payment_schema = PaymentFormSchema()
payments_schema = PaymentFormSchema(many=True)

class CustomerPaymentListResource(Resource):
    def post(self):
        data = request.get_json()
        payment = create_payment(
            customer_id=data.get("customer_id"),
            posting_id=data.get("posting_id"),
            product_id=data.get("product_id"),
            company_id=data.get("company_id"),
            amount_paid=data.get("amount_paid"),
            payment_method=data.get("payment_method"),
            payment_date=data.get("payment_date"),
            notes=data.get("notes")
        )
        return payment_schema.dump(payment), 201

    def get(self):
        payments = get_all_payments()
        return payments_schema.dump(payments), 200

class CustomerPaymentResource(Resource):
    def get(self, payment_id):
        payment = get_payment_by_id(payment_id)
        if not payment:
            return {"message": "Payment not found"}, 404
        return payment_schema.dump(payment), 200

    def put(self, payment_id):
        data = request.get_json()
        payment = update_payment(
            payment_id,
            amount_paid=data.get("amount_paid"),
            payment_method=data.get("payment_method"),
            payment_date=data.get("payment_date"),
            notes=data.get("notes")
        )
        if not payment:
            return {"message": "Payment not found"}, 404
        return payment_schema.dump(payment), 200

    def delete(self, payment_id):
        success = delete_payment(payment_id)
        if not success:
            return {"message": "Payment not found"}, 404
        return {"message": "Payment deleted successfully"}, 200

class PaymentsByCustomerResource(Resource):
    def get(self, customer_id):
        payments = get_payments_by_customer(customer_id)
        return payments_schema.dump(payments), 200

class PaymentsByCompanyResource(Resource):
    def get(self, company_id):
        payments = get_payments_by_company(company_id)
        return payments_schema.dump(payments), 200
