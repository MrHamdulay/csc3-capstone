# Luke Henkeman
# HNKLUK001
# 24 April 2014
# question1.py
# right-align a list of names input by the user

def aligned():
    name = input("Enter strings (end with DONE):\n")
    namestr = [name]
    while name != "DONE":
        name = input("")
        if name != "DONE":
            namestr.append(name)
        else:
            break
    longest = len(namestr[0])
    for i in range(1,len(namestr)):
        if len(namestr[i]) > longest:
            longest = len(namestr[i])
        i += 1
    print("\nRight-aligned list:")    
    for i in range(len(namestr)):
        gap = (longest-len(namestr[i]))*" "
        print(gap,namestr[i],sep="")
        i+=1
    
aligned()