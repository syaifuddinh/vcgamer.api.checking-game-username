"""seed_mtcodashopgame

Revision ID: 6345adac68f3
Revises: a51d5bb81531
Create Date: 2023-12-08 23:31:19.136530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6345adac68f3'
down_revision: Union[str, None] = 'a51d5bb81531'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
    	INSERT INTO public."MTCodashopGame" ("gameSlug", "codashopSlug", "additionalField") VALUES('mobile-legends', 'MOBILE_LEGENDS', 'zoneId');
    ''')


def downgrade() -> None:
    op.execute('DELETE FROM public."MTCodashopGame"')
