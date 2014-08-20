# Tashiv Sewpersad
# Assignment 4 - Question 1
# 30 - 3 - 2014

def print_square():
	sBase = "*"*5
	sInner = "*" + " "*3 + "*"
	sInner = (sInner + "\n")*2 + sInner
	print(sBase,sInner,sBase,sep="\n")

def print_rectangle(iWidth,iHeight):
	sResult = "*"*iWidth + "\n"
	for i in range(iHeight-2):
		sInner = "*"
		for J in range(iWidth-2):
			sInner += " "
		sInner += "*"   
		sResult += sInner + "\n"
	sResult += "*"*iWidth
	print(sResult)

def get_rectangle(iWidth,iHeight):
	sResult = "*"*iWidth + "\n"
	for i in range(iHeight-2):
		sInner = "*"
		for J in range(iWidth-2):
			sInner += " "
		sInner += "*"   
		sResult += sInner + "\n"
	sResult += "*"*iWidth
	return sResult

