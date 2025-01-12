"""add_description_to_user

Revision ID: a04aecf6b163
Revises: f7a0650b42c5
Create Date: 2025-01-12 14:08:59.081335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a04aecf6b163'
down_revision = 'f7a0650b42c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
