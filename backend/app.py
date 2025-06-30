from flask import Flask
from config import Config
from extensions import db, migrate, bcrypt, jwt, ma, cors

#Models
from models.user import User
from models.Supplier import Supplier, Invoice, Payment, SupplierPosting
from models.Stock import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    #setup API
    from flask_restful import Api
    api = Api(app)

    #supplier resources
    from resource.Supplier.supplier import SupplierListResource, SupplierResource, SupplierRecentResource
    from resource.Supplier.invoice import InvoiceListResource, InvoiceResource
    from resource.Supplier.payment import PaymentListResource, PaymentResource
    from resource.Supplier.supplier_posting import SupplierPostingListResource, SupplierPostingResource
    from resource.Supplier.analytics import SupplierDashboardOverviewResource, RecentOrdersResource, SupplierPaymentSummaryResource

    #---------------------------------------Supplier-----------------------------------------------------#
    #supplier endpoints
    api.add_resource(SupplierListResource, '/suppliers')
    api.add_resource(SupplierResource, '/suppliers/<int:supplier_id>')
    api.add_resource(SupplierRecentResource, '/suppliers/recent')

    #invoice endpoints
    api.add_resource(InvoiceListResource, '/invoices')
    api.add_resource(InvoiceResource, '/invoices/<int:invoice_id>')

    #payment endpoints
    api.add_resource(PaymentListResource, '/payments')
    api.add_resource(PaymentResource, '/payments/<int:payment_id>')

    #supplier Posting endpoints
    api.add_resource(SupplierPostingListResource, '/supplier_postings')
    api.add_resource(SupplierPostingResource, '/supplier_postings/<int:posting_id>')

    #supplier analytics
    api.add_resource(SupplierDashboardOverviewResource, '/suppliers/overview')
    api.add_resource(RecentOrdersResource, '/suppliers/recent_orders')
    api.add_resource(SupplierPaymentSummaryResource, '/suppliers/payment_summary')



    @app.route('/')
    def home():
        return "Hey Bizpro"

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
