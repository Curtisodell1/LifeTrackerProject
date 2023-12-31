"""adding models 

Revision ID: dde1145ee19e
Revises: 
Create Date: 2023-09-26 11:23:51.297286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dde1145ee19e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('activity', sa.String(), nullable=True),
    sa.Column('activity_status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feelings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('morning_feeling', sa.Integer(), nullable=True),
    sa.Column('afternoon_feeling', sa.Integer(), nullable=True),
    sa.Column('evening_feeling', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('_password_hash', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('days',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feeling_id', sa.Integer(), nullable=True),
    sa.Column('activity_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['activities.id'], name=op.f('fk_days_activity_id_activities')),
    sa.ForeignKeyConstraint(['feeling_id'], ['feelings.id'], name=op.f('fk_days_feeling_id_feelings')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('days')
    op.drop_table('users')
    op.drop_table('feelings')
    op.drop_table('activities')
    # ### end Alembic commands ###
