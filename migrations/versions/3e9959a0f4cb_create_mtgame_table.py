"""create MTGame table

Revision ID: 3e9959a0f4cb
Revises: 
Create Date: 2023-12-06 22:01:04.096487

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision: str = '3e9959a0f4cb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
	op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
	op.create_table(
		'MTGame',
		sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), nullable=False, unique=True, server_default=sa.text("uuid_generate_v4()")),
		sa.Column('name', sa.String(), nullable=False),
		sa.Column('slug', sa.String(), nullable=False),
		sa.Column('thumbnailUrl', sa.String(), nullable=True),
		sa.Column('hasCodashop', sa.Boolean(), nullable=False, server_default=sa.text("False")),
		sa.Column('hasJollymax', sa.Boolean(), nullable=False, server_default=sa.text("False")),
		sa.PrimaryKeyConstraint('id')
	)
	op.create_index('GameNameIndex', 'MTGame', ['name'], unique=False)
	op.create_index('GameSlugIndex', 'MTGame', ['slug'], unique=False)


def downgrade() -> None:
    op.drop_table('MTGame')
