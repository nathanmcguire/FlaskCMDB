"""Add number field to implementation_groups table

Revision ID: 872c2fd3050a
Revises: 9ca1126c2fd7
Create Date: 2025-03-11 10:42:02.961732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '872c2fd3050a'
down_revision = '9ca1126c2fd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('implementation_groups', sa.Column('number', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('implementation_groups', 'number')
    # ### end Alembic commands ###
