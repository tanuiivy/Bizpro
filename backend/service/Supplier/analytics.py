from extensions import db
from models.Supplier.supplier import Supplier
from models.Supplier.invoice import Invoice
from models.Supplier.payments import Payment

#read-total payments made to suppliers
def get_total_payments():
    total = db.session.query(db.func.sum(Payment.amount)).scalar() or 0
    return {"total_payments": total}

#read-number of  pending orders (status Pending)
def get_pending_orders_count():
    count = Invoice.query.filter_by(status="Pending").count()
    return {"pending_orders": count}

#read-number of completed orders (status Delivered)
def get_completed_orders_count():
    count = Invoice.query.filter_by(status="Delivered").count()
    return {"completed_orders": count}

#read-number of orders (sum of invoice amounts)
def get_total_order_value():
    total = db.session.query(db.func.sum(Invoice.amount)).scalar() or 0
    return {"total_order_value": total}

#read-recent orders
def get_recent_orders(limit=5):
    return Invoice.query.order_by(Invoice.issue_date.desc()).limit(limit).all()
    
#read-recent supplier payments
def get_supplier_payment_summary():
    results = (
        db.session.query(Supplier.supplier_name, db.func.sum(Payment.amount))
        .join(Payment)
        .group_by(Supplier.supplier_name)
        .all()
    )
    return [{"supplier_name": name, "total_paid": total} for name, total in results]
