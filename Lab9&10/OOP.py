#Task 1
#The class definition for Image starts on line 533

#Task 2
#The docstring for the Image class is located at 534-543
#     """
#     This class represents an image object.  To create
#     :py:class:`~PIL.Image.Image` objects, use the appropriate factory
#     functions.  There's hardly ever any reason to call the Image constructor
#     directly.

#     * :py:func:`~PIL.Image.open`
#     * :py:func:`~PIL.Image.new`
#     * :py:func:`~PIL.Image.frombytes`
#     """

#Task 3
from PIL import Image

image = Image.open("Sunset.png")

attributes = dir(image)
# print(attributes)

quantized_image = image.quantize(colors=64, method=Image.Quantize.FASTOCTREE)
quantized_image.save("Sunset_quantized.png")


#I am choosing the quantize attribute to talk about

#You use Quantize to reduce the amount of colors in the image. Depending on the number you put in the function
#it makes that the number of colors in the image. The value you put needs to be over 0 but under 257 so a range of 1-256
#You then choose between different ways to choose which color is saved.
#They are called Quantize.MEDIANCUT, Quantize.MAXCOVERAGE, Quantize.FASTOCTREE, Quantize.LIBIMAGEQUANT
#FASTOCREE barely changed the image but it made the background behind the tree visibly different 

#Task 4
class Song():
    """This class simulates songs"""

    def __init__(self, title, artist, length, genre, album):
        self.title = title
        self.artist = artist
        self.length = length
        self.genre = genre
        self.album = album

    def __str__(self):
        return f"{self.artist} made a song titled {self.title}, it is {self.length} minutes and the genre is {self.genre}. It is apart of the {self.album} album."

    def __eq__(self, other):
        return self.artist == other.artist and self.title == other.title and self.length == other.length and self.genre == other.genre and self.album == other.album


class SongSnippet(Song):
    """This class simulates song snippets"""

    def __init__(self, title, artist, length, genre, album, monetized):
       super().__init__(title, artist, length, genre, album)
       self.monetized = monetized

    def __str__(self):
        return f"{self.artist} made a song titled {self.title}, it is {self.length} minutes and the genre is {self.genre}. It is apart of the {self.album} album. Monetized Status: {self.monetized}"

    def __eq__(self, other):
        return self.artist == other.artist and self.title == other.title and self.length == other.length and self.genre == other.genre and self.album == other.album and self.monetized == other.monetized


first_object = Song("Bohemian Rhapsody", "Queen", "5:55", "Rock", "A Night at the Opera")

second_object = Song("Blinding Lights", "The Weeknd", "3:20", "Synthwave / R&B", "After Hours")

third_object = Song("Billie Jean", "Michael Jackson", "4:54", "Pop", "Thriller")

print(first_object)

print(second_object)

print(third_object)

print(first_object == second_object)


Song_Snippet1 = SongSnippet("Lose Yourself", "Eminem", 30, "Hip-Hop", "8 Mile", False)

Song_Snippet2 = SongSnippet("Shape of You", "Ed Sheeran", 20, "Pop", "Divide", True)

print(Song_Snippet1)

print(Song_Snippet2)

print(Song_Snippet1 == Song_Snippet2)


# The MyWidget Subclass inherits from the QtWidgets.QWidget class