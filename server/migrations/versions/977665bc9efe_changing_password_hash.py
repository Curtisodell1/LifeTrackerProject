"""changing password hash

Revision ID: 977665bc9efe
Revises: 81e5576f2790
Create Date: 2023-09-28 20:33:51.059700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '977665bc9efe'
down_revision = '81e5576f2790'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('_password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password_hash', sa.TEXT(), nullable=False))

    # ### end Alembic commands ###
