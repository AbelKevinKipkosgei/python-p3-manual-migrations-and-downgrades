"""Renaming column <grade> in students to <grade_level>.

Revision ID: e0ad36d19fee
Revises: 3a340b461ad3
Create Date: 2024-09-18 07:18:20.890452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0ad36d19fee'
down_revision = '3a340b461ad3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("scholars", "students")
    op.alter_column("students", "grade", new_column_name="grade_level")


def downgrade() -> None:
    op.alter_column("students", "grade_level", new_column_name="grade")
