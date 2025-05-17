from PIL import Image
from colorthief import ColorThief
import numpy as np
import math

def patch_asscalar(a):
    return a.item()

setattr(np, "asscalar", patch_asscalar)

# Task 1
im = Image.open('chameleon.png')
gray_list = [((a[0]+ a[1] + a[2])//3,) * 3 for a in im.getdata()]
im.putdata(gray_list)
im.save('grayscale_average_chameleon.png')

#Task 2
im2 = Image.open('chameleon.png')
gray_list_lum = [((int((a[0]*.299) + (a[1]*.587) + (a[2]*.114)),) * 3) for a in im2.getdata()]
im2.putdata(gray_list_lum)
im2.save('grayscale_luminosity_chameleon.png')

#Task 3
color_thief = ColorThief('chameleon.png')
dominant_color = color_thief.get_color(quality=1)
print(f"The dominant color: {dominant_color}")
image = Image.open('chameleon.png')
pixels = list(image.getdata())
dominant_count = pixels.count(dominant_color) # I couldn't get this to work. I get the dominant color but when I do this to find the count 
print(f"The dominant color count: {dominant_count}") # No matter what I do it prints the count is 0

#Task 4
apple1_rgb = (176, 63, 81)
apple2_rgb = (185, 77, 89)

lab = math.sqrt(math.pow(apple1_rgb[0] - apple2_rgb[0], 2) + math.pow(apple1_rgb[1] - apple2_rgb[1], 2) + math.pow(apple1_rgb[2] - apple2_rgb[2], 2))
print(f"L*a*b of the apples: {lab}")

#Task 5
def color_distance(c1, c2):
    r_diff = (c1[0] - c2[0])**2
    g_diff = (c1[1] - c2[1])**2
    b_diff = (c1[2] - c2[2])**2
    return (r_diff + g_diff + b_diff)**(1/2)

def color_distance2(c1, c2):
  val = 0
  for i in range(3):
      val += math.pow((c1[i]-c2[i]), 2)
    
  return math.sqrt(val)

distance1 = color_distance(apple1_rgb, apple2_rgb)
distance2 = color_distance2(apple1_rgb, apple2_rgb)

print(f"Apple Color distance using color_distance: {distance1}")
print(f"Apple Color distance using color_distance2: {distance2}")
# If you compare the Euclidean Color distance and the L*a*b* color distance they end up being the same. When you run this program all three give the same response
# They are also very similar in structure like distance2 you are still powering the values and square rooting them. Distance 1 is timesing the values by two
# Then we add them together and multiply them by 1/2.