"""seed_codashop_availability

Revision ID: dbd54d99560c
Revises: 6345adac68f3
Create Date: 2023-12-14 10:06:59.645440

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dbd54d99560c'
down_revision: Union[str, None] = '6345adac68f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
    	UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'mobile-legends' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'valorant' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'ragnarok-eternal-love' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'point-blank-beyonds-limit' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'genshin-impact' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'dragon-raja' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'arena-of-valor' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'clash-of-clans' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'call-of-duty-mobile' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'hay-day' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'honkai-impact-3' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'life-after' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'league-of-legends-wild-rift' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'one-punch-man-the-strongest' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'zepeto' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'free-fire' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'ragnarok-x-generation' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'sausage-man' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'super-sus' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'ludo-club' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'era-of-celestials' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'revelation-infinite-journey' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'marvel-snap' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'stumble-guys' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'clash-royale' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'brawl-stars' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'undawn' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'honkai-star-rail' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'metal-slug-awakening' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'eggy-party' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'ea-sports-fc' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'farlight-84' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'kings-choice' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'among-heroes-fantasy-samkok' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'dynasty-warriors-overlords' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'scroll-of-onymyoji' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'madtale-idle-rpg' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'idle-legends-god-saga' ;
		UPDATE "MTGame" SET "hasCodashop" = True WHERE slug = 'miko-era-twelve-myths' ;
    ''')


def downgrade() -> None:
    op.execute('UPDATE public."MTGame" SET "hasCodashop" = False')
