from PIL import Image
from math import sqrt
from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie2000 

#I used this function to place all three images onto a new image with the background of green.
def copy_image(your_first_image, your_second_image, your_third_image):
    my_first_src = Image.open(your_first_image)
    my_second_src = Image.open(your_second_image)
    my_third_src = Image.open(your_third_image)
    new_w, new_h = my_first_src.width + 500, my_first_src.height + 500
    my_trgt = Image.new('RGB', (new_w, new_h), (0,255,0))

    target_x = 0
    for source_x in range(my_first_src.width):
        target_y = 0
        for source_y in range(my_first_src.height):
            pixel = my_first_src.getpixel((source_x, source_y))
            my_trgt.putpixel((target_x, target_y), pixel)
            target_y += 1
        target_x += 1
    
    target_x = 300
    for source_x in range(my_second_src.width):
        target_y = 20
        for source_y in range(my_second_src.height):
            pixel = my_second_src.getpixel((source_x, source_y))
            my_trgt.putpixel((target_x, target_y), pixel)
            target_y += 1
        target_x += 1

    target_x = 100
    for source_x in range(my_third_src.width):
        target_y = 330
        for source_y in range(my_third_src.height):
            pixel = my_third_src.getpixel((source_x, source_y))
            my_trgt.putpixel((target_x, target_y), pixel)
            target_y += 1
        target_x += 1

    return my_trgt

#I used this function to find the color distance of the current pixel and the green screen
def color_distance(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2)

#I used this function to replace the green background with the background image
def chromakey(src, bg, refp):
   for x in range(src.width):
       for y in range(src.height):
           cur_pixel = src.getpixel((x,y))

           if color_distance(cur_pixel, refp) < 20:
               src.putpixel((x,y), bg.getpixel((x,y)))
      
   src.show()
   src.save('Collage.png')

# def color_distance(c1):
#     color1 = LabColor(lab_l=c1[0], lab_a=c1[1], lab_b=c1[2])
#     color2 = LabColor(lab_l=0, lab_a=255, lab_b=0)
#     delta_e = delta_e_cie2000(color1, color2)
#     return delta_e.item()

# def chromakey(src, bg, refp):
#    for x in range(src.width):
#        for y in range(src.height):
#            cur_pixel = src.getpixel((x,y))

#            if color_distance(cur_pixel) < 20:
#                src.putpixel((x,y), bg.getpixel((x,y)))
      
#    src.show()
#    src.save('Collage.png')


#I tried to complete task 3 using the delta_e_cie2000(color1, color2) I looked it up online and used ChatGPT to try an figure this out
#It keeps giving me a NumPy error and everything I find online never works. I don't know what to do to fix this I left my current code in
#as comments so you can see I tried to do it.

#I used this function to scale the background image up so I can use that for the chromakey
def scale(my_src, image):
    w, h = image.width, image.height
    my_trgt = Image.new('RGB', (w, h))
    
    x_ratio = my_src.width/w
    y_ratio = my_src.height/h

    for target_x in range(w):
        source_x = int(target_x * x_ratio)
        for target_y in range(h):
            source_y = int(target_y * y_ratio)
            p = my_src.getpixel((source_x, source_y))
            my_trgt.putpixel((target_x, target_y), p)

    return my_trgt

#Calls the functions to create the collage with the chroma key
image = copy_image('Tiger.png', 'Elephant.png', 'Parrot.png')
background = Image.open('Background.png')
background = scale(background, image)
chromakey(image, background, (0,255,0))