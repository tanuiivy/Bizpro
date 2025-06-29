from flask import request
from flask_restful import Resource
from schema.Supplier.supplier import SupplierSchema
from service.Supplier.supplier import (
    create_supplier,
    get_all_suppliers,
    get_supplier_by_id,
    update_supplier,
    delete_supplier,
    get_suppliers_by_invoice_status,
    get_most_recent_supplier
)
#schema instance
supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many=True)

#supplier list
class SupplierListResource(Resource):
    def post(self):
        json_data = request.get_json()
        data = supplier_schema.load(json_data)
        new_supplier = create_supplier(data)
        return supplier_schema.dump(new_supplier), 201

    def get(self):
        status = request.args.get('status')
        if status:
            suppliers = get_suppliers_by_invoice_status(status)
        else:
            suppliers = get_all_suppliers()
        return suppliers_schema.dump(suppliers), 200

#supplier by ID
class SupplierResource(Resource):
    def put(self, supplier_id):
        supplier = get_supplier_by_id(supplier_id)
        json_data = request.get_json()
        data = supplier_schema.load(json_data, partial=True)
        updated_supplier = update_supplier(supplier, data)
        return supplier_schema.dump(updated_supplier), 200

    def get(self, supplier_id):
        supplier = get_supplier_by_id(supplier_id)
        return supplier_schema.dump(supplier), 200

    def delete(self, supplier_id):
        supplier = get_supplier_by_id(supplier_id)
        delete_supplier(supplier)
        return '', 204

#most recent supplier
class SupplierRecentResource(Resource):
    def get(self):
        supplier = get_most_recent_supplier()
        if not supplier:
            return {"message": "No suppliers found"}, 404
        return supplier_schema.dump(supplier), 200
