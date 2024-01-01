"""seed_mtadditionalfield

Revision ID: ccfa6c522b41
Revises: f7b0905605d3
Create Date: 2023-12-19 11:21:21.370350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ccfa6c522b41'
down_revision: Union[str, None] = 'f7b0905605d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
    	INSERT INTO "MTAdditionalField" ("gameSlug", "additionalField", "additionalFieldType", "additionalFieldLabel") VALUES ('mobile-legends', 'zoneId', 'TEXT', 'Zone ID');
		INSERT INTO "MTAdditionalField" ("gameSlug", "additionalField", "additionalFieldType", "additionalFieldLabel") VALUES ('one-punch-man-the-strongest', 'serverId', 'TEXT', 'Server ID');
		INSERT INTO "MTAdditionalField" ("gameSlug", "additionalField", "additionalFieldType", "additionalFieldLabel") VALUES ('scroll-of-onymyoji', 'serverName', 'TEXT', 'Server Name');
		INSERT INTO "MTAdditionalField" ("gameSlug", "additionalField", "additionalFieldType", "additionalFieldLabel") VALUES ('idle-legends-god-saga', 'serverName', 'TEXT', 'Server Name');
		INSERT INTO "MTAdditionalField" ("gameSlug", "additionalField", "additionalFieldType", "additionalFieldLabel") VALUES ('genshin-impact', 'serverId', 'OPTIONS', 'Server ID');
		INSERT INTO "MTAdditionalField" ("gameSlug", "additionalField", "additionalFieldType", "additionalFieldLabel") VALUES ('honkai-star-rail', 'serverId', 'OPTIONS', 'Server ID');
		INSERT INTO "MTAdditionalField" ("gameSlug", "additionalField", "additionalFieldType", "additionalFieldLabel") VALUES ('eggy-party', 'serverId', 'OPTIONS', 'Server ID');
		INSERT INTO "MTAdditionalField" ("gameSlug", "additionalField", "additionalFieldType", "additionalFieldLabel") VALUES ('ragnarok-eternal-love', 'serverId', 'OPTIONS', 'Server ID');
		INSERT INTO "MTAdditionalField" ("gameSlug", "additionalField", "additionalFieldType", "additionalFieldLabel") VALUES ('life-after', 'serverId', 'OPTIONS', 'Server ID');
		INSERT INTO "MTAdditionalField" ("gameSlug", "additionalField", "additionalFieldType", "additionalFieldLabel") VALUES ('ragnarok-x-generation', 'serverId', 'OPTIONS', 'Server ID');
    ''')


def downgrade() -> None:
    op.execute('DELETE FROM "MTAdditionalField"')
