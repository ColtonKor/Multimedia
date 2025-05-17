import random
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from dictionary import multimedia_info
from PIL import Image

#GitHub Link: https://github.com/ColtonKor/FlaskLab15

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)


# route decorator binds a function to a URL
@app.route('/')
def hello():
  return '''
    <h1>Hello world from Flask!</h1>
    <p>Aiden H. : lmao (Laugh My Ass Off)</p>
    <p>Nick S. : brb (Be Right Back)</p>
    <p>Daniel R. : smh (Shaking My Head)</p>
    <p>Caden T. : lol (Laugh Out Loud)</p>
    <p>Charlie B. : tbh (To Be Honest)</p>
    '''

@app.route('/template')
def t_test():
   return render_template('template.html', my_info = multimedia_info)

@app.route('/random')
def pillow():
   Random_Image()
   return render_template('random.html')



def Random_Image():
  image_files = ["static/chameleon.png", "static/Collage.png", "static/Sunset.png"]
  index = random.randint(0, 2)
  im = Image.open(image_files[index])
  negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
  im.putdata(negative_list)
  im.save('static/negative.png')