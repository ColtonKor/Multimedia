#Task 4
def task4():
    x = int(input("Enter red: "))
    y = int(input("Enter green: ")) #This gathers the inputs for the three color values.
    z = int(input("Enter blue: "))

    print(f"Thank you, your RGB color is ({x}, {y}, {z})") #This prints out the color values.

#Task 5
def task5(color):
    print(f"The red channel intensity is: {color[0]}")
    print(f"The green channel intensity is: {color[1]}") #This prints the three values of the tuple so it shows the color.
    print(f"The blue channel intensity is: {color[2]}")

#Task 6
def task6(color):
    hex = "#{:02X}{:02X}{:02X}".format(color[0], color[1], color[2]) #Turns rgb to hex
    print(f"The hexadecimal value of {color} is {hex}")

#Task 7
def task7(hex):
    hexa = hex.lstrip("#")
    rgb = (int(hexa[0:2], 16), int(hexa[2:4], 16), int(hexa[4:6], 16)) #Turns hex value to RGB tuple
    print(f"The RGB tuple of {hex} is {rgb}")

#Task 1
color_dictionary = {
    "green" : (0,255,0),
    "blue" : (0,0,255), #The dictionary of the 4 colors I input.
    "magenta" : (255,0,255),
    "black" : (0,0,0)
}

#Task 2
print("Task 2: ")
print(f"The green channel of the color green is {color_dictionary['green'][1]}")
print(f"The blue channel of the color blue is {color_dictionary['blue'][2]}") #These lines just print the channel values of the color in the dictionary.
print(f"The green channel of the color black is {color_dictionary['black'][1]}")
print(f"The blue channel of the color magenta is {color_dictionary['magenta'][2]}")
print(f"The red channel of the color magenta is {color_dictionary['magenta'][0]}")



#Task 3
tineye_sample = {
    "status": "ok",
    "error": [],
    "method": "extract_collection_colors",
    "result": [
        {
            "color": (141,125,83),
            "weight": 76.37, #Dictionary imported from the assignment handout
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        },
        {
            "color": (35,22,19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
        }
    ]
}

print("Task 3: ")
print(f"The red channel of the color clay creek is {tineye_sample['result'][0]["color"][0]}")#Prints the color channel of the imported dictionary

print("Task 4: ")
task4() #Calls the task4 function

print("Task 5: ")
task5((155,255,12)) #Calls the task5 function

print("Task 6: ")
task6((155,255,12)) #Calls the task6 function

print("Task 7: ")
task7("#9BFF0C") #Calls the task7 function
