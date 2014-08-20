"""The program to fiht alligne the items in the list
By Bruce Sontshoto
20 April 2014 """


def main():
    #creating an  e mpty list
    names =[]
    #get a list of names
    name = input("Enter strings (end with DONE):\n")
    while name !='DONE':
        names.append(name)
        name = input("")
    #if done
    if name =='DONE':
        print()
        print("Right-aligned list:\n",end="")
    #identifying the length of the longest word
    longestWord = 0
    for item in range(len(names)):
        if longestWord < len(names[item]):
            longestWord = len(names[item])
    #right alignment prints    
    for i in range(len(names)):
        print((" "*(longestWord-len(names[i]))),end="")
        print(names[i])
            
        
        
main()        
       
