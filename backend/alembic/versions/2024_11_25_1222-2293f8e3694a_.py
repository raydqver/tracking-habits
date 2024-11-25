"""empty message

Revision ID: 2293f8e3694a
Revises: 204859f1683e
Create Date: 2024-11-25 12:22:35.451933

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2293f8e3694a"
down_revision: Union[str, None] = "204859f1683e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "habits", sa.Column("is_frozen", sa.Boolean(), nullable=False)
    )
    op.add_column(
        "habits",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
    )
    op.alter_column(
        "habits", "description", existing_type=sa.TEXT(), nullable=False
    )
    op.alter_column(
        "habits",
        "notification_hour",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "habits", "count", existing_type=sa.INTEGER(), nullable=False
    )
    op.drop_column("users", "notification_hour")
    op.drop_column("users", "count")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column("count", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "users",
        sa.Column(
            "notification_hour",
            sa.INTEGER(),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.alter_column(
        "habits", "count", existing_type=sa.INTEGER(), nullable=True
    )
    op.alter_column(
        "habits",
        "notification_hour",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "habits", "description", existing_type=sa.TEXT(), nullable=True
    )
    op.drop_column("habits", "created_at")
    op.drop_column("habits", "is_frozen")
    # ### end Alembic commands ###
