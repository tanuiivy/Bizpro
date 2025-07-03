from flask_restful import Resource
from flask import request
from schema.Stock import CompanySchema
from service.Stock.company import (
    create_company,
    get_all_companies,
    get_company_by_id,
    get_company_by_name,
    update_company,
    delete_company,
)
#schema instance
company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)

#create company and get all
class CompanyListResource(Resource):
    def post(self):
        data = request.get_json()
        company = create_company(data)
        return company_schema.dump(company), 201

    def get(self):
        companies = get_all_companies()
        return companies_schema.dump(companies), 200

#single company
class CompanyResource(Resource):
    def get(self, company_id):
        company = get_company_by_id(company_id)
        if not company:
            return {"message": "Company not found"}, 404
        return company_schema.dump(company), 200

    def put(self, company_id):
        data = request.get_json()
        company = update_company(company_id, data)
        if not company:
            return {"message": "Company not found"}, 404
        return company_schema.dump(company), 200

    def delete(self, company_id):
        company = delete_company(company_id)
        if not company:
            return {"message": "Company not found"}, 404
        return {"message": "Company deleted successfully"}, 200

#company by name
class CompanyByNameResource(Resource):
    def get(self, name):
        company = get_company_by_name(name)
        if not company:
            return {"message": "Company not found"}, 404
        return company_schema.dump(company), 200
