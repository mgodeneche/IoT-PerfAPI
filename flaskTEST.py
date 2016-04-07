# coding=UTF-8
from flask import Flask
import time

STRING = "abcedfgijklmnop"
NBTRY = 100000

app = Flask(__name__)

@app.route("/")
def hello():
	startTime = start()
	perfTest(NBTRY)
	duration = stop(startTime)
	return duration;

@app.route("/receiveMessage")
def receiveMessage():
	return 0

def sendResponde():
	return 0


def start():
	start = time.time()
	return start;

def stop(startTime):
	stopTime = time.time()
	result = stopTime - startTime
	return chronoCalc(result)
	

def chronoCalc(timer):
	strTimer = str(timer)
	timer = int(timer)
	hours = timer/3600
	minsLeft=timer%3600
	mins = minsLeft/60
	secsLeft=minsLeft%60
	#récupère les millièmes de secondes
	milliSec = strTimer.split('.')[1][0:3]
	varTime = "Temps execution : "+str(hours)+"h "+str(mins)+"min "+str(secsLeft)+"secondes "+str(milliSec)+"ms"
	return varTime

def perfTest(tries):
	for i in range(tries):
		STRING2 = STRING+str(i)
		#print STRING2

if __name__ == "__main__":
	app.run(threaded=True)


