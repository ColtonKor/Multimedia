from PIL import Image

# Task 1
im = Image.open('recreated_image.png')
negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
im.putdata(negative_list)
im.save('recreated_image_negative.png')

ima = Image.open('recreated_image_negative.png')
double_negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in ima.getdata()]
ima.putdata(double_negative_list)
ima.save('recreated_image_double_negative.png')
#I just followed everything from the instructions. Except I used the new negative picture to negate it again. 
#When you negate the negated colors. They return back to the original colors.


imag = Image.open('recreated_image.png')
sunset_list = [(p[0], int(p[1] / 2), int(p[2] / 2)) for p in imag.getdata()]
imag.putdata(sunset_list)
imag.save('recreated_image_sunset.png')