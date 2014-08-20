#GLMSUM001
#Sumayah Goolam Rassool

#--------------------------------------------------user input-------------------------------------
sent=input("Enter a string:\n")

#------------------------------------------------checks if sentence is a palindrome---------------------------------
def palindrome(sent):
#----------------------------------------------if sentence is one letter long = palindrome    
    if len(sent)<1:
        print("Palindrome!")

    

    else:
#------------------------------------------if end letters of sentence are the same = palindrome        
        if sent[0]==sent[-1]:
#--------------------------------------------returns substring of sent from first to last letter       
            return palindrome(sent[1:-1])
        else:
            print("Not a palindrome!")
palindrome(sent)
    

    
    
                       
    
    