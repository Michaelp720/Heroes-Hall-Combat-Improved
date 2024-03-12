"""empty message

Revision ID: 4e8e7895cce2
Revises: 
Create Date: 2024-03-11 17:11:00.631854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e8e7895cce2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('max_hp', sa.Integer(), nullable=True),
    sa.Column('base_pwr', sa.Integer(), nullable=True),
    sa.Column('base_def', sa.Integer(), nullable=True),
    sa.Column('spd', sa.Integer(), nullable=True),
    sa.Column('crnt_hp', sa.Integer(), nullable=True),
    sa.Column('temp_pwr', sa.Integer(), nullable=True),
    sa.Column('temp_def', sa.Integer(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('techs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('target', sa.String(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('stat', sa.String(), nullable=True),
    sa.Column('amnt', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('known_techs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slot', sa.Integer(), nullable=True),
    sa.Column('rnk', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('tech_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], name=op.f('fk_known_techs_character_id_characters')),
    sa.ForeignKeyConstraint(['tech_id'], ['techs.id'], name=op.f('fk_known_techs_tech_id_techs')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['characters.id'], name=op.f('fk_player_id_characters')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('combats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('enemy_id', sa.Integer(), nullable=True),
    sa.Column('rnd', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enemy_id'], ['characters.id'], name=op.f('fk_combats_enemy_id_characters')),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name=op.f('fk_combats_player_id_player')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('remaining_duration', sa.Integer(), nullable=True),
    sa.Column('affected_stat', sa.String(), nullable=True),
    sa.Column('amnt', sa.Integer(), nullable=True),
    sa.Column('combat_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], name=op.f('fk_statuses_character_id_characters')),
    sa.ForeignKeyConstraint(['combat_id'], ['combats.id'], name=op.f('fk_statuses_combat_id_combats')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('statuses')
    op.drop_table('combats')
    op.drop_table('player')
    op.drop_table('known_techs')
    op.drop_table('techs')
    op.drop_table('characters')
    # ### end Alembic commands ###
