import re


def sumValue(nameWithInitials, num_alpha):
	charArray = nameValue(nameWithInitials, num_alpha)
	tValue = sum(charArray)
	print("\n")
	print("Name : ", name.upper())
	print("Net Value : ", tValue)
	rVal = reverseValue(tValue)
	print("Rev Value : ", rVal)
	if tValue > 9:
		fSum = totalValue(tValue)
		print("Total : ", fSum)
	else:
		print("Total : ", tValue)
	planPyramid(charArray)


def planPyramid(charArray):
  tArr = []
  tArr.append(charArray)
  dList = buildPyramid(charArray, tArr)
  simplePyramid(dList)
  

def simplePyramid(dList):
  fLen = len(dList)
  lElem = dList[fLen -1]
  sLE = sum(lElem)
  print("Calculation Value : ", sLE)
  #print("Calculation : ")
  pTVal = []
  dSpace = " "
  lSpace = ""
  for iList in dList:
    iVal = sum(iList)
    eVal = totalValue(iVal)
    pTVal.append(eVal)
    lSpace += dSpace
    #print(lSpace, str(iList)[1:-1])
    #print(str(iList)[1:-1])
    fList = ' '.join(map(str, iList))
    print(lSpace + str(fList) + lSpace + " => " + str(iVal) + " => " + str(eVal))
  #repeatPyramids(pTVal)
  
  
def repeatPyramids(pTVal):
  #pTVal.pop()
  pVal = []
  pVal.append(pTVal)
  sVal = len(pTVal)
  if sVal > 1:
    sList = buildPyramid(pTVal, pVal)
    simplePyramid(sList)
  
  
def nameValue(name, num_alpha):
	charArray = []
	characters = list(name)
	for character in characters:
		for alpha, num in num_alpha.items():
			if character == alpha:
				charArray.append(num)
			else:
				pass
	return charArray


def totalValue(number):
	tSum = []
	rev = 0
	while (number > 0):
		reminder = number % 10
		rev = rev * 10 + reminder
		tSum.append(reminder)
		number = number // 10
	sValue = sum(tSum)
	if sValue > 9:
		fVal = sValue
		return totalValue(fVal)
	else:
		return sValue


def reverseValue(number):
  rev = 0
  while(number > 0):
    reminder = number % 10
    rev= rev * 10 + reminder
    number = number // 10
  return rev


def buildPyramid(numArray, tArr):
	rArray = []
	for cVal, nVal in zip(numArray, numArray[1:]):
		num = cVal + nVal
		tNum = totalValue(num)
		rArray.append(tNum)
	rLen = len(rArray)
	if rLen >= 2:
		tArr.append(rArray)
		return buildPyramid(rArray, tArr)
	else:
		return tArr


if __name__ == '__main__':
	# Name to be used to calculate
	try:
		names = input(
		    "Enter your name(s) [For multiple names use ',' between each name] : "
		).lower()
		n = True
		while n == True:
			invalidName = re.search("[^(A-Za-z),. ]+", names)

			if invalidName:
				print("No numbers or special characters will be accepted.")
				names = ""
				n = False
			elif not names:
				print("You must type something in!")
				names = ""
				n = False
			else:
				n = False
	except:
		names = ""

	# Choose Style of Numerology to be used
	try:
		myMethod = input(
		    "Enter anyone method ['Indian', 'Chaldean', 'Pythagorean'] : "
		).lower()
		n = True
		while n == True:
			invalidMethod = re.search("[^A-Za-z]+", myMethod)

			if invalidMethod:
				print(
				    "No numbers or special characters will be accepted. So By Default we will use Indian Numerology Method"
				)
				myMethod = "Indian"
				n = False
			elif not names:
				print(
				    "You must type something in! or By Default we will use Indian Numerology Method"
				)
				myMethod = "Indian"
				n = False
			else:
				if myMethod == "Indian" or myMethod == "indian":
					myMethod = "Indian"
				elif myMethod == "Chaldean" or myMethod == "chaldean":
					myMethod = "Chaldean"
				elif myMethod == "Pythagorean" or myMethod == "pythagorean":
					myMethod = "Pythagorean"
				else:
					myMethod = "Indian"
				n = False
	except:
		myMethod = "Indian"

	numerologyPythagorean = {
	    "a": 1,
	    "b": 2,
	    "c": 3,
	    "d": 4,
	    "e": 5,
	    "f": 6,
	    "g": 7,
	    "h": 8,
	    "i": 9,
	    "j": 1,
	    "k": 2,
	    "l": 3,
	    "m": 4,
	    "n": 5,
	    "o": 6,
	    "p": 7,
	    "q": 8,
	    "r": 9,
	    "s": 1,
	    "t": 2,
	    "u": 3,
	    "v": 4,
	    "w": 5,
	    "x": 6,
	    "y": 7,
	    "z": 8
	}

	numerologyChaldean = {
	    "a": 1,
	    "b": 2,
	    "c": 3,
	    "d": 4,
	    "e": 5,
	    "f": 6,
	    "g": 7,
	    "h": 8,
	    "i": 1,
	    "j": 2,
	    "k": 3,
	    "l": 4,
	    "m": 5,
	    "n": 6,
	    "o": 7,
	    "p": 8,
	    "q": 1,
	    "r": 2,
	    "s": 3,
	    "t": 4,
	    "u": 5,
	    "v": 6,
	    "w": 7,
	    "x": 8,
	    "y": 1,
	    "z": 2
	}

	numerologyIndian = {
	    "a": 1,
	    "b": 2,
	    "c": 3,
	    "d": 4,
	    "e": 5,
	    "f": 8,
	    "g": 3,
	    "h": 5,
	    "i": 1,
	    "j": 1,
	    "k": 2,
	    "l": 3,
	    "m": 4,
	    "n": 5,
	    "o": 7,
	    "p": 8,
	    "q": 1,
	    "r": 2,
	    "s": 3,
	    "t": 4,
	    "u": 6,
	    "v": 6,
	    "w": 6,
	    "x": 5,
	    "y": 1,
	    "z": 7
	}

	numerology = {
	    "Indian": numerologyIndian,
	    "Chaldean": numerologyChaldean,
	    "Pythagorean": numerologyPythagorean
	}

	if names != "":
		print("\n")
		print("Numerology method used: " + myMethod)
		names = names.split(",")
		for name in names:
			if name != "":
				sumValue(name, numerology[myMethod])
			else:
				print("\n")
				print("TIme to do some stretches.")
	else:
		print("You must type something in!.")
	print("------------------------------------------")