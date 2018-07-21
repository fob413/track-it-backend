"""empty message

Revision ID: 80326a97a197
Revises: 2f4516515142
Create Date: 2018-07-21 00:54:31.385134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80326a97a197'
down_revision = '2f4516515142'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shipments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pfi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('shipments_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['shipments_id'], ['shipments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pfi')
    op.drop_table('shipments')
    # ### end Alembic commands ###