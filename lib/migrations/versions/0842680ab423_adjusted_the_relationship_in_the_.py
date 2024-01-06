"""adjusted the relationship in the restaurant module

Revision ID: 0842680ab423
Revises: eb82700e1ba6
Create Date: 2024-01-06 13:07:07.210113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0842680ab423'
down_revision: Union[str, None] = 'eb82700e1ba6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_customers_id', table_name='customers')
    op.drop_index('ix_restaurants_id', table_name='restaurants')
    op.drop_index('ix_reviews_id', table_name='reviews')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_reviews_id', 'reviews', ['id'], unique=False)
    op.create_index('ix_restaurants_id', 'restaurants', ['id'], unique=False)
    op.create_index('ix_customers_id', 'customers', ['id'], unique=False)
    # ### end Alembic commands ###