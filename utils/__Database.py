from sanic import Sanic
import psycopg2
from psycopg2 import sql
import os

def GetConfig():
	dbParams = {
		'dbname': os.environ.get('DB_NAME'),
		'user': os.environ.get('DB_USER'),
		'password': os.environ.get('DB_PASSWORD'),
		'host': os.environ.get('DB_HOST'),
		'port': os.environ.get('DB_PORT')
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
