"""First revision

Revision ID: 41dd4afb9418
Revises: 
Create Date: 2022-08-09 11:37:39.179895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41dd4afb9418'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_school',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_contract',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('school_id', sa.Integer(), nullable=False),
    sa.Column('mat', sa.String(), nullable=False),
    sa.Column('start', sa.Date(), nullable=False),
    sa.Column('end', sa.Date(), nullable=False),
    sa.Column('work_hours', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['school_id'], ['tb_school.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_contract')
    op.drop_table('tb_school')
    # ### end Alembic commands ###
