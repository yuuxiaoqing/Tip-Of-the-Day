from flask import Flask
from flask import render_template, request
from werkzeug import secure_filename
import io
import os
app = Flask(__name__)
import fileinput
import random

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
   isReceipt2 = False

   # Scan the file
   for line in f:
      if("WOODIES CAFE" in line):
         isReceipt2 = True
   #   print("   => " + line)
      # Clean up the numbers
      line = line.replace('$', '')
      if(line[0] == ':'):
         line = line.replace(':', '')
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
   while isReceipt2 == False:
       # Clean up the numbers
       line = line.replace('$', '')
   #    print("THIS IS LINE: " + line)
       if(is_number(line)):
           break
       print(line)
       line = next(f)
   if(isReceipt2 == False):
      subtotal = float(line)
      tax = float(next(f).replace('$', ''))

   if(isReceipt2 == True):
      subtotal = itemsPrice[2]
      tax = itemsPrice[3]
      del itemsPrice[2:]

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
   randtip=random.randint(0, len(tips_of_the_day)-1)
   return render_template('text.html', subtotal=round(subtotal,2), tax=round(tax,2), tax_percent=round(tax_percent,2), items_price=itemsPrice, items_name=itemsName, tips_of_the_day=tips_of_the_day[randtip])
   

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

tips_of_the_day = ['"Feeling tipsy?"',
   '"This is just the tip of the iceberg."',
   '"If you fear change, leave it in the tip jar."',
   '"Money is the root of all evil. Cleanse yourself here!"',
   '"We knead the dough!"',
   "If you need to look up to see the menu, you're probably in a restaraunt where you don't need to pay a tip.",
   "Places like cafes, sit-down restaraunts, and hair dressers require tips (so don't leave without paying one!)",
   "Tips are generally between 10 and 20 percent of the cost of what you purchased (before tax)."
]
