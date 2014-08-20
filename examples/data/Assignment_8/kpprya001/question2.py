word = input("Enter a message:\n")
string1 = word
pairs = 0
def count_characters(string1,pairs):
    if(string1[1:2]!=""):
        if(string1[0:1]==string1[1:2]):
            pairs += 1
            return count_characters(string1[2:],pairs)
        else:
            return count_characters(string1[2:],pairs)
    return pairs
        
        
print("Number of pairs:",count_characters(string1,pairs))
        
    
    