class PipelineService:
	queues = []

	def __init__(self):
		self.queues = [] 

	def Push(self, key, isAllowed, function):
		params = {
			"key": key,
			"isAllowed": isAllowed,
			"function": function
		}

		self.queues.append(params)

	def Run(self):
		trying = 0
		response = None
		for index, value in enumerate(self.queues):
			if(value["isAllowed"] == True):
				try:
					response = value["function"]()
					trying += 1
				except:
					print(value["key"] + " is fail")


			if(trying > 0):
				break

		return response