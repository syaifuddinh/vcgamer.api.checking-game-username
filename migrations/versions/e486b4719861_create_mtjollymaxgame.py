"""create_mtjollymaxgame

Revision ID: e486b4719861
Revises: d1a92c68e794
Create Date: 2023-12-17 11:18:57.190730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e486b4719861'
down_revision: Union[str, None] = 'd1a92c68e794'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
		'MTJollymaxGame',
		sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), nullable=False, unique=True, server_default=sa.text("uuid_generate_v4()")),
		sa.Column('gameSlug', sa.String(), nullable=False),
		sa.Column('jollymaxSlug', sa.String(), nullable=False),
		sa.Column('jollymaxAppId', sa.String(), nullable=False),
		sa.Column('jollymaxGoodId', sa.String(), nullable=False),
		sa.Column('additionalField', sa.String(), nullable=True),
		sa.Column('additionalFieldType', sa.String(), nullable=False),
		sa.PrimaryKeyConstraint('id')
	)


def downgrade() -> None:
    op.drop_table('MTJollymaxGame')
