"""seed_mtjollymaxgame

Revision ID: 6a5a401a695a
Revises: e486b4719861
Create Date: 2023-12-17 19:23:16.030165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a5a401a695a'
down_revision: Union[str, None] = 'e486b4719861'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
    	INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('mobile-legends', 'mlbb_diamonds', 'APP20210608084718702', 'G20231123033110502', 'serverId', 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('valorant', 'Valorant', 'APP20220121125657101', 'G20220121125926906', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('point-blank-beyonds-limit', 'PointBlank', 'APP20210820080230203', 'G20220506092154903', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('dragon-raja', 'DragonRaja', 'APP20220214080751701', 'G20220214081922310', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('arena-of-valor', 'ArenaofValor', 'APP20210820080018104', 'G20220104055440005', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('clash-of-clans', 'ClashofClan', 'APP20230525104008101', 'G20230525110808516', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('call-of-duty-mobile', 'COD', 'APP20210926025003301', 'G20230801131903101', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('hay-day', 'HayDay', 'APP20230525123018003', 'G20230606100039460', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('honkai-impact-3', 'Honkaiimpact3', 'APP20230216131947101', 'G20230221031718738', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('light-of-thel', 'LightofThel', 'APP20230216131947101', 'G20230221031718738', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('league-of-legends-wild-rift', 'lolm', 'APP20220214075731202', 'G20231120083559306', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('lords-mobile', 'LordsMobile', 'APP20210820075934102', 'G20230628033856305', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('one-punch-man-the-strongest', 'OnePunchMan', 'APP20220113070824401', 'G20221115121029204', 'serverId', 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('zepeto', 'Zepeto', 'APP20230817095242703', 'G20231127074024315', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('free-fire', 'kyd_ff_50diamonds', 'APP20210820075855101', 'G20220105115515605', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('ragnarok-x-generation', 'ragnarokX', 'APP20220324061330801', 'G20230919115048301', 'server', 'OPTIONS');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('sausage-man', 'sausageman', 'APP20220113071133701', 'G20220506101525603', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('super-sus', 'SuperSus', 'APP20220419030726501', 'G20220419031659001', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('ludo-club', 'LudoClub', 'APP20221118071001203', 'G20230417122610713', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('revelation-infinite-journey', 'revelation_infinite_journey', 'APP20230207033757405', 'G20230329100208802', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('ace-racer', 'aceracer', 'APP20230314162731801', 'G20230421034933907', 'server', 'OPTIONS');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('stumble-guys', 'stumbleguystopup', 'APP20230630033048001', 'G20230630095751161', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('goddess-of-victory-nikke', 'NIKKE', 'APP20230213055737801', 'G20230911124549436', 'server', 'OPTIONS');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('clash-royale', 'ClashRoyale', 'APP20230525114126102', 'G20230525114738626', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('undawn', 'undawn_garena', 'APP20230720093016201', 'G20230725084455643', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('metal-slug-awakening', 'MetalSlug', 'APP20231012113209504', 'G20231012114523784', null, 'TEXT');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('eggy-party', 'EGGYPARTY', 'APP20230517085457901', 'G20230517090203211', 'server', 'OPTIONS');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('jade-legends', 'Jade_Legends', 'APP20220816054209401', 'G20230807124527503', 'server', 'OPTIONS');
		INSERT INTO "MTJollymaxGame" ("gameSlug", "jollymaxSlug", "jollymaxAppId", "jollymaxGoodId", "additionalField", "additionalFieldType") VALUES ('scroll-of-onymyoji', 'scrollofonmyoji', 'APP20220809025521101', 'G20230807124518010', 'server', 'OPTIONS');
    ''')


def downgrade() -> None:
    op.execute('DELETE FROM "MTJollymaxGame"')
