from models.Stock.company import Company
from extensions import db

def create_company(data):
    company = Company(
        company_name = data["company_name"],
        company_email = data["company_email"],
        company_phone = data["company_phone"],
        company_phone_2 = data.get("company_phone_2"),
        county = data["county"],
        sub_county = data["sub_county"],
        city = data["city"],
        company_address = data["company_address"],
        company_address_2 = data.get("company_address_2"),
        zip_code = data.get("zip_code"),
        product_category = data.get("product_category"),
        product_sub_category = data.get("product_sub_category"),
        vat = data.get("vat"),
    )
    db.session.add(company)
    db.session.commit()
    return company

def get_all_companies():
    return Company.query.all()

def get_company_by_id(company_id):
    return Company.query.get(company_id)

def get_company_by_name(name):
    return Company.query.filter_by(company_name=name).first()

def update_company(company_id, data):
    company = Company.query.get(company_id)
    if not company:
        return None
    for key, value in data.items():
        if hasattr(company, key):
            setattr(company, key, value)
    db.session.commit()
    return company

def delete_company(company_id):
    company = Company.query.get(company_id)
    if not company:
        return None
    db.session.delete(company)
    db.session.commit()
    return company
