# Tashiv Sewpersad
# Assignment 4 - Question 2
# 30 - 3 - 2014

def ndom_to_decimal(iNum):
	sNum = str(iNum)
	iLen = len(sNum)
	if iLen < 3: # corrects input
		sNum = (3-iLen)*"0"+sNum
	iResult = int(sNum[2]) + int(sNum[1])*6 + int(sNum[0])*36
	return iResult

def decimal_to_ndom(iNum):
	sResult = ""
	for k in [36,6,1]:
		sResult = sResult +  str(iNum//k)
		iNum = iNum%k
	iResult = int(sResult)
	return iResult

def ndom_add(iNum1,iNum2):
	iNum1 = ndom_to_decimal(iNum1)
	iNum2 = ndom_to_decimal(iNum2)
	iResult = iNum1 + iNum2
	iResult = decimal_to_ndom(iResult)
	return iResult

def ndom_multiply(iNum1,iNum2):
	iNum1 = ndom_to_decimal(iNum1)
	iNum2 = ndom_to_decimal(iNum2)
	iResult = iNum1 * iNum2
	iResult = decimal_to_ndom(iResult)
	return iResult

