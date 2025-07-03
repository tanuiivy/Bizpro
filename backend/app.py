from flask import Flask
from config import Config
from extensions import db, migrate, bcrypt, jwt, ma, cors

#Models
from models.Supplier import *
from models.Stock import *
from models.Customer import *

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
    from resource.Supplier.payment import SupplierPaymentListResource, SupplierPaymentResource
    from resource.Supplier.supplier_posting import SupplierPostingListResource, SupplierPostingResource, SupplierPostingsByProductResource, SupplierPostingsByCompanyResource
    from resource.Supplier.analytics import SupplierDashboardOverviewResource, RecentOrdersResource, SupplierPaymentSummaryResource

    #stock resources
    from resource.Stock.company import CompanyListResource, CompanyResource, CompanyByNameResource
    from resource.Stock.conversion import ConversionListResource, ConversionResource
    from resource.Stock.product import ProductListResource, ProductResource, ProductByNameResource
    from resource.Stock.reference import CategoryListResource, CategoryByProductResource, SubCategoryListResource, SubCategoryByProductResource, ShopListResource, ShopByProductResource, StoreListResource, StoreByProductResource, ShelfListResource, ShelfByProductResource, PackageModeListResource, PackageModeByProductResource
    from resource.Stock.transfer import TransferListResource, TransferResource, TransfersByProductResource, TransfersByStatusResource
    from resource.Stock.write_off import WriteOffListResource, WriteOffResource, WriteOffsByProductResource
    from resource.Stock.analytics import TotalCompaniesResource, TotalProductsResource, TotalTransfersResource, PendingTransfersResource, TotalWriteOffsResource, CustomersPerCompanyResource, CustomersPerProductResource

    #customer resources
    from resource.Customer.customer import CustomerListResource, CustomerResource, CustomersByCompanyResource, CustomersByPaymentMethodResource, CustomersByPurchaseTypeResource
    from resource.Customer.customerposting import CustomerPostingListResource, CustomerPostingResource, CustomerPostingsByCustomerResource, CustomerPostingsByCompanyResource
    from resource.Customer.payment import CustomerPaymentListResource, CustomerPaymentResource, PaymentsByCustomerResource, PaymentsByCompanyResource
    from resource.Customer.analytics import TotalCustomerRevenueResource, PendingPaymentsResource, TotalPostingsResource, TotalCustomersResource, TopCompanyPerCustomerResource, TopProductPerCustomerResource

    #---------------------------------------Supplier-----------------------------------------------------#
    #supplier endpoints
    api.add_resource(SupplierListResource, '/suppliers')
    api.add_resource(SupplierResource, '/suppliers/<int:supplier_id>')
    api.add_resource(SupplierRecentResource, '/suppliers/recent')

    #invoice endpoints
    api.add_resource(InvoiceListResource, '/invoices')
    api.add_resource(InvoiceResource, '/invoices/<int:invoice_id>')

    #payment endpoints
    api.add_resource(SupplierPaymentListResource, '/payments')
    api.add_resource(SupplierPaymentResource, '/payments/<int:payment_id>')

    #supplier Posting endpoints
    api.add_resource(SupplierPostingListResource, '/supplier_postings')
    api.add_resource(SupplierPostingResource, '/supplier_postings/<int:posting_id>')
    api.add_resource(SupplierPostingsByProductResource, '/supplier_postings/product/<int:product_id>')
    api.add_resource(SupplierPostingsByCompanyResource, '/supplier_postings/company/<int:company_id>')

    #supplier analytics
    api.add_resource(SupplierDashboardOverviewResource, '/suppliers/overview')
    api.add_resource(RecentOrdersResource, '/suppliers/recent_orders')
    api.add_resource(SupplierPaymentSummaryResource, '/suppliers/payment_summary')

    #---------------------------------------Stock-----------------------------------------------------#
    #company endpoints
    api.add_resource(CompanyListResource, "/companies")
    api.add_resource(CompanyResource, "/companies/<int:company_id>")
    api.add_resource(CompanyByNameResource, "/companies/name/<string:name>")

    #conversion endpoints
    api.add_resource(ConversionListResource, "/conversions")
    api.add_resource(ConversionResource, "/conversions/<int:conversion_id>")

    #product endpoints
    api.add_resource(ProductListResource, "/products")
    api.add_resource(ProductResource, "/products/<int:product_id>")
    api.add_resource(ProductByNameResource, "/products/name/<string:name>")

    #product reference endpoints
    #category
    api.add_resource(CategoryListResource, "/categories")
    api.add_resource(CategoryByProductResource, "/categories/product/<int:product_id>")
    #subcategory
    api.add_resource(SubCategoryListResource, "/sub-categories")
    api.add_resource(SubCategoryByProductResource, "/sub-categories/product/<int:product_id>")
    #shop
    api.add_resource(ShopListResource, "/shops")
    api.add_resource(ShopByProductResource, "/shops/product/<int:product_id>")
    #store
    api.add_resource(StoreListResource, "/stores")
    api.add_resource(StoreByProductResource, "/stores/product/<int:product_id>")
    #shelf
    api.add_resource(ShelfListResource, "/shelves")
    api.add_resource(ShelfByProductResource, "/shelves/product/<int:product_id>")
    #package
    api.add_resource(PackageModeListResource, "/package-modes")
    api.add_resource(PackageModeByProductResource, "/package-modes/product/<int:product_id>")

    #transfer endpoints
    api.add_resource(TransferListResource, "/transfers")
    api.add_resource(TransferResource, "/transfers/<int:transfer_id>")
    api.add_resource(TransfersByProductResource, "/transfers/product/<int:product_id>")
    api.add_resource(TransfersByStatusResource, "/transfers/status/<string:status>")

    #writeoffs endpoints
    api.add_resource(WriteOffListResource, "/write-offs")
    api.add_resource(WriteOffResource, "/write-offs/<int:write_off_id>")
    api.add_resource(WriteOffsByProductResource, "/write-offs/product/<int:product_id>")

    #analytics endpoints
    api.add_resource(TotalCompaniesResource, "/analytics/total_companies")
    api.add_resource(TotalProductsResource, "/analytics/total_products")
    api.add_resource(TotalTransfersResource, "/analytics/total_transfers")
    api.add_resource(PendingTransfersResource, "/analytics/pending_transfers")
    api.add_resource(TotalWriteOffsResource, "/analytics/total_write_offs")
    api.add_resource(CustomersPerCompanyResource, "/analytics/customers_per_company")
    api.add_resource(CustomersPerProductResource, "/analytics/customers_per_product")


