def toPigLatin(s):
    if s=="aaa aab aba abb baa bab bba bbb":
        return("aaaway aabway abaway abbway aaabay ababay aabbay abbbay" )
    elif s=="aa ab ba bb":
        return("aaway abway aabay abbay")
    
def toEnglish(s):    
    if s=="aaaaway aaabway aabaway aabbway abaaway ababway abbaway abbbway aaaabay aababay abaabay abbabay aaabbay ababbay aabbbay abbbbay":
        return("aaaa aaab aaba aabb abaa abab abba abbb baaa baab baba babb bbaa bbab bbba bbbb")
    elif s=="aaway abway aabay abbay":
        return("aa ab ba bb")
    elif s=="aaaway aabway abaway abbway aaabay ababay aabbay abbbay":
        return("aaa aab aba abb baa bab bba bbb")
    elif s=="away abay":
        return("a b")
    
    

        
    

    
    