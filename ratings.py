"""Restaurant rating lister."""

import sys

file_name = open(sys.argv[1])

rates = {}

for line in file_name:
    line = line.rstrip()
    (key, value)= line.split(":") #splits into restuaturant and  rating 
    rates[key] = value

for key, value in sorted(rates.items()):
        print(f"{key} is rated at {value}.")

resturant_name = input("What is the resturant?>")
user_rating = input("What is your rating?>")

rates[resturant_name] = user_rating

for key, value in sorted(rates.items()):
        print(f"{key} is rated at {value}.")
 
    #print(sorted(words))
   
    #rates[words[0]] = int(words[1])


# for word in words:
#     rates[word] = rates.get(word, 0) + 1
 
 #for word, count in sorted(rates.items()):
    #print(f"{key} is rated at {value}.")
