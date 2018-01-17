'''
Banco Algarete
Marcos O. Nieves Rivera
Section M J 3:30 - 4:30

NOTE (for Github users not professor):
I made this program with the intention that the program could always work as a real bank account.
Meaning that even when you close the program, everything is saved into the text file. That wasn't the full
intention of the class proyect so for that reason, the last line replaces the file format needed
to work even when the program closes. To use this program as a real bank account just remove the last line
and just type all of the new commands you want on the file named 'alghistorical.txt'.
'''

import sys
import time
import ast
import os
os.system("clear")


formatString = "\t\t----------AL GARETE BANK HISTORICAL REPORT----------\nReport of Bank Accounts oRdered by Account Numbers"
fileH = "alghistorical.txt"
fileC = "algcustomers.txt"
lineCArray = []
bankEarnings = 0
bonusPaid = 0

def writeToTxt(file, string):
	text_file = open(file, "a")
	text_file.write(string)
	text_file.close()

def overwriteTxt(file, string):
	text_file = open(file, "w+")
	text_file.write(string)
	text_file.close()

def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            #print '"{old_string}" not found in {filename}.'.format(**locals())
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        #print 'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals())
        s = s.replace(old_string, new_string)
        f.write(s)

mainArray = []
def changeToArray(lineArray):
	#Get the list size so we can get the last item in the list (another list) and convert to string.
	arrayLength = len(lineArray)
	lineArray[arrayLength - 1] = str(lineArray[arrayLength - 1])
	##
	for s in lineArray:
		s = s.replace("\n", "")
		formattedS = ast.literal_eval(s)
		mainArray.append(formattedS)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#################

# print "Enter the input:"
# input_ = raw_input("")
# inputArray = input_.split(", ")

overwriteTxt(fileC, "")

try:
	file_ = open(fileH)
except:
	print "ERROR! FILE '" + fileC + "' NOT FOUND! Closing program..."
	time.sleep(3)
	sys.exit()
linesInFile = file_.readlines()
for line in linesInFile:
	inputArray = line.split(", ")

	print line
	#time.sleep(3)

	if (line.lower().startswith("o")):
		customerName = inputArray[1]

		#Take out transaction fee
		amountMoney = float(inputArray[2])
		amountSubtracted = amountMoney*0.05
		amountMoney = amountMoney - amountSubtracted
		bankEarnings = bankEarnings + amountSubtracted
		try:
			fp = open(fileC)
		except:
			writeToTxt(fileC, "")
		lines = fp.readlines()
		linesAmount = 0
		for line in lines:
			linesAmount = linesAmount + 1
			#lineCArray.append(line)#Creates a list with all the bank accounts with its format.
		accNumber = linesAmount + 1
		accNumber = str(accNumber).zfill(10)
		bankAccount = [accNumber, customerName, amountMoney]
		#lineCArray.append(bankAccount) #Again after the new bankAccount has been created.
		#Format
		bankAccount = str(bankAccount).replace("\'" + str(accNumber) + "\'", str(accNumber))
		##
		writeToTxt(fileC, str(bankAccount) + "\n")
		
	elif (line.lower().startswith("w")):
		accNumber = int(inputArray[1])
		amountMoney = float(inputArray[2])
		amountSubtracted = amountMoney*0.05
		amountSubtracted = float("{0:.2f}".format(amountSubtracted))
		#amountMoney = amountMoney + amountSubtracted
		bankEarnings = bankEarnings + amountSubtracted

		try:
			fp = open(fileC)
		except:
			writeToTxt(fileC, "")
		lines = fp.readlines()
		linesAmount = 0
		lineCArray = []
		mainArray = []
		for line in lines:
			linesAmount = linesAmount + 1
			lineCArray.append(line)#Creates a list with all the bank accounts with its format.
		
		changeToArray(lineCArray)
		
		previousArray = lines[accNumber - 1]
		customerArray = mainArray[accNumber - 1]
		customerArray[2] = customerArray[2] - amountMoney
		#Format
		accNumber = str(accNumber).zfill(10)
		customerArray[0] = accNumber
		customerArray = str(customerArray).replace("\'" + str(accNumber) + "\'", str(accNumber))
		##
		inplace_change(fileC, str(previousArray), str(customerArray) + "\n")

	elif (line.lower().startswith("d")):
		accNumber = int(inputArray[1])
		amountMoney = float(inputArray[2])
		amountSubtracted = amountMoney*0.05
		amountSubtracted = float("{0:.2f}".format(amountSubtracted))
		amountMoney = amountMoney - amountSubtracted
		bankEarnings = bankEarnings + amountSubtracted
		try:
			fp = open(fileC)
		except:
			writeToTxt(fileC, "")
		lines = fp.readlines()
		#linesAmount = 0

		lineCArray = []
		mainArray = []
		for line in lines:
			#linesAmount = linesAmount + 1
			lineCArray.append(line)#Creates a list with all the bank accounts with its format.

		changeToArray(lineCArray)
		previousArray = lines[accNumber - 1]
		customerArray = mainArray[accNumber - 1]
		customerArray[2] = customerArray[2] + amountMoney
		#Format
		accNumber = str(accNumber).zfill(10)
		customerArray[0] = accNumber
		customerArray = str(customerArray).replace("\'" + str(accNumber) + "\'", str(accNumber))
		##
		inplace_change(fileC, str(previousArray), str(customerArray) + "\n")

	elif (line.lower().startswith("b")):
		bonus = float(inputArray[1])
		try:
			fp = open(fileC)
		except:
			writeToTxt(fileC, "")
		lines = fp.readlines()
		linesAmount = 0
		bonusSum = 0
		for line in lines:
			dividedLine = line.split(", ")
			dividedLine[2] = dividedLine[2].replace("]", "") #This takes out the character to get integer
			bonusSum = float(dividedLine[2]) * (bonus/100)
			bonusSum = float("{0:.2f}".format(bonusSum))
			dividedLine[2] = str(float(dividedLine[2]) + bonusSum)
			bonusPaid = bonusPaid + bonusSum
			dividedLine[2] = dividedLine[2] + "]\n" #Adds character taken
			dividedLine = ", ".join(dividedLine)
			inplace_change(fileC, line, dividedLine)
			#lineCArray.append(line)#Creates a list with all the bank accounts with its format.
		#changeToArray(lineCArray)

	else:
		print "ERROR! Please use the letters 'o, w, d, or b' depending on your action! To try again, open program once again. Closing..."
		print "Closing program..."
		time.sleep(3)
		sys.exit()
		#time.sleep(5)

