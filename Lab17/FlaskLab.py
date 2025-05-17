import random
from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from PIL import Image
from datetime import datetime


# create an instance of Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

class Playlist(FlaskForm):
    song_title = StringField(
        'Song Title', 
        validators=[DataRequired()]
    )
    artist_name = StringField(
        'Name of Artist', 
        validators=[DataRequired()]
    )
    genre = StringField(
        'Genre', 
        validators=[DataRequired()]
    )

playlist = []

def store_song(my_song, my_artist, my_genre):
    playlist.append(dict(
        song = my_song,
        genre = my_genre,
        artist = my_artist,
        date = datetime.today()
    ))

# route decorator binds a function to a URL
@app.route('/', methods=('GET', 'POST'))
def index():
    form = Playlist()
    if form.validate_on_submit():
        store_song(form.song_title.data, form.artist_name.data, form.genre.data)
        return redirect('/view_playlist')
    return render_template('home.html', form=form)

@app.route('/view_playlist')
def vp():
    return render_template('vp.html', playlist=playlist)