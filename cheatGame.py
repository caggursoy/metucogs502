# cheatGame
#
# Usage: To find the shuffled word given in guessGame.py
# Next goal is to merge guessGame.py and cheatGuess.py
# This is just an auxillary version to find the word discussed in class "yuyinelm"

file = open("boun.list.txt",'r')
str = ''
# checkStr = "yuyinelm" 
checkStr = raw_input("Enter the shuffled word to search: ")
inStr = ''
ind = 0
linInd = 0

for line in file:
	str = line
	str = str[:-1]
	for j in checkStr:
		if j in str:
			ind += 1
	if ind == len(checkStr) and len(checkStr) == len(str):
		print("Found it!")
		print(str)
	ind = 0
