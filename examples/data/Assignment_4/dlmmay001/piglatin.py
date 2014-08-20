def toPigLatin (s):
    s.split()
    print(s)
    p = list(s)
 #   print(p)
    vowel = ['a','e','i','o','u']
    lst = []
    i = 0
    if s[0] in vowel:
        s = p[i] + 'way'
        print(s)
   # else: #s[0] != vowel:    
    #    while s[i::] not in vowel:
      #      lst.append(s[i::])
     #       i+=1
      #      str(lst)
        #print(lst)
        
toPigLatin ('apple ade')        