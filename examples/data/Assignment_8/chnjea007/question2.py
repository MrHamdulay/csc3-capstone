#A8Q2

index = 0
count = 0

def findPairs(s):
    global index
    global count
    if s[index] == s[index+1]:
        count+=1
        index+=1
    index+=1
    if index < (len(s) - 1):
        findPairs(s)
text = input("Enter a message:\n")
findPairs(text)
print("Number of pairs:", count)