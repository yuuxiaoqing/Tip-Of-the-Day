from flask import Flask
from flask import render_template, request
from werkzeug import secure_filename
import io
import os
app = Flask(__name__)
import fileinput

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
   return render_template('index.html')

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

   stringtext = ""
   f = open("receipt.txt", "w")
   print('Labels:')
   for label in labels:
      print(label.description)
      f.write(label.description)
      # stringtext+=label.description
   f.close()
   
   
   f = open('receipt.txt', 'r')
   itemsName = []
   itemsPrice = []
   subtotal = 0
   tax = 0
   line = ""
   
   # Scan the file
   for line in f:
      # Clean up the numbers
      line = line.replace('$', '')
      if('subtotal' in line.lower() or 'sub-total' in line.lower() or 'sub total' in line.lower()):
         break
      if(is_number(line)):
         print(line)
         itemsPrice.append(float(line))

   # After reaching subtotal, scan in the subtotal and tax
   while True:
       # Clean up the numbers
       line = line.replace('$', '')
   #    print("THIS IS LINE: " + line)
       if(is_number(line)):
           break
       print(line)
       line = next(f)
   subtotal = float(line)
   tax = float(next(f).replace('$', ''))

   # Printlines for testing
   print(itemsName)
   print(itemsPrice)
   print(subtotal)
   print(tax)

   f.close()

   return render_template('index.html')
   

#Gathered from here
#https://www.pythoncentral.io/how-to-check-if-a-string-is-a-number-in-python-including-unicode/
def is_number(s):
    foundDecimal = False
    for c in s:
        if(c == '.'):
            if(foundDecimal == False):
                foundDecimal = True
            else:
                return False
    if(foundDecimal == False):
        return False

    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False




