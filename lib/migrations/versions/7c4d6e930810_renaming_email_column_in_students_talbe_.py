"""Renaming email column in students talbe to contact

Revision ID: 7c4d6e930810
Revises: 791279dd0760
Create Date: 2023-01-21 00:21:28.239480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c4d6e930810'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='contact')
    pass


def downgrade() -> None:
    op.alter_column('students', 'contact', new_column_name='email')
    pass
