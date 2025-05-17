from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

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
   return render_template('template.html')