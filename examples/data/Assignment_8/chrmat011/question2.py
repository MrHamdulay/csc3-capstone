def pair(s):
    if len(s[0])==1:
        return 0
    if s[1] > len(s[0])-2:
        return s
    
    if s[1] == len(s[0])-2:
        if s[0][s[1]]==s[0][s[1]+1]:
            s[2] += 1
        return [s[0],0,s[2]]

    if s[0][s[1]]==s[0][s[1]+1]:
        s[2] += 1
        s[1] += 1
    return pair([s[0],s[1]+1,s[2]])
    
i = input("Enter a message:\n")
print("Number of pairs:",pair([i,0,0])[2])
