"""seed_mtserver

Revision ID: fb5b796fab58
Revises: c17539a07c97
Create Date: 2023-12-27 00:28:04.427902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb5b796fab58'
down_revision: Union[str, None] = 'c17539a07c97'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
	query = '''
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('honkai-star-rail', 'America', 'america', '2');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('honkai-star-rail', 'Asia', 'asia', '1');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('honkai-star-rail', 'Europe', 'europe', '3');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('honkai-star-rail', 'TW, HK, MO', 'tw-hk-mo', '4');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('genshin-impact', 'America', 'america', '1');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('genshin-impact', 'Europe', 'europe', '2');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('genshin-impact', 'Asia', 'asia', '3');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('genshin-impact', 'TW, HK, MO', 'tw-hk-mo', '4');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('eggy-party', 'Asia', 'asia', '1');

	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-eternal-love', 'Eternal Love', 'eternal-love', '1');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-eternal-love', 'Midnight Party', 'midnight-party', '2');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-eternal-love', 'Memory of Faith', 'memory-of-faith', '3');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-eternal-love', 'Valhalla Glory', 'valhalla-glory', '4');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-eternal-love', 'Port City', 'port-city', '5');

	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'MiskaTown ', 'miskatown ', '1');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'SandCastle ', 'sandcastle ', '2');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'MouthSwamp ', 'mouthswamp ', '3');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'RedwoodTown ', 'redwoodtown ', '4');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'Obelisk ', 'obelisk ', '5');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'ChaosOutpost ', 'chaosoutpost ', '6');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'FallForest', 'fallforest', '8');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'MountSnow', 'mountsnow', '9');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'NancyCity', 'nancycity', '10');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'CharlesTown', 'charlestown', '11');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'SnowHighlands', 'snowhighlands', '12');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'Santopany', 'santopany', '13');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'LevinCity', 'levincity', '14');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'ChaosCity', 'chaoscity', '15');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'TwinIslands', 'twinislands', '16');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'NewLand ', 'newland ', '18');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'MileStone', 'milestone', '20');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'IronStride', 'ironstride', '7');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'HopeWall', 'hopewall', '17');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'CrystalhornSea', 'crystalhornsea', '19');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('life-after', 'Labyrinthsea', 'labyrinthsea', '21');

	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Opera Phantom', 'opera-phantom', '1');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Wing of Blessing', 'wing-of-blessing', '2');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Royal Instrument', 'royal-instrument', '3');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Valhalla', 'valhalla', '4');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Gungnir', 'gungnir', '5');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Central Plains', 'central-plains', '6');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Dark Lord', 'dark-lord', '7');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Clock Tower', 'clock-tower', '8');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Comodo', 'comodo', '9');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Rainbow Paradise', 'rainbow-paradise', '10');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Temple of Dawn', 'temple-of-dawn', '11');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Golden Lava', 'golden-lava', '12');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Highland', 'highland', '13');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Demon''s Castle', 'demons-castle', '14');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Sealed Island', 'sealed-island', '15');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Sipera', 'sipera', '16');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Silent Ship', 'silent-ship', '17');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Golden Route', 'golden-route', '18');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Sapir', 'sapir', '19');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Rose Red', 'rose-red', '20');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Kingdom of Freedom', 'kingdom-of-freedom', '21');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Nicola', 'nicola', '22');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Crystal Waterfall', 'crystal-waterfall', '23');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Bifrost', 'bifrost', '24');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Nastia', 'nastia', '25');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Strouf Treasury', 'strouf-treasury', '26');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Green Tranquil Pond', 'green-tranquil-pond', '27');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Ingael', 'ingael', '28');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Tome of Glory', 'tome-of-glory', '29');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Incense Pavilion', 'incense-pavilion', '30');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Carew', 'carew', '31');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Boulders and Horns', 'boulders-and-horns', '32');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Exquisite Pond', 'exquisite-pond', '33');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Nemesis', 'nemesis', '34');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Aldebaran', 'aldebaran', '35');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Honor of Emperium', 'honor-of-emperium', '36');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Frenetic Land', 'frenetic-land', '37');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Bright Lotus Pond', 'bright-lotus-pond', '38');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Seocho Market', 'seocho-market', '39');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Eudora', 'eudora', '40');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Moonlit Temple', 'moonlit-temple', '41');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Hidden Wood Ruins', 'hidden-wood-ruins', '42');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Dungeon Throne', 'dungeon-throne', '43');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Dimension Door', 'dimension-door', '44');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Gunslinger''s Revenge', 'gunslingers-revenge', '45');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Ayothaya', 'ayothaya', '46');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Luzon', 'luzon', '47');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Majapahit', 'majapahit', '48');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Garden City', 'garden-city', '49');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Manila', 'manila', '50');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Sukhothai', 'sukhothai', '51');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Attack On Poring', 'attack-on-poring', '52');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Light of Umbala', 'light-of-umbala', '53');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Tossakan', 'tossakan', '54');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Badang', 'badang', '55');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Lapulapu', 'lapulapu', '56');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Gatotkaca', 'gatotkaca', '57');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Srikandi', 'srikandi', '58');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Kumpakan', 'kumpakan', '59');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Original Love', 'original-love', '60');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Angeling', 'angeling', '61');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Deviling', 'deviling', '62');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Ghostring', 'ghostring', '63');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Mastering', 'mastering', '64');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Song Tử', 'song-tu', '65');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Xử Nữ', 'xu-nu', '66');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Half Anniversary', 'half-anniversary', '67');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Hero Association', 'hero-association', '68');
	INSERT INTO "MTServer"("gameSlug", "serverName", "serverSlug", "codashopIndex") VALUES('ragnarok-x-generation', 'Monster Association', 'monster-association', '69');

	'''
	op.execute(query)


def downgrade() -> None:
	query = 'DELETE FROM "MTServer"'
	op.execute(query)
