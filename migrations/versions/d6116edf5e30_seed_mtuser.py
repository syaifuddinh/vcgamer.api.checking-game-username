"""seed_mtuser

Revision ID: d6116edf5e30
Revises: d7cb498f9fbd
Create Date: 2023-12-21 20:40:53.229824

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from utils import Bcrypt
from utils import JWT
from utils import String


# revision identifiers, used by Alembic.
revision: str = 'd6116edf5e30'
down_revision: Union[str, None] = 'd7cb498f9fbd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

users = [
	"root@gmail.com",
	"admin@gmail.com",
	"master@gmail.com"
]

def upgrade() -> None:
    query = ""
    for email in users:
    	password = Bcrypt.Hash("12345678")
    	apiKey = String.Random(16)
    	query += f'''
    		INSERT INTO "MTUser" (fullname, email, password, "apiKey")
    		VALUES ('{email}', '{email}', '{password}', '{apiKey}');
    	'''
    op.execute(query)


def downgrade() -> None:
	def render(text):
		return "'" + text + "'"

	emails = map(render, users)
	dataset = ", ".join(emails)
	query = 'DELETE FROM "MTUser" WHERE email IN (' + dataset + ')'
	op.execute(query)
