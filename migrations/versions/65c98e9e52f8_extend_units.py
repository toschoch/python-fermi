"""extend units

Revision ID: 65c98e9e52f8
Revises: 5a1d863e8d25
Create Date: 2019-10-08 18:02:18.026285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65c98e9e52f8'
down_revision = '5a1d863e8d25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question_category_assignments', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('question_category_assignments', 'question_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('units', "name", new_column_name="description")
    op.add_column('units', sa.Column('formula', sa.String(), nullable=True))
    op.add_column('units', sa.Column('latex', sa.String(), nullable=True))
    op.add_column('units', sa.Column('quantity', sa.String(), nullable=True))
    op.add_column('units', sa.Column('shortFormula', sa.String(), nullable=True))
    op.add_column('units', sa.Column('wikidata', sa.String(), nullable=True))

    bind = op.get_bind()
    bind.execute("UPDATE public.units SET \"description\"='per square centimeters', \"formula\"='1/(centimeter)^2', "
                 "\"shortFormula\"='1/cm^2', \"latex\"='$1/{cm}^2$' WHERE description='1/(centimeter)^2'")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('units', 'wikidata')
    op.drop_column('units', 'shortFormula')
    op.drop_column('units', 'quantity')
    op.drop_column('units', 'latex')
    op.drop_column('units', 'formula')

    op.alter_column('units', "description", new_column_name="name")
    op.alter_column('question_category_assignments', 'question_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('question_category_assignments', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
