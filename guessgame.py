# guess game
# 
# first choose a random string from list
# then shuffle the string
# then show the user the shuffled string and start timer
# user should guess
# when user's guess is correct show the guess time

import random
import time

file = open("boun.list.txt",'r')
file2 = open("boun.list.txt",'r')
randomNum = random.randint(0,25000)
str = ''
newStr = '' 
inStr = ''
ind = 0


for line in file:
	if ind == randomNum:
		str = line
	ind += 1
str = str[:-1]
newStr = "".join(random.sample(str, len(str)))
# print(str) # for debugging purposes, if you want to play the game fair and square do not uncomment this line
print ("Guess the word!")
print (newStr)
start = time.time()
found = True
while (found):
	inStr = raw_input("Enter a word (Write 'Lemme cheat' to cheat): ")
	if(inStr == str):
		end = time.time()
		print("You found it!")
		print("{} {} {}".format("You've find the word in ", end-start,"seconds!"))
		found = False
