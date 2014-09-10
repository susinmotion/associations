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

def experiment():
	thePic=choosePic()
	if thePic==None:
		return None
	displayPic(thePic)
	micRecord(thePic)
	time.sleep(5)
	closePic(thePic)
	if checkContinue():
		experiment()


global wordList
wordList=fileOpen()
#experiment()
#thePic=choosePic()+".jpg"



"""#def THE NAME OF THE THING AFTER THE SLASH--different page views
def index():
	user = { 'nickname': 'Miguel' } 
	posts = [ # fake array of posts
	{ 
	'author': { 'nickname': 'John' }, 
	'body': 'Beautiful day in Portland!' 
	},
	{ 
	'author': { 'nickname': 'Susan' }, 
	'body': 'The Avengers movie was so cool!' 
	}
	]
	# return render_template THE NAME OF THE FILE IN THE TEMPLATES FOLDER, VARIABLE NAMES AND VALUES
	return render_template("index.html",
		title = 'Home',
		user = user,
		posts = posts)

	from associations import app
@app.route('/')
@app.route('/index')"""

@app.route('/')
@app.route('/index')
#these include the data itself that could be part of the view. The html page controls how it looks and what gets shown

def index():
	thePic= choosePic()+".jpg"
	return render_template("index.html", thePic=thePic)


#these include the data itself that could be part of the view. The html page controls how it looks and what gets shown
#def THE NAME OF THE THING AFTER THE SLASH--different page views
