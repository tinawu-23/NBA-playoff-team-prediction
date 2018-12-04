class Evaluation:
	def __init__(self, predictions, actual):
		self.confusion_matrix = self.getConfusionMatrix(predictions, actual)
		self.TP = self.confusion_matrix[0][0]
		self.TN = self.confusion_matrix[1][1]
		self.FP = self.confusion_matrix[1][0]
		self.FN = self.confusion_matrix[0][1]

	def getConfusionMatrix(self, predictions, actual):
		confusion_matrix = [[0,0],[0, 0]]
		for index, prediction in enumerate(predictions):
			if actual[index] == "Y": #
				if actual[index] == prediction: #TP
					confusion_matrix[0][0] += 1
				else:
					confusion_matrix[0][1] += 1 #FN
			else: #it is actually N
				if actual[index] == prediction: #TN
					confusion_matrix[1][1] +=1
				else:
					confusion_matrix[1][0] += 1 #FP
		return confusion_matrix

	def getAccuracy(self):
		return (self.TP + self.TN )/(self.TP + self.TN + self.FP + self.FN)

	def getPrecision(self):
		if (self.TP + self.FP) == 0:
			return 0
		return self.TP /(self.TP + self.FP)

	def getRecall(self):
		if (self.TP + self.FN) ==0:
			return 0
		return self.TP / (self.TP + self.FN)

	def getF1(self):
		precision = self.getPrecision()
		recall = self.getRecall()
		if precision + recall ==0:
			return 0
		return (2 * precision * recall) / (precision + recall)
