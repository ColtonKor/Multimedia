# Name: Colton Korhummel
# Class: Multimedia CST 205
# Date: 4/6/2025
# Description: This web app shows 3 random images from the dictionary and a link to the information of each one.
# When you click on the link it shows all of its information and then produces a link to go back to original page.

import random
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from image_info import image_info
from PIL import Image


app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
  Random_Image()
  return render_template('home.html', images = image_info)

@app.route('/image/<info>')
def image(info):
  for index in image_info:
    if index['id'] == info:
      im_inf = index
      break
  im = Image.open(f"static/images/{info}.jpg")
  return render_template('image.html', my_image = im_inf, width = im.width, height = im.height, mode = im.mode, format = im.format)

def Random_Image():
  random.shuffle(image_info)