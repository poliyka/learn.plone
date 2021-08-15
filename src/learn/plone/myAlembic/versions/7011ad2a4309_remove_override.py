"""remove_override

Revision ID: 7011ad2a4309
Revises: 93a4f1dfebf9
Create Date: 2021-08-15 19:23:12.223061

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7011ad2a4309'
down_revision = '93a4f1dfebf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True))
        batch_op.drop_column('test')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test', mysql.VARCHAR(collation='utf8mb4_general_ci', length=64), nullable=True))
        batch_op.drop_column('age')

    # ### end Alembic commands ###
