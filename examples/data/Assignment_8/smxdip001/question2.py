#Program to count the number of pairs of repeated characters in a string
#Dipanjali Samoo
#SMXDIP001
#11.05.2014

def counting(string,count):
    if len(string)==0 or len(string)==1:
        return print("Number of pairs:",count)
    
    else:
        if string[0]==string[1]:
            count+=1
            return (counting(string[2:len(string)],count))
        else:
            return(counting(string[2:len(string)],count))
        print("Number of pairs:",count)
        
    
#prompting user to enter a string
string = input("Enter a message:\n")
counting(string,0)