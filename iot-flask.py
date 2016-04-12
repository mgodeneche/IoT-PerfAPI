# coding=UTF-8
from flask import Flask
from collections import deque
import time

app = Flask(__name__)
global globalData = []
global globalDataOpti = collections.deque(maxlen=100000)

@app.route("/receiveMessage", methods=['POST'])
def receiveMessage():
	messageId = request.form['id']
	messageTS = request.form['timestamp']
	sensorType  = request.form['sensorType']
	sensorValue = request.form['value']
	return 200
def receiveMessages():
	messageId,messageTS,sensorType,sensorValue = request.form['id'],request.form['timestamp'],request.form['sensorType'],request.form['value']
	return 200

@app.route("/messages/synthesis",methods=['GET']
def getSynthesis():
	return 0

def addDataToGlobalData(data):
	globalData.append(data)
	return 0

def addDataToGlobalDataOpti(data):
	globalDataOpti.append(data)

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
