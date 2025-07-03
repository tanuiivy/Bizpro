from extensions import ma
from models.Customer import Customer, CustomerPosting, PaymentForm

# customer
class CustomerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Customer
        load_instance = True

    customer_id = ma.auto_field()
    company_id = ma.auto_field()
    fullname = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    purchase_type = ma.auto_field()
    payment_method = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()

# customer posting 
class CustomerPostingSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CustomerPosting
        load_instance = True

    customer_postings_id = ma.auto_field()
    customer_id = ma.auto_field()
    product_id = ma.auto_field()
    company_id = ma.auto_field()
    purchase_type = ma.auto_field()
    amount = ma.auto_field()
    description = ma.auto_field()
    status = ma.auto_field()
    payment_date = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()

# payment form
class PaymentFormSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PaymentForm
        load_instance = True

    payment_id = ma.auto_field()
    customer_id = ma.auto_field()
    posting_id = ma.auto_field()
    product_id = ma.auto_field()
    company_id = ma.auto_field()
    amount_paid = ma.auto_field()
    payment_method = ma.auto_field()
    payment_date = ma.auto_field()
    notes = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()
