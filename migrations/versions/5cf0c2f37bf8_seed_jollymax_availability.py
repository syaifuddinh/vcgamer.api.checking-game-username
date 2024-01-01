"""seed_jollymax_availability

Revision ID: 5cf0c2f37bf8
Revises: 6a5a401a695a
Create Date: 2023-12-17 19:27:43.857624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5cf0c2f37bf8'
down_revision: Union[str, None] = '6a5a401a695a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
    	UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'mobile-legends';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'valorant';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'point-blank-beyonds-limit';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'dragon-raja';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'arena-of-valor';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'clash-of-clans';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'call-of-duty-mobile';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'hay-day';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'honkai-impact-3';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'light-of-thel';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'league-of-legends-wild-rift';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'lords-mobile';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'one-punch-man-the-strongest';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'zepeto';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'free-fire';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'ragnarok-x-generation';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'sausage-man';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'super-sus';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'ludo-club';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'revelation-infinite-journey';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'ace-racer';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'stumble-guys';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'goddess-of-victory-nikke';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'clash-royale';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'undawn';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'metal-slug-awakening';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'eggy-party';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'jade-legends';
		UPDATE "MTGame" SET "hasJollymax" = True WHERE slug = 'scroll-of-onymyoji';
    ''')


def downgrade() -> None:
    op.execute('UPDATE public."MTGame" SET "hasJollymax" = False')
