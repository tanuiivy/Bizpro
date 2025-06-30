from extensions import ma
from marshmallow import fields
from models.Supplier import Supplier, Invoice, Payment, SupplierPosting
#Supplier
class SupplierSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Supplier
        load_instance = False

    supplier_id = ma.auto_field()
    image_path = ma.auto_field()
    supplier_name = ma.auto_field()
    supplier_email = ma.auto_field()
    supplier_phone = ma.auto_field()
    supplier_address = ma.auto_field()
    supplier_balance = ma.auto_field()
    contact_person = ma.auto_field()
    contact_person_no = ma.auto_field()
    package_mode = ma.auto_field()
    vat = ma.auto_field()
    stock = ma.auto_field()
    utility = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = fields.DateTime(dump_only=True)

#Invoice
class InvoiceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Invoice
        load_instance = False

    invoice_id = ma.auto_field()
    supplier_id = ma.auto_field()
    invoice_number = ma.auto_field()
    amount = ma.auto_field()
    issue_date = ma.auto_field()
    due_date = ma.auto_field()
    status = ma.auto_field()

#Payment
class PaymentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Payment
        load_instance = False

    id = ma.auto_field()
    supplier_id = ma.auto_field()
    amount = ma.auto_field()
    payment_date = ma.auto_field()
    method = ma.auto_field()
    reference = ma.auto_field()

#SupplierPosting
class SupplierPostingSchema(ma.SQLAlchemySchema):
    class Meta:
        model = SupplierPosting
        load_instance = False

    posting_id = ma.auto_field()
    supplier_id = ma.auto_field()
    amount = ma.auto_field()
    description = ma.auto_field()
    posting_date = ma.auto_field()
