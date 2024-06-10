"""empty message

Revision ID: 4fd2dfd73f76
Revises: cea9265946d0
Create Date: 2024-04-23 21:10:15.268876

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "4fd2dfd73f76"
down_revision: Union[str, None] = "cea9265946d0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("username", sa.String(), nullable=True))
    op.add_column("users", sa.Column("full_name", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "full_name")
    op.drop_column("users", "username")
    # ### end Alembic commands ###