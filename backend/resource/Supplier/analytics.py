from flask_restful import Resource
from service.Supplier.analytics import (
    get_total_payments,
    get_pending_orders_count,
    get_completed_orders_count,
    get_total_order_value,
    get_recent_orders,
    get_supplier_payment_summary,
)
from schema.Supplier.supplier import InvoiceSchema
#schema instance
invoice_schema = InvoiceSchema(many=True)

class SupplierDashboardOverviewResource(Resource):
    def get(self):
        data = {
            "total_payments": get_total_payments()["total_payments"],
            "pending_orders": get_pending_orders_count()["pending_orders"],
            "completed_orders": get_completed_orders_count()["completed_orders"],
            "total_order_value": get_total_order_value()["total_order_value"],
        }
        return data, 200

class RecentOrdersResource(Resource):
    def get(self):
        orders = get_recent_orders()
        return invoice_schema.dump(orders), 200

class SupplierPaymentSummaryResource(Resource):
    def get(self):
        summary = get_supplier_payment_summary()
        return summary, 200
