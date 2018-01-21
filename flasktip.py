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
#      print("   => " + line)
      # Clean up the numbers
      line = line.replace('$', '')
      # Break out of the loop once we reach subtotal
      if('subtotal' in line.lower() or 'sub-total' in line.lower() or 'sub total' in line.lower()):
         break
      # Add names of items into an array
      if(line[0].isdigit() and line[1] == ' '):
         print(line[2:-1])
         itemsName.append(line[2:-1])
      # Add prices of items into an array
      if(is_number(line)):
         print(float(line))
         itemsPrice.append(float(line))
   print()

   # After reaching subtotal, scan in the subtotal and tax
   while True:
       # Clean up the numbers
       line = line.replace('$', '')
#       print("THIS IS LINE: " + line)
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

   tax_percent= round(tax/subtotal*100,2)
   for item in itemsPrice:
      if item > subtotal:
         itemsPrice.remove(item)

   f.close()

   return render_template('text.html', subtotal=subtotal, tax=tax, tax_percent=tax_percent, items_price=itemsPrice, items_name=itemsName)
   

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




