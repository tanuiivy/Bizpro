from extensions import ma
from models.Stock.company import Company
from models.Stock.product import Product
from models.Stock.reference import (
    ProductCategory,
    ProductSubCategory,
    Shop,
    Store,
    Shelf,
    PackageMode
)
from models.Stock.transfer import ProductTransfer
from models.Stock.write_off import WriteOff
from models.Stock.conversion import ProductConversion

# Company Schema
class CompanySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Company
        load_instance = True

    company_id = ma.auto_field()
    company_name = ma.auto_field()
    company_email = ma.auto_field()
    company_phone = ma.auto_field()
    company_phone_2 = ma.auto_field()
    county = ma.auto_field()
    sub_county = ma.auto_field()
    city = ma.auto_field()
    company_address = ma.auto_field()
    company_address_2 = ma.auto_field()
    zip_code = ma.auto_field()
    product_category = ma.auto_field()
    product_sub_category = ma.auto_field()
    vat = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()

# Product Schema
class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product
        load_instance = True

    product_id = ma.auto_field()
    product_name = ma.auto_field()
    product_description = ma.auto_field()
    part_number = ma.auto_field()
    barcode = ma.auto_field()
    buying_price = ma.auto_field()
    wholesale_price = ma.auto_field()
    retail_price = ma.auto_field()
    product_type = ma.auto_field()
    product_category_id = ma.auto_field()
    product_sub_category_id = ma.auto_field()
    shop_id = ma.auto_field()
    store_id = ma.auto_field()
    shelf_id = ma.auto_field()
    package_mode_id = ma.auto_field()
    shelf_names = ma.auto_field()
    shop_quantity = ma.auto_field()
    store_quantity = ma.auto_field()
    component = ma.auto_field()
    hot_list = ma.auto_field()
    dormant = ma.auto_field()
    apply_vat = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()

# ProductCategory Schema
class ProductCategorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = ProductCategory
        load_instance = True

    category_id = ma.auto_field()
    product_category = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()

# ProductSubCategory Schema
class ProductSubCategorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = ProductSubCategory
        load_instance = True

    sub_category_id = ma.auto_field()
    product_sub_category = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()

# Shop Schema
class ShopSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Shop
        load_instance = True

    shop_id = ma.auto_field()
    shop_name = ma.auto_field()
    company_id = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()

# Store Schema
class StoreSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Store
        load_instance = True

    store_id = ma.auto_field()
    company_id = ma.auto_field()
    store_name = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()

# Shelf Schema
class ShelfSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Shelf
        load_instance = True

    shelf_id = ma.auto_field()
    store_id = ma.auto_field()
    shelf_name = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()

# PackageMode Schema
class PackageModeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PackageMode
        load_instance = True

    package_mode_id = ma.auto_field()
    package_mode = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()

# ProductTransfer Schema
class ProductTransferSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ProductTransfer
        load_instance = True

    transfer_id = ma.auto_field()
    product_id = ma.auto_field()
    transfer_quantity = ma.auto_field()
    from_location = ma.auto_field()
    to_location = ma.auto_field()
    remarks = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()

# WriteOff Schema
class WriteOffSchema(ma.SQLAlchemySchema):
    class Meta:
        model = WriteOff
        load_instance = True

    write_off_id = ma.auto_field()
    product_id = ma.auto_field()
    write_off_quantity = ma.auto_field()
    buying_price = ma.auto_field()
    expiry_date = ma.auto_field()
    remarks = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()

# ProductConversion Schema
class ProductConversionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ProductConversion
        load_instance = True

    conversion_id = ma.auto_field()
    from_product_id = ma.auto_field()
    to_product_id = ma.auto_field()
    unit_before = ma.auto_field()
    conversion_quantity = ma.auto_field()
    unit_after = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()
