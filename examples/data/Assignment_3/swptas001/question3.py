# Tashiv Sewpersad
# CSC1015F
# Assignment 3 - Question 3

# input
sMessage = " " + input("Enter the message:\n") + " "
iLen = len(sMessage)
iMsgCnt = eval(input("Enter the message repeat count:\n"))
iFrameWidth = eval(input("Enter the frame thickness:\n"))


# Generating the body
if (iMsgCnt > 0) and (iFrameWidth > 0):
	sSideFrame = (iFrameWidth*"|")
	sBody = (sSideFrame + sMessage + sSideFrame)
	sBody = (sBody+"\n")*((iMsgCnt)-1) + sBody
else:
	sBody = ""

# Generating the border
sBorderT, sBorderB = "",""
for i in range(1,iFrameWidth+1):
	iSide = ((iLen+(2*iFrameWidth-1)-1)-(iLen+(2*i-1)-1))//2
	
	sBorder = iSide*"|" + "+" + (iLen+(2*i-1)-1)*"-" + "+" + "|"*iSide 
	if sBorder != "":
		sBorderB = sBorderB + "\n" + sBorder
		sBorderT = sBorder + "\n" + sBorderT
	else:	
		sBorderB = sBorderB + sBorder
		sBorderT = sBorder + sBorderT
print(sBorderT+sBody+sBorderB)