#-------------------------------------------------------------------------------
# Name:        question3
# Purpose:
#
# Author:      Lungelo Mdunge
#
# Created:     21/04/2014
# Copyright:   (c) Lungelo 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


print("Independent Electoral Commission")
print("--------------------------------")
#get input from user
candidates=[]
name=input("Enter the names of parties (terminated by DONE):\n")
while name!='DONE':
    candidates.append(name)
    name=input('')
print()

dictionary={}
for i in candidates:
    if not i in dictionary:
        dictionary[i] = 0
    dictionary[i]+=1

print("Vote counts:")
namelist=list(dictionary)
namelist.sort()
for word in namelist:
    form= '{0:<11}- {1:<}'.format(word,dictionary[word])
    print(form)



