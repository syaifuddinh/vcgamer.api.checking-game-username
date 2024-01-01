"""create_mtuser

Revision ID: d7cb498f9fbd
Revises: ccfa6c522b41
Create Date: 2023-12-21 11:00:13.525932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7cb498f9fbd'
down_revision: Union[str, None] = 'ccfa6c522b41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
	op.create_table(
		'MTUser',
		sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), nullable=False, unique=True, server_default=sa.text("uuid_generate_v4()")),
		sa.Column('fullname', sa.String(), nullable=False),
		sa.Column('email', sa.String(), nullable=False, unique=True),
		sa.Column('password', sa.String(), nullable=False),
		sa.Column('apiKey', sa.String(), nullable=False, unique=True),
		sa.PrimaryKeyConstraint('id')
	)
	op.create_index('EmailIndex', 'MTUser', ['email'], unique=False)


def downgrade() -> None:
    op.drop_table('MTUser')
