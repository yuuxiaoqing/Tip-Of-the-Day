from flask import Flask
from flask import render_template, request
from werkzeug import secure_filename
import io
import os
app = Flask(__name__)

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
def hello_world():
   return 'Hello, World!'
   
@app.route('/hello')
def hello():
   print("so this works")
   return render_template('index.html')
	
@app.route('/uploader')
@app.route('/uploader/<photo>', methods = ['GET', 'POST'])
def upload_file(photo):
   print("recieved POST")
   f = request.files['file']
   #f.save(secure_filename(f.filename))
   
   # The name of the image file to annotate
   file_name = os.path.join(
      os.path.dirname(__file__),
      secure_filename(f.filename))
   # Loads the image into memory
   with io.open(file_name, 'rb') as image_file:
      content = image_file.read()

   image = types.Image(content=content)

   # Performs label detection on the image file
   response = client.text_detection(image=image)
   labels = response.text_annotations

   print('Labels:')
   for label in labels:
      print(label.description)
   return 'file uploaded successfully'



@app.route('/upload', methods=['POST'])
def upload_photo():
   file = request.files['image']
   f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
   file.save(f)
   with io.open(f, 'rb') as image_file:
      content = image_file.read()
   
   image = types.Image(content=content)

   # Performs label detection on the image file
   response = client.text_detection(image=image)
   labels = response.text_annotations

   print('Labels:')
   for label in labels:
      print(label.description)
   return 'file uploaded successfully'
   # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
   file.save(f)

   return render_template('index.html')