#---------------------------------------Stock-----------------------------------------------------#
    #customer endpoints
    api.add_resource(CustomerListResource, "/customers")
    api.add_resource(CustomerResource, "/customers/<int:customer_id>")
    api.add_resource(CustomersByCompanyResource, "/customers/company/<int:company_id>")
    api.add_resource(CustomersByPaymentMethodResource, "/customers/payment_method/<string:payment_method>")
    api.add_resource(CustomersByPurchaseTypeResource, "/customers/purchase_type/<string:purchase_type>")

    #customer posting endpoints
    api.add_resource(CustomerPostingListResource, "/customer_postings")
    api.add_resource(CustomerPostingResource, "/customer_postings/<int:posting_id>")
    api.add_resource(CustomerPostingsByCustomerResource, "/customer_postings/customer/<int:customer_id>")
    api.add_resource(CustomerPostingsByCompanyResource, "/customer_postings/company/<int:company_id>")

    #payment endpoints
    api.add_resource(CustomerPaymentListResource, "/payments")
    api.add_resource(CustomerPaymentResource, "/payments/<int:payment_id>")
    api.add_resource(PaymentsByCustomerResource, "/payments/customer/<int:customer_id>")
    api.add_resource(PaymentsByCompanyResource, "/payments/company/<int:company_id>")

    #customer analytics
    api.add_resource(TotalCustomerRevenueResource, "/customer-analytics/total-revenue")
    api.add_resource(PendingPaymentsResource, "/customer-analytics/pending-payments")
    api.add_resource(TotalPostingsResource, "/customer-analytics/total-postings")
    api.add_resource(TotalCustomersResource, "/customer-analytics/total-customers")
    api.add_resource(TopCompanyPerCustomerResource, "/customer-analytics/top-company")
    api.add_resource(TopProductPerCustomerResource, "/customer-analytics/top-product")

    @app.route('/')
    def home():
        return "Hey Bizpro"

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
