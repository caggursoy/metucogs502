# Import required libraries
# encoding=utf8 
from Crypto.Cipher import AES
from openpyxl import Workbook
from openpyxl import load_workbook
import random

passStr = "" # Init password string variable
gradeList = [] # define the grade list
dumList = []
encList = []
idx = 0
ind = 0
ind2 = 0
ind3 = 0

for i in range (0, 16): # in a for loop generate the random password
		passStr += chr(random.randint(33, 126))
obj = AES.new(passStr, AES.MODE_ECB)
obj2 = AES.new(passStr, AES.MODE_ECB)
# if (len(msg)%16 != 0):
# 	for i in range (0, 16-len(msg)%16):
# 		msg += " "
# codeText = obj.encrypt(msg)
# print (codeText)
# obj2 = AES.new(passStr, AES.MODE_CBC, 'This is an IV456')
# encodeText = obj2.decrypt(codeText)
# print(encodeText)

# Read from file 
wb_name = raw_input("Please enter the name of the file: ") + ".xlsx"
sheet_name = raw_input("Please enter the name of the sheet: ")
num_student = input("Please enter the number of students: ")
num_quiz = input("Please enter the number of quizzes: ")
wb = load_workbook(wb_name)
sheet_ranges = wb[sheet_name]
for k in range (2, 2+num_student):
	for j in range (65, 65+num_quiz+1):
		row_str = chr(j)+str(k)
		dumList.insert(idx,(sheet_ranges[row_str].value))
		idx += 1
	gradeList.insert(ind,dumList[ind*(1+num_quiz):ind*(1+num_quiz)+(num_quiz+1)])
	ind += 1
	
# Encode the read values
for ii in range (0,num_student):
	for jj in range (0,num_quiz):
		msg = str(gradeList[ii][jj])
		if (len(msg)%16 != 0):
			for i in range (0, 16-len(msg)%16):
				msg += " "
				
		encList.insert(ind2, obj.encrypt(msg))
		ind2 += 1
				
# 		print(msg)
# 		print(codeText)
# 		encodeText = obj2.decrypt(codeText)
# 		print(encodeText)

# Write to another sheet 
ws1 = wb.get_sheet_by_name("Sayfa2")

for k in range (2, 2+num_student):
	for j in range (65, 65+num_quiz+1):
		cellNo = chr(j)+str(k)
		# ws1[cellNo] = encList[ind3]
		try:
			print(obj2.decrypt(encList[ind3]))
			ind3 += 1
		except IndexError as e:
			break
		
#Add this line
wb.save("grades.xlsx")

# Get the values for each student into a list -- done
# Encode the values, then save to a file
# Let user write e-mails for the students (might get it from an excel file) then send the keys to the students
# Write a code to decypher the grades. User can only decypher his/her own row
