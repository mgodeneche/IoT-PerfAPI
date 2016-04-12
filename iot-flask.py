# coding=UTF-8
from flask import Flask
from collections import deque
import time

app = Flask(__name__)
TOTAL_MESSAGE = 100000
globalData = deque(maxlen=TOTAL_MESSAGE)
globalIndex = deque(maxlen=TOTAL_MESSAGE)


@app.route("/receiveMessage", methods=['POST'])
def receiveMessage():
	messageId,data = request.form['id'],[request.form['id'],request.form['timestamp'],request.form['sensorType'],request.form['value']
	if(alreadyExist(messageId)):
		return 202
	addDataToGlobalData(data)
	return 201

@app.route("/messages/synthesis",methods=['GET'])
def getSynthesis():
	for(item in globalData):

		

def addDataToGlobalData(data):
	globalDataOpti.append(data)
	globalIndex.append(data.messageId)
	return True

def alreadyExist(messageId):
	if(messageId in globalIndex):
		return True
	return False

#Methode qui renvoie la liste des datas de la dernière heure afin de les traiter
def listLastHourSensorData(timestamp):
	return 0
#Construit le message JSON 
def buildSynthesis():
	return 0

def getAllAggregations():
	allAggregations = []
	for sensorTypeId in globalData:
		allAggregations.append(getAllMessagesFromSensorType)
		#todo : min / max / moy

def getAllMessagesFromSensorType(sensorTypeId):
	sensorTypeAggregation = []
	for item in globalData:
		if(item['sensorType']==sensorTypeId):
			sensorTypeAggregation.append(item)
	return sensorTypeAggregation

if __name__ == "__main__":
	#app.run(threaded=True)
	#app.run(threaded=True,debug=True)
	app.run(debug=True)
