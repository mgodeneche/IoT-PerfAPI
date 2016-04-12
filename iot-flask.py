# coding=UTF-8
from flask import Flask
from collections import deque
import time

app = Flask(__name__)
TOTAL_MESSAGE = 100000
global globalData = []
global globalDataOpti = collections.deque(maxlen=TOTAL_MESSAGE)
global globalIndex = collections.deque(maxlen=TOTAL_MESSAGE)

@app.route("/receiveMessage", methods=['POST'])
def receiveMessage():
	messageId = request.form['id']
	messageTS = request.form['timestamp']
	sensorType  = request.form['sensorType']
	sensorValue = request.form['value']
	if(alreadyExist(messageId)):
		return 0

	return 200
def receiveMessages():
	messageId,messageTS,sensorType,sensorValue = request.form['id'],request.form['timestamp'],request.form['sensorType'],request.form['value']
	if(alreadyExistOpti(messageId)):
		return 0
	return 200

@app.route("/messages/synthesis",methods=['GET']
def getSynthesis():
	return 0

def addDataToGlobalData(data):
	globalData.append(data)
	return 0

def addDataToGlobalDataOpti(data):
	globalDataOpti.append(data)
	return 0

def alreadyExist(messageId):
	#check existence dans l'index
	return False

def alreadyExistOpti(messageId):
	#check existence dans l'index opti
	return False

#Methode qui renvoie la liste des datas de la dernière heure afin de les traiter
def listLastHourSensorData(timestamp):
	return 0
#Construit le message JSON 
def buildSynthesis():
	return 0

if __name__ == "__main__":
	#app.run(threaded=True)
	#app.run(threaded=True,debug=True)
	app.run(debug=True)
