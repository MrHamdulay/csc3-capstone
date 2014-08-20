"""Chat=racter pair counter
Luveshen Pillay
4/5/14"""
word=str(input("Enter a message:\n"))

def char_pair(word):
        
    if len(word) % 2 == 0:
        if len(word)== 0:
            return 0  
        # retrun 1 and function if a set pf repeats is found
        if word[0] == word[1]:
            return 1 + char_pair(word[2:])
        
        # if no repeats just return function    
        else:
            return char_pair(word[2:])
        
    else:
        if len(word)== 1:
            return 0  
        # retrun 1 and function if a set pf repeats is found
        if word[0] == word[1]:
            return 1 + char_pair(word[2:])
        
        # if no repeats just return function    
        else:
            return char_pair(word[2:])        
    
    
    
    
print("Number of pairs:",char_pair(word))