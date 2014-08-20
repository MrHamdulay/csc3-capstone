'''question 1 , Assignment 6
simangaliso mlangeni
MLNSIM014
23 April 2014'''

#get list from user
list1 = input("Enter strings (end with DONE):\n")
print()
lis =[]
while list1 != 'DONE':
    lis.append(list1)
    list1 = input("")

maxL = 0#set 0 to maximum length of list
#iterate through list for maximum length
for i in lis:
    if len(i) > maxL:
        maxL = len(i)#maximum length is set to new value
        
#create function to print out right-aligned words
def alignedstr():
    print("Right-aligned list:")
    for i in lis:
        numOfSpaces = maxL - len(i)#number of spaces to insert before the word
        print(numOfSpaces*" ",i,sep = '')#prints right aligned word
        
alignedstr()