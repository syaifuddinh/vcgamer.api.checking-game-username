from utils import Database
from services.scraper.codashop import CodashopService
from services.scraper.codashop import LogService as CodashopLogService

from services.scraper.jollymax import JollymaxService
from services.scraper.jollymax import LogService as JollymaxLogService

from services.game import PipelineService

def Get(keyword = None, transactionStartDate = None, transactionEndDate = None, activityStatus = None):
	condition = ""
	if keyword is not None:
		condition += 'AND ("emailSource" ILIKE \'%' + keyword + '%\' '
		condition += 'OR "userGameId" ILIKE \'%' + keyword + '%\') '

	if transactionStartDate is not None or transactionEndDate is not None:
		condition += 'AND ('
		if transactionStartDate is not None and transactionEndDate is None:
			condition += '"transactionTime" >= \'' + transactionStartDate + '\''
		elif transactionStartDate is None and transactionEndDate is not None:
			condition += '"transactionTime" <= \'' + transactionEndDate + '\''
		elif transactionStartDate is not None and transactionEndDate is not None:
			condition += '"transactionTime" >= \'' + transactionStartDate + '\' AND "transactionTime" <= \'' + transactionEndDate + '\''

		condition += ') '

	if activityStatus is not None:
		condition += 'AND "activityStatus" = \'' + activityStatus + '\''


	query = f'''
		SELECT 
			"TRLog".id, 
			"emailSource", 
			"userGameId", 
			TO_CHAR("transactionTime", 'YYYY-MM-DD HH24:MI:SS') AS transactionTime,
			"activityStatus", 
			"userGameAvailabilityStatus",
			"MTGame".name as gameName
		FROM "TRLog"
		JOIN "MTGame"
		ON "MTGame".slug = "TRLog"."gameSlug"
		WHERE 1=1 {condition}
	''';
	dbResult = Database.FetchFromQuery(query);
	listData = [{
		"id": item[0],
		"emailSource": item[1],
		"userGameId": item[2],
		"transactionTime": item[3],
		"activityStatus": item[4],
		"userGameAvailabilityStatus": item[5],
		"gameName": item[6]
	} for item in dbResult]
	response = {
		"list": listData
	}

	return response