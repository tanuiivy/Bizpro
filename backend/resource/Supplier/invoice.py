from flask import request
from flask_restful import Resource
from schema.Supplier.supplier import InvoiceSchema
from service.Supplier.invoice import (
    create_invoice,
    get_all_invoices,
    get_invoice_by_id,
    get_invoices_by_supplier,
    update_invoice,
    delete_invoice,
)
#schema instance
invoice_schema = InvoiceSchema()
invoices_schema = InvoiceSchema(many=True)

#invoice list
class InvoiceListResource(Resource):
    def post(self):
        json_data = request.get_json()
        data = invoice_schema.load(json_data)
        new_invoice = create_invoice(data)
        return invoice_schema.dump(new_invoice), 201

    def get(self):
        supplier_id = request.args.get('supplier_id')
        if supplier_id:
            invoices = get_invoices_by_supplier(supplier_id)
        else:
            invoices = get_all_invoices()
        return invoices_schema.dump(invoices), 200

#invoice by ID
class InvoiceResource(Resource):
    def get(self, invoice_id):
        invoice = get_invoice_by_id(invoice_id)
        return invoice_schema.dump(invoice), 200

    def put(self, invoice_id):
        invoice = get_invoice_by_id(invoice_id)
        json_data = request.get_json()
        data = invoice_schema.load(json_data, partial=True)
        updated_invoice = update_invoice(invoice, data)
        return invoice_schema.dump(updated_invoice), 200

    def delete(self, invoice_id):
        invoice = get_invoice_by_id(invoice_id)
        delete_invoice(invoice)
        return '', 204
