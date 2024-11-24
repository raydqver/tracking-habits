"""empty message

Revision ID: 204859f1683e
Revises: e79d0a50e642
Create Date: 2024-11-24 21:34:18.735451

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "204859f1683e"
down_revision: Union[str, None] = "e79d0a50e642"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "habits", "description", existing_type=sa.TEXT(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "habits", "description", existing_type=sa.TEXT(), nullable=False
    )
    # ### end Alembic commands ###