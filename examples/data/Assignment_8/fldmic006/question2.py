#program to count the number of pairs in an entered string
#michael Field
#5 may 2014

#create the message fucntion
def pairs(message, npairs, count):
    
    #check for empty string
    if message == "":
        print("Number of pairs:", count)
    
    elif (count+1) < len(message):
        if message[count] == message[count+1]:
            npairs += 1
            
            #check if there are 3 of the same character next to each other
            if (count+2) < len(message):
                if message[count] == message[count+2]:
                    count += 2
                    
                else:
                    count += 1
            else:
                count += 1
                
            pairs(message, npairs, count)
        
        else:
            count += 1
            pairs(message, npairs, count)  
            
    elif count == (len(message)-1):
        print("Number of pairs:", npairs)
        
    else:
        count += 1
        pairs(message, npairs, count)

#get input. create count to check the position of the current character being compared
message = input("Enter a message:\n")
count = 0
npairs = 0

pairs(message, npairs, count)
