"""create_mtserver

Revision ID: c17539a07c97
Revises: d6116edf5e30
Create Date: 2023-12-25 17:17:12.124685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c17539a07c97'
down_revision: Union[str, None] = 'd6116edf5e30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
		'MTServer',
		sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), nullable=False, unique=True, server_default=sa.text("uuid_generate_v4()")),
		sa.Column('gameSlug', sa.String(), nullable=False),
		sa.Column('serverSlug', sa.String(), nullable=False),
		sa.Column('serverName', sa.String(), nullable=False),
		sa.Column('codashopIndex', sa.String(), nullable=True),
		sa.PrimaryKeyConstraint('id')
	)
    op.create_index('MTServer_GameSlug', 'MTServer', ['gameSlug'], unique=False)
    op.create_index('MTServer_GameAndServerSlug', 'MTServer', ['gameSlug', 'serverSlug'], unique=True)


def downgrade() -> None:
    op.drop_table('MTServer')
