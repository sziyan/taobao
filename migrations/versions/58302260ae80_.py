"""empty message

Revision ID: 58302260ae80
Revises: 35d48998070c
Create Date: 2019-11-28 15:34:07.312640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58302260ae80'
down_revision = '35d48998070c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('ship_amount', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'ship_amount')
    # ### end Alembic commands ###