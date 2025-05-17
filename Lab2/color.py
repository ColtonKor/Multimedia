color_list = [ (227, 66, 52), (205, 96, 144), (28, 134, 238), (72, 209, 204), (237, 145, 33), (250, 250, 70), (245, 50, 245), (100, 231, 231)]

for color in color_list:
    print(f"RGB values: ({color[0]}, {color[1]}, {color[2]})")
    if color[0] > color[1] and color[0] > color[2]:
        print('The color is reddish')
    elif color[1] > color[0] and color[1] > color[2]:
        print('the color is greenish')
    elif color[2] > color[0] and color[2] > color[1]:
        print('the color is blueish')
    elif color[0] == color[1] and color[0] > color[2]:
        print("The color is a shade of yellow")
    elif color[0] == color[2] and color[0] > color[1]:
        print("The color is a shade of magenta")
    elif color[1] == color[2] and color[1] > color[0]:
        print("The color is a shade of cyan")

