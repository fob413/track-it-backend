"""empty message

Revision ID: fe15c4205329
Revises: 
Create Date: 2018-07-21 13:47:44.475885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe15c4205329'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shipments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('formm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('shipments_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['shipments_id'], ['shipments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pfi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('supplier_name', sa.String(length=80), nullable=False),
    sa.Column('pfi_number', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('shipments_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.Column('hs_code', sa.Integer(), nullable=False),
    sa.Column('items_detail', sa.Text(), nullable=True),
    sa.Column('pfi_type', sa.String(length=80), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('hscode_percentage', sa.Integer(), nullable=False),
    sa.Column('unit_cost', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['shipments_id'], ['shipments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('insurance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('insurance_number', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=80), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('formm_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['formm_id'], ['formm.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('letterofcredit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('letter_number', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=80), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('formm_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['formm_id'], ['formm.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('letterofcredit')
    op.drop_table('insurance')
    op.drop_table('pfi')
    op.drop_table('formm')
    op.drop_table('shipments')
    op.drop_table('users')
    # ### end Alembic commands ###
