# from CONTAINING FOLDER OF RUN.PY import MODULE NAMED BELOW
from flaskPlay import app
from flask import render_template
import random, time
from PIL import Image




#from psychopy import microphone, sound, core

"""def micRecord(aPic):
	microphone.switchOn(sampleRate=48000,outputDevice=None, bufferSize=None)
	#raw_input('press a key to continue')
	mic = microphone.AdvAudioCapture()
	mic.record(5, filename=aPic,block=False)
	print 'recording'
"""
#opens the file containing the list of words and uses it to populate a list, which it returns
def fileOpen():
	filename='wordList'
	f=open(filename,'r')
	returnList=f.read().split()
	return returnList

#selects a word randomly from the word list, removes it from the list, and returns the word.
def choosePic():
	if not wordList:
		return None
	else:
		thisWord=(random.choice(wordList))
		wordList.remove(thisWord)
		return thisWord

def displayPic(aPic):
	aPic=aPic
	try:
		imageShown = Image.open("images/" + aPic +".jpg")
	except:
		print "unable to load image"
	print aPic
	#sound.Sound(value=aPic+".wav", secs=2,sampleRate=44100, bits=16,  name='', autoLog=True)

def checkContinue():
	image.open('checkContinue.jpg')

def closePic(aPic):
	aPic=aPic+'.jpg'
#	if os.path.exists(aPic)
	image.close(aPic)	

"""def experiment():
	thePic=choosePic()
	if thePic==None:
		return None
	displayPic(thePic)
	micRecord(thePic)
	time.sleep(5)
	closePic(thePic)
	if checkContinue():
		experiment()"""


global wordList, thePic
wordList=fileOpen()
thePic=choosePic()
#experiment()
#thePic=choosePic()+".jpg"



"""#def THE NAME OF THE THING AFTER THE SLASH--different page views"""

@app.route('/')
@app.route('/index')
#these include the data itself that could be part of the view. The html page controls how it looks and what gets shown

def index():
	if thePic != None:
		return render_template("index.html", thePic=thePic)
	else:
		return render_template("done.html")

@app.route('/areyouready')

def areyouready():
	return render_template("areyouready.html", thePic=  thePic)


@app.route('/gopicrecordcantremember12341234630fje')
def go():
	return render_template("record.html")

@app.route('/norecord')
def norecord():
	return render_template("audioerror.html")
#these include the data itself that could be part of the view. The html page controls how it looks and what gets shown
#def THE NAME OF THE THING AFTER THE SLASH--different page views
