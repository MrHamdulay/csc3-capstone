#Assignment 5
#Question 1
#Receive a list of string. Sentinel controlled with word DONE. Find and evaluate length of longest string in array. Format right according to length of longest and print. 

words = []

words.append(input("Enter strings (end with DONE):\n"))
while 'DONE' not in words:
    words.append(input(""))

maxlength = max(len(i) for i in words)
longestword = [i for i in words if len(i) == maxlength]
    
print()
print("Right-aligned list:")
x = "{0: >"+str(maxlength)+"}"
for i in range(len(words)-1):
    print(x.format(words[i]))