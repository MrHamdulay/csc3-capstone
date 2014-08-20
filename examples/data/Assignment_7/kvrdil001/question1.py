#Dilan Koovarjee
#unique list
#29 April 2014

print ("Enter strings (end with DONE):")

userlist = []
newlist = []

while True:
    x=input ()
    if x=="DONE": #sentinel to break loop when user input done
        break
    else: #add input to list
        userlist.append (x)
print ()
print ("Unique list:")
for i in userlist:
    if i not in newlist:
        newlist.append (i)
        print (i) #print item if not in newlist (if not repeated)