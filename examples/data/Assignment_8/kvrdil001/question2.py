#Repeated strings function
#Dilan Koovarjee
#6 May 2014

#create a function to count the number of pairs
def count_pairs (message):                      #use input as parameter
    if len(message)==1:                         #use if else elif to find pairs
        return 0
    elif len(message)==2:
        if message[0]==message[1]:
            return 1
        else:
            return 0
    elif message[0] == message[1]:
        return 1 + count_pairs(message[2:])
    else:
        return 0 + count_pairs(message[1:])

message=input("Enter a message:\n") 
y=count_pairs(message)                                   
print("Number of pairs:",y)                               

 
        
 
        
   

