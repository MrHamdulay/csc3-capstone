#Question 2
#Counting the number of pairs of repeated characters in a string
#By: Dean de Haast

count= 0
s =input("Enter a message:\n")

def counter(s):
    global count 
    
    if s == "":
        return (print("Number of pairs:", count))
    elif len(s) >1:
        if s[0] == s[1]: #Checks if 2 letters next to one another are the same.
            count += 1
        return counter(s[2:]) # Recursive step removes 2 letters from the left each time
    else:
        return(print("Number of pairs:",count)) 
counter(s)

    