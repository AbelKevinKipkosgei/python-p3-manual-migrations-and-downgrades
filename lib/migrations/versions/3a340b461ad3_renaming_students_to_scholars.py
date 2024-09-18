"""Renaming students to scholars.

Revision ID: 3a340b461ad3
Revises: 791279dd0760
Create Date: 2024-09-18 07:02:22.073611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a340b461ad3'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("students", "scholars")


def downgrade() -> None:
    op.rename_table("scholars", "students")
