"""empty message

Revision ID: d0e3164faea1
Revises: 
Create Date: 2022-04-28 10:29:57.875000

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op
from app.models.client_model import Client

# revision identifiers, used by Alembic.
revision = 'd0e3164faea1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.Column('occupation', sa.String(length=30), nullable=True),
    sa.Column('gender', sqlalchemy_utils.types.choice.ChoiceType(Client.GENDER_CHOICES), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clients')
    # ### end Alembic commands ###
