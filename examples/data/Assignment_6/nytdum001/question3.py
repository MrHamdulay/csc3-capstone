"""program to count the number of votes for each political party in an election
Dumisani J Nyathi
23-04-2014"""

def EVC():
    print("Independent Electoral Commission")
    print("--------------------------------")
    y=input("Enter the names of parties (terminated by DONE):\n")
    z=dict()#Create an empty dictionary in which input will be added
    while y != 'DONE':
        if y in z.keys():
            z[y]+=1
        else:
            z[y]=1
        y = input("")
    
    print()#for an empty line between input and output

    print("Vote counts:")
    for i in sorted(z.keys()):
        print("{0:<10}".format(i),'-',z[i])#cant use+ because strings and integers
        #remember always to differentiate [] from ()
    
                
    
EVC()#call function