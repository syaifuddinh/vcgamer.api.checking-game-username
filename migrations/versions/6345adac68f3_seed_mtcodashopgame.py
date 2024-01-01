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
    	INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('mobile-legends', 'mobile-legends', 'zoneId', 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('valorant', 'valorant', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('ragnarok-m-eternal-love-big-cat-coin', 'ragnarok-eternal-love', 'server', 'OPTIONS');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('point-blank', 'point-blank-beyonds-limit', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('genshin-impact', 'genshin-impact', 'server', 'OPTIONS');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('dragon-raja', 'dragon-raja', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('arena-of-valor', 'arena-of-valor', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('clash-of-clans', 'clash-of-clans', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('call-of-duty-mobile', 'call-of-duty-mobile', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('hay-day', 'hay-day', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('honkai-impact-3', 'honkai-impact-3', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('lifeafter', 'life-after', 'server', 'OPTIONS');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('league-of-legends-wild-rift', 'league-of-legends-wild-rift', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('one-punch-man-the-strongest', 'one-punch-man-the-strongest', 'serverId', 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('zepeto', 'zepeto', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('free-fire', 'free-fire', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('ragnarok-x-next-generation', 'ragnarok-x-generation', 'server', 'OPTIONS');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('sausage-man', 'sausage-man', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('super-sus', 'super-sus', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('ludo-club', 'ludo-club', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('era-of-celestials', 'era-of-celestials', 'server', 'OPTIONS');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('revelation-infinite-journey', 'revelation-infinite-journey', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('marvel-snap', 'marvel-snap', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('stumble-guys', 'stumble-guys', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('clash-royale', 'clash-royale', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('brawl-stars', 'brawl-stars', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('undawn', 'undawn', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('honkai-star-rail', 'honkai-star-rail', 'server', 'OPTIONS');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('metal-slug-awakening', 'metal-slug-awakening', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('eggy-party', 'eggy-party', 'server', 'OPTIONS');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('ea-sports-fc-mobile', 'ea-sports-fc', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('farlight-84', 'farlight-84', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('kings-choice', 'kings-choice', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('among-heroes-fantasy-samkok', 'among-heroes-fantasy-samkok', 'server', 'OPTIONS');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('dynasty-warriors-overlords', 'dynasty-warriors-overlords', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('scroll-of-onymyoji', 'scroll-of-onymyoji', 'server', 'AUTOFILL');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('madtale-idle-rpg', 'madtale-idle-rpg', null, 'TEXT');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('idle-legends-god-saga', 'idle-legends-god-saga', 'server', 'AUTOFILL');
		INSERT INTO "MTCodashopGame" ("codashopSlug", "gameSlug", "additionalField", "additionalFieldType") VALUES ('miko-era-twelve-myths', 'miko-era-twelve-myths', 'server', 'OPTIONS');

    ''')


def downgrade() -> None:
    op.execute('DELETE FROM public."MTCodashopGame"')
