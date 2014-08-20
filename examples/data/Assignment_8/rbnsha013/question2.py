"""Count number of repeated characters in a string
Shane Robinson
3 May 2014"""

print("Enter a message:")
string = input()
count = 0
string_list = []

def pairs(string):
    global count
    if string=="":
        return count
    elif string[0]==' ':
        return pairs(string[1:])
    elif len(string)==1:
        return count
    elif string[0]!=string[1]:
        return pairs(string[1:])
    elif string[0]==string[1]:
        count+=1
        return pairs(string[2:])
    return count

num = pairs(string)
print("Number of pairs:", num)