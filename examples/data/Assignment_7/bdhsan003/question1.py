#Sandisha Budhal
#BDHSAN003

thelis = [] #CREATING AN EMPTY LIST

def LST_():
    string=input("Enter strings (end with DONE):\n")
    while string!="DONE": #AS LONG AS THE STING DOES NOT SAY "DONE", THE FOLLOWING WILL TAKE PLACE
        thelis.append(string) #THE LIST IS APPENDED AS EACH STRING IS ENTERED BY THE USER
        string=input("") #THIS ALLOWS THE USER TO INPUT DIFFERENT STRINGS ON NEW LINES
LST_()
print()

LIST2=[] #CREATING AN EMPTY LIST

def ELIMINATE():
    for strng in thelis:
        while strng not in LIST2:
            LIST2.append(strng)
    for i in LIST2:
        print(i)
print("Unique list:")
ELIMINATE()
