"""empty message

Revision ID: 046297158e4d
Revises: 914e9055ad37
Create Date: 2018-07-21 11:05:43.822704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '046297158e4d'
down_revision = '914e9055ad37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pfi', sa.Column('hscode_percentage', sa.Integer(), nullable=False))
    op.add_column('pfi', sa.Column('unit_cost', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pfi', 'unit_cost')
    op.drop_column('pfi', 'hscode_percentage')
    # ### end Alembic commands ###
