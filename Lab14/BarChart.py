from PlainText import plain_text, stop_words
import matplotlib.pyplot as plt




words = plain_text.split()
stop_word_count = {} #I got the plain text and split it into words. I then make a dictionary which functions the same as a hashmap.
#I knew that I should use a hashmap because I have had many other classes that involve them.

stopped_words = []
for stop in stop_words: #Turns all of the stop words into lowercase so they will all be counted 
    stopped_words.append(stop.lower())

for word in words:
    if word.lower() in stopped_words: #I get each word then check if it is in the list of stop words
        if word in stop_word_count: #If it is it checks if it is already in the dictionary if so it adds a value to the count if not it gives a base value of 1
            stop_word_count[word.lower()] += 1
        else:
            stop_word_count[word.lower()] = 1

#I found this sorting for dictionary and and also how to limit it to 5. I know how to do this in java but not in python which is why I needed to find it
top_five = sorted(stop_word_count.items(), key=lambda x: x[1], reverse=True)[:5] 

five_words = [word for word, count in top_five] #I then made a list for each the words and the counts in from the dictionary so I could put them into the graph
five_counts = [count for word, count in top_five]


plt.bar(five_words, five_counts)
plt.title("Five Most Used Stop Words")
plt.ylabel("Times used") #I used the bar graph from the slides here
plt.xlabel("Stop Words")
plt.show()
