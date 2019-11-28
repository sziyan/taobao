"""empty message

Revision ID: 35d48998070c
Revises: 27dfa8867c82
Create Date: 2019-11-28 15:27:54.015853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35d48998070c'
down_revision = '27dfa8867c82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('status', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'status')
    # ### end Alembic commands ###
