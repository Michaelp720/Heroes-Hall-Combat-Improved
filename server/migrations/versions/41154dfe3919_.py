"""empty message

Revision ID: 41154dfe3919
Revises: 28bb08ffa851
Create Date: 2024-03-25 20:32:38.236609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41154dfe3919'
down_revision = '28bb08ffa851'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('enemy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('threat_rating', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('enemy', schema=None) as batch_op:
        batch_op.drop_column('threat_rating')

    # ### end Alembic commands ###
