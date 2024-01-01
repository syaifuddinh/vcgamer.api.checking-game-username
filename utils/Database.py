from sanic import Sanic
import psycopg2
from psycopg2 import sql

def GetConfig():
	app = Sanic.get_app("CheckingGameApp")
	dbParams = {
		'dbname': app.config.db["name"],
		'user': app.config.db["username"],
		'password': app.config.db["password"],
		'host': app.config.db["host"],
		'port': app.config.db["port"]
	}

	return dbParams


def FetchFromQuery(rawQuery):
	dbConfig = GetConfig()
	# Construct your raw SQL query
	query = sql.SQL(rawQuery)
	results = []
	with psycopg2.connect(**dbConfig) as conn:
	# Create a cursor object
		with conn.cursor() as cursor:
		# Execute the query
			cursor.execute(query)

			# Fetch all the results
			results = cursor.fetchall()

	return results

def FirstFromQuery(rawQuery):
	dbResult = FetchFromQuery(rawQuery)
	result = None
	if len(dbResult) > 0:
		firstRow = dbResult[0]
		result = firstRow

	return result

def Execute(rawQuery):
	dbConfig = GetConfig()
	# Construct your raw SQL query
	query = sql.SQL(rawQuery)
	results = []
	with psycopg2.connect(**dbConfig) as conn:
	# Create a cursor object
		with conn.cursor() as cursor:
		# Execute the query
			cursor.execute(query)
