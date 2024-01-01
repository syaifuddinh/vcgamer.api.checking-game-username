"""create_mtadditionalfield

Revision ID: f7b0905605d3
Revises: 5cf0c2f37bf8
Create Date: 2023-12-19 11:11:16.640473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7b0905605d3'
down_revision: Union[str, None] = '5cf0c2f37bf8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
	op.create_table(
		'MTAdditionalField',
		sa.Column('id', sa.dialects.postgresql.UUID(as_uuid=True), nullable=False, unique=True, server_default=sa.text("uuid_generate_v4()")),
		sa.Column('gameSlug', sa.String(), nullable=False),
		sa.Column('additionalField', sa.String(), nullable=False),
		sa.Column('additionalFieldType', sa.String(), nullable=False),
		sa.Column('additionalFieldLabel', sa.String(), nullable=False),
		sa.PrimaryKeyConstraint('id')
	)
   
	op.create_index('MTAdditionalField-GameSlugIndex', 'MTAdditionalField', ['gameSlug'], unique=False)


def downgrade() -> None:
	op.drop_table('MTAdditionalField')
