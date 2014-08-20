"""Programme to count repeated pairs in string
Mishka Latib
06 May 2014"""

#function to count repeated pairs

def repeated_pairs(string,count):
    if len(string)>=2:
        #checks for repeats
        if string[0]==string[1]:
            return repeated_pairs(string[2:],(count+1))
        if string[0]!=string[1]:
            return repeated_pairs(string[1:],count)
    else:
        #provides output of how many repeats were found in string
        print("Number of pairs:",count)

  
string = str(input("Enter a message:\n"))
#calls function with string input in place
repeated_pairs(string,0)
