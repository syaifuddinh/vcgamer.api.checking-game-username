from sanic import Sanic
import psycopg2
from psycopg2 import sql
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

def FetchFromQuery(rawQuery):
	command = text(rawQuery)
	result = db.session.execute(command)
	rows = result.fetchall()

	return rows

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
