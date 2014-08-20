#Assignment 9.2
#Michael Gant
#11/05/2014

#Reformat

iCurrWidth = 0
sOutput = ""

fInput = open(input("Enter the input filename:\n"), "r")
fOutput = open(input("Enter the output filename:\n"),"w")
iWidth = eval(input("Enter the line width:\n"))

sText = fInput.read()
for k in range(len(sText)):
    if sText[k:k+2] != "\n\n" and sText[k-1:k+1] != "\n\n" and sText[k] == "\n":
        sText = sText[0:k] + " " + sText[k+1:]
lText = sText.split(" ")

iCurrWidth = iWidth
for k in lText:
    if "\n\n" in k:
        sOutput = sOutput + k + " "
        iCurrWidth = iWidth-6
    elif iCurrWidth < len(k):
        iCurrWidth = iWidth - (len(k)+1)
        sOutput = sOutput + "\n" + k + " "
    else:
        sOutput = sOutput + k + " "
        iCurrWidth = iCurrWidth - (len(k)+1)


fOutput.write(sOutput)

fInput.close()
fOutput.close()