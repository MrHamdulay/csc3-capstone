m = input("Enter the message:\n")
c = eval(input("Enter the repeat count:\n"))
t = eval(input("Enter the frame thickness:\n"))



    
#length of phrase
l=(len(m))
#l=l+2
print('len:')
print(l)

m=' '+m+' '




#create top
top=''

for i in range(0,l+2*t):
    top=top+'-'
top='+'+top+'+'



#create second line
#length of phrase
l=(len(m))
#l=l+2


m=''+m+''



second=''
topp=''


for j in range(0,l):
    topp=topp+''
    topp='+'+topp+'+'
    

    for k in range(c+l) :
        second=top
        second='|'+second+'|'
    


print(top)
print(second)

#adds amount of side edges to phrase
for j in range(0,t):
        m='|'+m+'|'

for i in range(0, c) :
    
    print(m)
    
print(second)
print (top)
