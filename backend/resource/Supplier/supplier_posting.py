from flask import request
from flask_restful import Resource
from schema.Supplier.supplier import SupplierPostingSchema

from service.Supplier.supplier_posting import (
    create_supplier_posting,
    get_all_supplier_postings,
    get_supplier_posting_by_id,
    get_postings_by_supplier,
    update_supplier_posting,
    delete_supplier_posting,
)
#schema instance
posting_schema = SupplierPostingSchema()
postings_schema = SupplierPostingSchema(many=True)

#posting list
class SupplierPostingListResource(Resource):
    def post(self):
        json_data = request.get_json()
        data = posting_schema.load(json_data)
        new_posting = create_supplier_posting(data)
        return posting_schema.dump(new_posting), 201

    def get(self):
        supplier_id = request.args.get('supplier_id')
        if supplier_id:
            postings = get_postings_by_supplier(supplier_id)
        else:
            postings = get_all_supplier_postings()
        return postings_schema.dump(postings), 200
#posting by ID
class SupplierPostingResource(Resource):
    def get(self, posting_id):
        posting = get_supplier_posting_by_id(posting_id)
        return posting_schema.dump(posting), 200

    def put(self, posting_id):
        posting = get_supplier_posting_by_id(posting_id)
        json_data = request.get_json()
        data = posting_schema.load(json_data, partial=True)
        updated_posting = update_supplier_posting(posting, data)
        return posting_schema.dump(updated_posting), 200

    def delete(self, posting_id):
        posting = get_supplier_posting_by_id(posting_id)
        delete_supplier_posting(posting)
        return '', 204
