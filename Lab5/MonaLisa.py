from PIL import Image

#Task 1
with open("rgb.txt") as file:
    lines = file.readlines() #Reads the file

width = len(lines[0].split())
height = len(lines) #Splits the lines so we get the width and uses lines to get height

rgb_tuples = []
for line in lines:
    line = line.replace("(", "").replace(")", "") #This removes the Parentheses from the each line.
    values = line.split() #Splits all the lines so it is each one formatted like x,y,z
    for value in values:
        r, g, b = map(int, value.split(",")) #Uses the split to split the ,'s and puts each value into rgb values
        rgb_tuples.append((r, g, b)) #Adds the rgb tuple to the array.

image = Image.new("RGB", (width, height))
image.putdata(rgb_tuples) #Puts image information

image.show()
image.save("recreated_image.png") #Shows/Saves the image



#Task 2
with open('mona_lisa.txt') as file:
    pixel_lines = file.readlines() #Reads the file as lines

width = len(pixel_lines[0].split())
height = len(pixel_lines) #Splits the lines so we get the width and uses lines to get height

pixels = []
for line in pixel_lines:
    values = line.split() #Splits each line into list of numbers
    for value in values:
        pixels.append(int(value)) #Adds the value of each number from each line into the pixels.

img = Image.new('L', (width, height))
img.putdata(pixels) #Puts the information into the image

img.show()
img.save("mona_lisa.png") #Shows and saves the image