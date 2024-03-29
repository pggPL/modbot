"""Change id columns names

Revision ID: c3d017d7a014
Revises: a7bb9b5de368
Create Date: 2024-03-29 18:08:47.157768

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'c3d017d7a014'
down_revision: Union[str, None] = 'a7bb9b5de368'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("ALTER TABLE mailboxes RENAME COLUMN id TO mailbox_id")
    op.execute("ALTER TABLE mails RENAME COLUMN id TO mail_id")


def downgrade():
    op.execute("ALTER TABLE mailboxes RENAME COLUMN mailbox_id TO id")
    op.execute("ALTER TABLE mails RENAME COLUMN mail_id TO id")
