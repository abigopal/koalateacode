"""CLA model for midi music"""
from csv import reader
import datetime

from nupic.frameworks.opf.modelfactory import ModelFactory

import description

_ANOMALY_THRESHOLD = 0.8

def createModel():
	return ModelFactory.create(description.config)

def run():
	#Model Setup
	song_number = 10
	headers = ['pitch']
	model = createModel()
	model.enableInference({'predictedField': 'pitch'})
	#Read in file
	records = [record for record in reader(open('legdam10_parsed.txt'))]
	#Train CLA
	result = 0
	print "Training"
	for i in range(1, song_number +1):
		for(j, record) in enumerate(records):
			modelInput = dict(zip(headers, record))
			modelInput["pitch"] = float(modelInput["pitch"])
			result = model.run(modelInput)
			anamolyScore = result.inferences['anamolyScore']
			if anomalyScore > _ANOMALY_THRESHOLD:
       				_LOGGER.info("Anomaly detected at [%s]. Anomaly score: %f.",
                      		result.rawInput["timestamp"], anomalyScore)

if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  runHotgymAnomaly()
			f.close()
if __name__ == "__main__":
	run()
