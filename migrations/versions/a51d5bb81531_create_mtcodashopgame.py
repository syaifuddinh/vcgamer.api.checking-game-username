"""create_mtcodashopgame

Revision ID: a51d5bb81531
Revises: 32f700047e1a
Create Date: 2023-12-07 22:54:39.351674

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a51d5bb81531'
down_revision: Union[str, None] = '32f700047e1a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
		'MTCodashopGame',
		sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), nullable=False, unique=True, server_default=sa.text("uuid_generate_v4()")),
		sa.Column('codashopSlug', sa.String(), nullable=False),
		sa.Column('gameSlug', sa.String(), nullable=False),
		sa.Column('additionalField', sa.String(), nullable=True),
		sa.Column('additionalFieldType', sa.String(), nullable=False),
		sa.PrimaryKeyConstraint('id')
	)
    op.create_index('MTCodashopGame-GameSlugIndex', 'MTCodashopGame', ['gameSlug'], unique=False)

def downgrade() -> None:
	op.drop_table('MTCodashopGame')
