def toPiglatin(s):
    t = s.split()
    if t[0]=="a" or t[0]=='i' or t[0]=='o' or t[0]=='e' or t[0]=='u':
        print(s+"way")
        
    else:
        for letter in t:
            if letter == [a,e,i,o,u]:
                break
            
        
