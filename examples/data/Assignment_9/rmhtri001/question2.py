InputFile = input("Enter the input filename:\n")
OutFile = input("Enter the output filename:\n")
LineWidth = eval(input("Enter the line width:\n"))

OldFile = open(InputFile, "r")
NewFile = open(OutFile, "w")

TempList = OldFile.read()
TempList = TempList.replace("\n", " ")

if len(TempList)<=LineWidth:
    print (TempList, file = NewFile)
else:
    Templist2 = TempList.split(" ")
    sum1 = 0
    prints = ""
    for word in Templist2:
        if word == " ":
            z = 0
        elif (len(prints)+len(word)) < LineWidth and word != Templist2[-1]:
            prints = prints + word + " "      
        elif (len(prints)+len(word)) == LineWidth:
            prints = prints + word
            print (prints, file = NewFile)
            prints = ""
        elif (len(prints)+len(word)) > LineWidth and word != Templist2[-1]:
            prints = prints[:len(prints)-1]
            print (prints, file = NewFile)
            prints = word + " "
        elif (len(prints)+len(word)) < LineWidth and word == Templist2[-1]:
            prints = prints + word 
            print(prints, file = NewFile)
        elif (len(prints)+len(word)) > LineWidth and word == Templist2[-1]:
            prints = prints = prints[:len(prints)-1] 
            print(prints, file = NewFile)
            prints = word 
            print(prints, file = NewFile)
 
OldFile.close()
NewFile.close()


