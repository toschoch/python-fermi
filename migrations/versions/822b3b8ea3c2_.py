"""empty message

Revision ID: 822b3b8ea3c2
Revises: 
Create Date: 2019-05-29 16:03:38.003165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '822b3b8ea3c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('users',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('password', sa.String(length=255), nullable=False),
                    sa.Column('registered_on', sa.DateTime(), nullable=False),
                    sa.Column('admin', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('answer', sa.Float(), nullable=False),
    sa.Column('uncertainty', sa.Float(), nullable=True),
    sa.Column('creation', sa.DateTime(), nullable=False),
    sa.Column('source', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    op.drop_table('users')
    # ### end Alembic commands ###