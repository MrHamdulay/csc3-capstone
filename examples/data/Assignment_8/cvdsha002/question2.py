"""Shahrain Coovadia"""
string=input("Enter a message:\n")   #prompts for input
def repeat(i):                          
    pair=0            
    if len(i)<2:               
        return 0
    else:
        if i[0]==i[1]:       #checks if letters are pairs
            pair=pair+1         #carries on to the next letter
            return pair+repeat(i[2:])        #adds on additional pairs found
        else:return pair+repeat(i[1:])
print("Number of pairs:", repeat(string))   #output

        
    