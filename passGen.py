# Import required modules
import random
# Definitions
passList=[] # define the password list
passStr = "" # Init password string variable

# Main code goes here
while(True):
	# from user, get the desired pass length
	passLen = int(input("Please enter desired length of the password to be generated: "))
	for i in range (0, passLen): # in a for loop generate the random password
		passStr += chr(random.randint(33, 126))
	print("Your randomly generated password is: "+passStr)
	# Save the pass if user wants so
	checkSave = raw_input("Do you want to save the password? (Y/N): ")
	if (checkSave =='Y'): # Save the pass
		passTag = raw_input("Please enter a tag for your password: ") # Enter a tag to create a tuple to remind the user
		passList.insert(0, (passTag,passStr)) # Add tuple to the list
		checkQuit = raw_input ("Do you want to quit? (Y/N): ") # Ask if user wants to quit
		if (checkQuit == 'Y'): # If wants to quit
			checkShow = raw_input ("Do you want to see your passwords? (Y/N): ") # Ask if user wants to see passwords
			if (checkShow == 'Y'): # If yes
				print(passList) # Print the passwords
				break
			else: # If no
				break # Kill the script
		elif (checkQuit == 'N'): # If user does not want to quit
			checkShow = raw_input ("Do you want to see your passwords? (Y/N): ") # Ask if user wants to see passwords
			if (checkShow == 'Y'): # If yes
				print(passList) # Print the passwords
				checkQuit = raw_input ("Do you want to quit? (Y/N): ") # Ask if user wants to quit
				if (checkQuit == 'Y'): # If yes
					break # Kill the script
	else: # If user does not want to save the password
		checkRet = raw_input("Do you want to create a new password? (Y/N): ") # Ask if user wants to create a new password
		if (checkRet == 'N'): # Check if user wants to create or not
			break # If not kill the script
