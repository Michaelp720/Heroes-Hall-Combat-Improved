"""empty message

Revision ID: be78090cd2a1
Revises: 4e8e7895cce2
Create Date: 2024-03-11 17:23:14.098611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be78090cd2a1'
down_revision = '4e8e7895cce2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('enemy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('actions', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['characters.id'], name=op.f('fk_enemy_id_characters')),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('combats', schema=None) as batch_op:
        batch_op.drop_constraint('fk_combats_enemy_id_characters', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_combats_enemy_id_enemy'), 'enemy', ['enemy_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('combats', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_combats_enemy_id_enemy'), type_='foreignkey')
        batch_op.create_foreign_key('fk_combats_enemy_id_characters', 'characters', ['enemy_id'], ['id'])

    op.drop_table('enemy')
    # ### end Alembic commands ###