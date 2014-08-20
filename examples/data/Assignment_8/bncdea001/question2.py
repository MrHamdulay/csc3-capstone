#Program to count number of pairs in a sentence
#Dean Bunce
#3 May

#Get input from user
string=input("Enter a message: \n")


#Count the number of pairs in the string using recursion
def count(string):
    
    
        if len(string)<2:
                
                return 0
        
        #If not found, add 0
        elif string[0]!=string[1] and len(string)>=2:
        
                return 0 + count(string[1:])
        
        #If found, add 1
        elif string[0]==string[1] and len(string)>=2:
        
                return 1 + count(string[2:])
        
    
#Give output 
print("Number of pairs:", count(string))