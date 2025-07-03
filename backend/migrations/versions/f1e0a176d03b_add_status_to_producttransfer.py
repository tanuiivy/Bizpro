"""Add status to ProductTransfer

Revision ID: f1e0a176d03b
Revises: b5649f2af376
Create Date: 2025-07-03 08:20:39.508087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1e0a176d03b'
down_revision = 'b5649f2af376'
branch_labels = None
depends_on = None


# Create the Enum type first
transfer_status_enum = sa.Enum('pending', 'completed', 'canceled', name='transfer_status_enum')


def upgrade():
    # Create the enum type explicitly
    transfer_status_enum.create(op.get_bind(), checkfirst=True)

    # Then add the column
    with op.batch_alter_table('product_transfer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', transfer_status_enum, nullable=False, server_default='pending'))


def downgrade():
    with op.batch_alter_table('product_transfer', schema=None) as batch_op:
        batch_op.drop_column('status')

    # Drop the enum type
    transfer_status_enum.drop(op.get_bind(), checkfirst=True)