print """
 				---------  AL GARETE BANK HISTORICAL REPORT  ---------
Report of Bank Accounts Ordered by Account Numbers
""" + color.BOLD + color.UNDERLINE + """Account Number""" + color.END +  """ 					""" + color.BOLD + color.UNDERLINE + """Customer Name""" + color.END + """ 					""" + color.BOLD + color.UNDERLINE + """Balance""" + color.END
try:
	fp = open(fileC)
except:
	writeToTxt(fileC, "")
lines = fp.readlines()
customerList = []
for line in lines:
	line = line.replace("\n", "").replace("[","").replace("]", "").replace("\'", "")
	outputArray = line.split(", ")
	print outputArray[0] + " \t\t\t\t\t" + outputArray[1] + " \t\t\t\t\t$" + ("%.2f" % float(outputArray[2]))
	#Add to 'customerList[]' all of the customer names to sort.
	customerList.append(outputArray[1])
	#print '%s \t\t\t\t\t%s \t\t\t\t\t%s \t\t\t\t\t' % (outputArray[0], outputArray[1], outputArray[2])
customerList = sorted(customerList)

print """
Report of Bank Accounts Ordered by Names of Owners
""" + color.BOLD + color.UNDERLINE + """Customer Name""" + color.END +  """ 					""" + color.BOLD + color.UNDERLINE + """Account Number""" + color.END + """ 					""" + color.BOLD + color.UNDERLINE + """Balance""" + color.END

sortedCustomerList = []
count = 0
finalOutput = ""
while (count < len(customerList)):
	for line in lines:
		line = line.replace("\n", "").replace("[","").replace("]", "").replace("\'", "")
		outputArray = line.split(", ")
		if (customerList[count] in outputArray):
			print outputArray[1] + " \t\t\t\t\t" + outputArray[0] + " \t\t\t\t\t$" + ("%.2f" % float(outputArray[2]))
			finalOutput = finalOutput + outputArray[1] + ", " + outputArray[0] + ", " + ("%.2f" % float(outputArray[2])) + "\n"
	count = count + 1






print """
Report of Bank Accounts Ordered by Names of Owners
""" + color.BOLD + color.UNDERLINE + """Customer Name""" + color.END +  """ 					""" + color.BOLD + color.UNDERLINE + """Account Number""" + color.END + """ 					""" + color.BOLD + color.UNDERLINE + """Balance""" + color.END

largestBalance = 0
balanceSorted = []
for line in lines:
	line = line.replace("\n", "").replace("[","").replace("]", "").replace("\'", "")
	outputArray = line.split(", ")
	balanceSorted.append((outputArray[2]))
balanceSorted = sorted(balanceSorted, reverse=True, key=float)
averageBalance = 0
count = 0
for balance in balanceSorted:
	averageBalance = averageBalance + float(balance)
	count = count + 1
averageBalance = averageBalance / count

balanceMax = balanceSorted[0]

for line in lines:
	line = line.replace("\n", "").replace("[","").replace("]", "").replace("\'", "")
	outputArray = line.split(", ")
	if balanceSorted[0] in line:
		accountMaxCustomer = outputArray[0]
		maxCustomer = outputArray[1]
print maxCustomer + " \t\t\t\t\t" + accountMaxCustomer + " \t\t\t\t\t$" + ("%.2f" % float(balanceMax))

print """
Report of Accounts with Minimum Balance
""" + color.BOLD + color.UNDERLINE + """Customer Name""" + color.END +  """ 					""" + color.BOLD + color.UNDERLINE + """Account Number""" + color.END + """ 					""" + color.BOLD + color.UNDERLINE + """Balance""" + color.END
balanceSorted = sorted(balanceSorted, key=float)
balanceMin = balanceSorted[0]

for line in lines:
	line = line.replace("\n", "").replace("[","").replace("]", "").replace("\'", "")
	outputArray = line.split(", ")
	if balanceSorted[0] in line:
		accountMinCustomer = outputArray[0]
		minCustomer = outputArray[1]
print minCustomer + " \t\t\t\t\t" + accountMinCustomer + " \t\t\t\t\t$" + ("%.2f" % float(balanceMin))

print "Average of Accounts Balances is: $" + ("%.2f" % averageBalance)
print "Total Bank Gross Earnings: $" + ("%.2f" % bankEarnings)
print "Total Bonus Paid: $" + ("%.2f" % bonusPaid)
print " 				---------  END OF HISTORICAL REPORT  ---------"""
#overwriteTxt(fileC, finalOutput)