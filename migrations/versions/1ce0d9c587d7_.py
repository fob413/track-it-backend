"""empty message

Revision ID: 1ce0d9c587d7
Revises: 94bb313ab372
Create Date: 2018-07-21 06:51:09.452214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ce0d9c587d7'
down_revision = '94bb313ab372'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pfi', sa.Column('pfi_type', sa.String(length=80), nullable=True))
    op.drop_column('pfi', 'pft_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pfi', sa.Column('pft_type', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.drop_column('pfi', 'pfi_type')
    # ### end Alembic commands ###
