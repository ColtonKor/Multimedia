# Name: Colton Korhummel
# Class: Multimedia CST 205
# Date: 3/10/2025
# Description: This file is used for searching for an Image with a Keyword from the image_info class and then passes the image if it found a match if not it returns a not found image.
# The file is also used to access and give the images the respective filter


from image_info import image_info
from PIL import Image

def my_search(search):
    max_hits = 0
    id = ''
    for img in image_info:
        current_hits = 0
        if search.lower() in img["title"].lower():
            current_hits += 1
        for tag in img["tags"]:
            if search.lower() in tag.lower():
                current_hits += 1
        if current_hits > max_hits:
            id = img["id"]
            max_hits = current_hits
    if id == '':
        id = 'no_results'
    return id



def filter(id, filterImage):
    my_src = Image.open(f"hw3_images/{id}.jpg")
    my_target = Image.new('RGB', my_src.size)
    if filterImage == "None" or id == "no_results":
        my_target = my_src
    elif filterImage == "Sepia":
        sepia_list = []
        
        for p in my_src.getdata():
            if p[0] < 63:
                r, g, b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
            elif 62 < p[0] < 192:
                r, g, b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
            else:
                r, g, b = int(p[0] * 1.08), p[1], int(p[2] * 0.5)

            sepia_list.append((min(r, 255), min(g, 255), min(b, 255)))

        my_target.putdata(sepia_list)
    elif filterImage == "Negative":
        negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in my_src.getdata()]
        my_target.putdata(negative_list)
    elif filterImage == "Grayscale":
        gray_list = [((a[0]+ a[1] + a[2])//3,) * 3 for a in my_src.getdata()]
        my_target.putdata(gray_list)
    elif filterImage == "Thumbnail":
        w = my_src.width//2
        h = my_src.height//2
        target = Image.new('RGB', (w, h))
        
        x_ratio = my_src.width/w
        y_ratio = my_src.height/h

        for target_x in range(w):
            source_x = int(target_x * x_ratio)
            for target_y in range(h):
                source_y = int(target_y * y_ratio)
                p = my_src.getpixel((source_x, source_y))
                target.putpixel((target_x, target_y), p)

        target.save("gui_image.jpg")
        return
    my_target.save("gui_image.jpg")