"""Add supplier and financial tables

Revision ID: a494c599c4b7
Revises: 62a8f7a9ec93
Create Date: 2025-06-29 06:12:10.922535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a494c599c4b7'
down_revision = '62a8f7a9ec93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('suppliers',
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('image_path', sa.String(length=255), nullable=True),
    sa.Column('supplier_name', sa.String(length=100), nullable=False),
    sa.Column('supplier_email', sa.String(length=100), nullable=False),
    sa.Column('supplier_phone', sa.String(length=10), nullable=False),
    sa.Column('supplier_address', sa.String(length=200), nullable=False),
    sa.Column('supplier_balance', sa.Float(), nullable=False),
    sa.Column('contact_person', sa.String(length=100), nullable=False),
    sa.Column('contact_person_no', sa.String(length=10), nullable=False),
    sa.Column('package_mode', sa.Text(), nullable=True),
    sa.Column('vat', sa.Boolean(), nullable=True),
    sa.Column('stock', sa.Boolean(), nullable=True),
    sa.Column('utility', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('supplier_id'),
    sa.UniqueConstraint('supplier_email'),
    sa.UniqueConstraint('supplier_phone')
    )
    op.create_table('invoices',
    sa.Column('invoice_id', sa.Integer(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('invoice_number', sa.String(length=50), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('issue_date', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('due_date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.supplier_id'], ),
    sa.PrimaryKeyConstraint('invoice_id'),
    sa.UniqueConstraint('invoice_number')
    )
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('payment_date', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('method', sa.String(length=50), nullable=True),
    sa.Column('reference', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.supplier_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('supplier_postings',
    sa.Column('posting_id', sa.Integer(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('posting_date', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.supplier_id'], ),
    sa.PrimaryKeyConstraint('posting_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('supplier_postings')
    op.drop_table('payments')
    op.drop_table('invoices')
    op.drop_table('suppliers')
    # ### end Alembic commands ###
