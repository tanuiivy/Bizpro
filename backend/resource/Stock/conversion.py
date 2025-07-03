from flask_restful import Resource
from flask import request
from schema.Stock import ProductConversionSchema
from service.Stock.conversion import (
    create_conversion,
    get_all_conversions,
    get_conversion_by_id,
    update_conversion,
    delete_conversion,
)
#schema instance
conversion_schema = ProductConversionSchema()
conversions_schema = ProductConversionSchema(many=True)

#create conversion and get all
class ConversionListResource(Resource):
    def post(self):
        data = request.get_json()
        conversion = create_conversion(data)
        return conversion_schema.dump(conversion), 201

    def get(self):
        conversions = get_all_conversions()
        return conversions_schema.dump(conversions), 200

#single conversion
class ConversionResource(Resource):
    def get(self, conversion_id):
        conversion = get_conversion_by_id(conversion_id)
        if not conversion:
            return {"message": "Conversion not found"}, 404
        return conversion_schema.dump(conversion), 200

    def put(self, conversion_id):
        data = request.get_json()
        conversion = update_conversion(conversion_id, data)
        if not conversion:
            return {"message": "Conversion not found"}, 404
        return conversion_schema.dump(conversion), 200

    def delete(self, conversion_id):
        conversion = delete_conversion(conversion_id)
        if not conversion:
            return {"message": "Conversion not found"}, 404
        return {"message": "Conversion deleted successfully"}, 200
