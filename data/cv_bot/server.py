import bottle
import ConfigParser
import pytesseract
import os
from PIL import Image
import time

"""
	LOAD CONFIGURATIONS
	
	EXAMPLE:

	[self]
	host = 0.0.0.0
	port = 8080
	max_file_size = 1048576
	wait_time = 0.005
	timeout = 4

"""

cp = ConfigParser.ConfigParser()
conf = cp.read("config")

HOST = cp.get("self", "host")
PORT = cp.get("self", "port")
MAX_FILE_SIZE = cp.get("self", "max_file_size")
WAIT_TIME = cp.getfloat("self", "wait_time")
TIMEOUT = cp.getint("self", "timeout")

"""

	BOTTLE APPLICATION DEFINITION
		* Setting MAX UPLOAD SIZE to MAX_FILE_SIZE (defined in conf)
"""

app = bottle.Bottle()
bottle.BaseRequest.MEMFILE_MAX = MAX_FILE_SIZE

#	ROUTES	#####################################################################
# 	insert custom routes here													#
#################################################################################

"""
	OCR SERVICE
	URL : localhost:PORT/ocrservice

	IN  --> POST request with image
	OUT <-- the string set result of OCR analysis

"""

@app.route('/ocrservice', method="POST")
def ocr_analysis():
	
	waiting = 0
	
	upload = bottle.request.files.get('image')
	upload.save("uploads/" + upload.filename)

	while not os.path.isfile(upload.filename):
		time.sleep(WAIT_TIME)
		waiting += WAIT_TIME

		if waiting > TIMEOUT:
			# CONNECTION TIMEOUT
			bottle.response.status = 409 
			return "Took too long to analyse image. TIMEOUT=%s" % TIMEOUT
			
	image = Image.open(upload.filename)
	return pytesseract.image_to_string(image)

"""
	SPLASH PAGE
	URL : localhost:PORT/

	IN  --> GET request 
	OUT <-- some HTML or text welcome response
	
"""

@app.route('/')
def home():
	return "connected to CV-Bot"


#	RUN APPLICATION ############################################################
app.run(host=HOST, port=PORT, reloader=True, debug=True)