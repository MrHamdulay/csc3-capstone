def toPigLatin (s):
   a=""
   vowels=['a','e','i','o','u']
   space=s.split(' ')
   for i in space:
      if i[0] in vowels:
         a+=(i[0:]+'way ')
      else:
         for j in range(len(i)):
            if i[j] in vowels:
               a+=(i[j:]+'a'+i[0:j]+'ay ')
               break
      x=0
      while i[x] not in vowels:
         x+=1
         if x==len(i):
            a+=('a'+i+'ay ')
            break
         
   
      
   return a

def position(x):
    c = 0
    p1 = 0
    p2 = 0
    for i in range(len(x)-1,-1,-1):
        if x[i] == "a":c+=1
        if c == 2:
            p1=i
            c+=1
        if x[i] == "a":
            p3 = i
            break
    return p1, p2
    
def Convertion(x):
    if x[len(x)-3] == "w": return x[:len(x)-3]
    else:
        p1, p2 = position(x)
        return x[p1+1:p3] + x[:p1]
    
def toEnglish(s):
    words = s.split(" ")
    eng = ""   
    for x in words:
        eng = eng + Convertion(x)    
        eng = eng + " "
    return eng[:len(eng)-1]