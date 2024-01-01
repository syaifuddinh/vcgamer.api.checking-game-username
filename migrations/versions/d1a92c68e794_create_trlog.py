"""create_trlog

Revision ID: d1a92c68e794
Revises: dbd54d99560c
Create Date: 2023-12-16 06:16:59.051894

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1a92c68e794'
down_revision: Union[str, None] = 'dbd54d99560c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
		'TRLog',
		sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), nullable=False, unique=True, server_default=sa.text("uuid_generate_v4()")),
		sa.Column('emailSource', sa.String(), nullable=False),
		sa.Column('gameSlug', sa.String(), nullable=False),
		sa.Column('providerName', sa.String(), nullable=False),
		sa.Column('userGameId', sa.String(), nullable=False),
		sa.Column('transactionTime', sa.DateTime(), nullable=False),
		sa.Column('activityStatus', sa.String(), nullable=False),
		sa.Column('userGameAvailabilityStatus', sa.String(), nullable=True),
		sa.Column('descriptionSlug', sa.String(), nullable=False),
		sa.Column('description', sa.String(), nullable=False),
		sa.PrimaryKeyConstraint('id')
	)

    op.create_index('TRLog_Searching', 'TRLog', ['emailSource', 'userGameId'], unique=False)
    op.create_index('TRLog_Time', 'TRLog', ['transactionTime'], unique=False)
    op.create_index('TRLog_Game', 'TRLog', ['gameSlug'], unique=False)
    op.create_index('TRLog_Status', 'TRLog', ['activityStatus'], unique=False)
    op.create_index('TRLog_Provider', 'TRLog', ['providerName'], unique=False)
    op.create_index('TRLog_DescriptionSlug', 'TRLog', ['descriptionSlug'], unique=False)

def downgrade() -> None:
    op.drop_table('TRLog')
