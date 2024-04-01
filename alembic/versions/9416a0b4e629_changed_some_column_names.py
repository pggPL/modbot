"""changed some column names

Revision ID: 9416a0b4e629
Revises: c3d017d7a014
Create Date: 2024-04-01 10:49:42.791739

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9416a0b4e629'
down_revision: Union[str, None] = 'c3d017d7a014'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table("servers", "guilds")

    op.alter_column('mailboxes', 'name', new_column_name='address')
    op.alter_column('mailboxes', 'server_id', new_column_name='guild_id')

    op.alter_column('mails', 'mailbox_name', new_column_name='sender_address')
    op.add_column("mails", sa.Column("receiver_address", sa.String(), nullable=True))


def downgrade() -> None:
    op.rename_table("guilds", "servers")

    op.alter_column('mailboxes', 'address', new_column_name='name')
    op.alter_column('mailboxes', 'guild_id', new_column_name='server_id')

    op.alter_column('mails', 'sender_address', new_column_name='mailbox_name')
    op.drop_column("mails", "receiver_address")
