"""init schema

Revision ID: 04541700cb92
Revises: 
Create Date: 2021-10-09 18:28:44.572209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04541700cb92'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE users_types (
            id VARCHAR PRIMARY KEY NOT NULL,
            name VARCHAR NOT NULL
        )
        """
    )


def downgrade():
    op.execute("DROP TABLE users_types CASCADE")
