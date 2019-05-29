"""add creator id to questions

Revision ID: a07447cd8896
Revises: 822b3b8ea3c2
Create Date: 2019-05-29 17:03:40.276304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a07447cd8896'
down_revision = '822b3b8ea3c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('creator_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'questions', 'users', ['creator_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.drop_column('questions', 'creator_id')
    # ### end Alembic commands ###
