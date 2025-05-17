import pickle


my_list = []
for x in range(2):
    for y in range(4,0,-2):
        my_list.append((x,y))
print(my_list)

# Task 4
try:
    with open("reminders.txt", 'rb') as my_file:
        ReminderList = pickle.load(my_file)
except (FileNotFoundError, EOFError): #Opens reminder file to see if it already has reminders. If not makes a new list. If it does all into the list
    ReminderList = []

if ReminderList:
    print("Your reminders:")
    for reminder in ReminderList: #Prints all reminders if there are none it says No Reminders
        print(f"{reminder}")
else:
    print("No reminders.")


# Task 1
with open("tarantella.txt") as file:
    lines = file.readlines() #Reads all of the lines of the file

print(f"The file has {len(lines) - 1} lines.") #Prints the lines minus 1 for the title

# Task 2
with open("tarantella.txt") as file: #Reads the file 
    words = file.read()

words = words.split() #Splits file into words
print(f"The file has {len(words) - 1} words.") # Calculates the words minus 1 for the title

# Task 3
Reminder = "y"
while(True):
    x = input("Enter a reminder. (Enter 'n' if done.): ") #This makes it so the user can input any reminder if they put n it exits
    if x == "n":
        break
    else:
        ReminderList.append(x)
    
with open('reminders.txt', 'wb') as my_file: #This puts all the reminders into the file overwriting what was there
    pickle.dump(ReminderList, my_file)

# Task 4
print("Here are your reminders:") 
for r in ReminderList: # This prints out the reminders of you have
    print(r)

