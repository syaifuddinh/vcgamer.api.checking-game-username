from sanic.response import json
from utils import Database
from services.game import LogService 
from flask import Flask, jsonify, request

def GetLog():
	data = None
	keyword = request.args.get("keyword")
	transactionStartDate = request.args.get("transactionStartDate")
	transactionEndDate = request.args.get("transactionEndDate")
	activityStatus = request.args.get("activityStatus")
	data = LogService.Get(
		keyword=keyword,
		transactionStartDate=transactionStartDate,
		transactionEndDate=transactionEndDate,
		activityStatus=activityStatus
	)
	return jsonify({
		"status": 200,
		"message": None,
		"data": data
	})
