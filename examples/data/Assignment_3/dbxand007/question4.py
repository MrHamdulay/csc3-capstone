#Cherise Dube
#28 March 2014
#Program to find palindromic primes between two raw inputs 
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
List=[0]


for i in range(N+1,M):
    x= str(i) #converts i into a string 
    reverse= x[::-1] #reverses to check if palindrome    
    if i==2:
        List.append(2)  #Makes sure 2 is included as a palindromic prime  
   
    elif i==int(reverse): #if the integer of the reversed number= that of the original number (i.e. they are palindromic)...
        for j in range(2,i): #all the numbers up to the palindrome
            if i%j ==0: #if the palindrome is divisible by a a specific number lower than itself stop and move on to next iteration
                break  
            elif i and j==i-1: # else if it is not divisible by a specific number and that number is the last in the iteration add it to the list of palindromes
                List.append(i)
    else:continue
List.remove(0)  #Removes the 0 List was initially set to 
print("The palindromic primes are:")
for a in List:
    print (a) 
                    
        
