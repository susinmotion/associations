#!/newEnv/bin/python
from flask import Flask

#NAME OF YOUR MODULE =...
app = Flask(__name__)

#talk to config object...not sure about naming here.
#app.config.from_object('config')
#from CONTAINING FOLDER OF this file import NAME OF THIS FILE
from flaskPlay import views

