from flask import request
from flask_restful import Resource
from schema.Supplier.supplier import PaymentSchema
from service.Supplier.payment import (
    create_payment,
    get_all_payments,
    get_payment_by_id,
    get_payments_by_supplier,
    update_payment,
    delete_payment,
)
#schema instance
payment_schema = PaymentSchema()
payments_schema = PaymentSchema(many=True)

#payment list
class PaymentListResource(Resource):
    def post(self):
        json_data = request.get_json()
        data = payment_schema.load(json_data)
        new_payment = create_payment(data)
        return payment_schema.dump(new_payment), 201

    def get(self):
        supplier_id = request.args.get('supplier_id')
        if supplier_id:
            payments = get_payments_by_supplier(supplier_id)
        else:
            payments = get_all_payments()
        return payments_schema.dump(payments), 200
#payment by ID
class PaymentResource(Resource):
    def get(self, payment_id):
        payment = get_payment_by_id(payment_id)
        return payment_schema.dump(payment), 200

    def put(self, payment_id):
        payment = get_payment_by_id(payment_id)
        json_data = request.get_json()
        data = payment_schema.load(json_data, partial=True)
        updated_payment = update_payment(payment, data)
        return payment_schema.dump(updated_payment), 200

    def delete(self, payment_id):
        payment = get_payment_by_id(payment_id)
        delete_payment(payment)
        return '', 204
