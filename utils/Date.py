from datetime import datetime

def Now():
	currentDatetime = datetime.now()
	formattedDatetime = currentDatetime.strftime("%Y-%m-%d %H:%M:%S")

	return formattedDatetime
