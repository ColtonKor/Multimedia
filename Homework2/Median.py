"""
Name: Colton Korhummel
Date: 02/20/2025
Class: Multimedia Programming, CST 205.
"""
from PIL import Image
from glob import glob

img_list = []

def load_images(location, type):
    for image in glob(f'{location}/*.{type}'):
        img_list.append(Image.open(image))

def my_median(num_list):
    num_list.sort()
    m = (len(num_list)) // 2
    return num_list[m]


def new_image(images):
    length = len(images)
    width = images[0].width
    height = images[0].height

    pixels = [img.getdata() for img in images]
    new_image = Image.new("RGB", (width, height))
    new_pixels = new_image.load()

    for x in range(width):
        for y in range(height):
            index = y * width + x
            r = [pixels[i][index][0] for i in range(length)]
            g = [pixels[i][index][1] for i in range(length)]
            b = [pixels[i][index][2] for i in range(length)]
            median_r = my_median(r)
            median_g = my_median(g)
            median_b = my_median(b)

            new_pixels[x, y] = (median_r, median_g, median_b)
    return new_image



# Task 1 - Test my_median function
temp_list1 = [2, 2, 2]
temp_list2 = [3, 1, 2]
temp_list3 = [3, 1, 2, 150, 59, 24, 23]
print(f"Median Test 1: {my_median(temp_list1)}")
print(f"Median Test 2: {my_median(temp_list2)}")
print(f"Median Test 3: {my_median(temp_list3)}")

# Task 2
load_images('task2_images', 'png')
median_image = new_image(img_list)
median_image.save('task2.png')
median_image.show()

#Shows the RGB for each pixel of the image
pixels = list(median_image.getdata())
for x in range(len(pixels)):
    r = pixels[x][0]
    g = pixels[x][1]
    b = pixels[x][2]
    print(f"RGB Pixel {x}: ({r}, {g}, {b})")
img_list = []

# Task 3
load_images('task3_images', 'png')
median_image = new_image(img_list)
median_image.save('task3.png')
median_image.show()