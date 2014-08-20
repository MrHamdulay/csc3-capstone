#Kiuran Naidoo
#Assignment 8
#Question 2
#5 May

def pairs(word,num = 0):
    if len(word) > 1: #Base case
        if word[0] == word[1]:#Check if first character is same as second one
            return pairs(word[2:],num+1) #Truncate word by leading 2 characters and run function
        else:
            return pairs(word[1:],num)#Truncate word by leading 1 characters and run function
    else:
        return num#Return number of pairs accumulated
    
inputMessage = input("Enter a message:\n")#Get Input
print("Number of pairs:",pairs(inputMessage))
