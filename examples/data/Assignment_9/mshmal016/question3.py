lines=[]
allans=[]
#horizontal check
for i in range (9):
    single=[]
    line=input()
    for i in range(len(line)):
        single.append(eval(line[i]))
    lines.append(single)
    
ans=[]
check=[1,2,3,4,5,6,7,8,9]
for i in range(9):
    for l in range(9):
        if check[l] not in lines[i]:
            ans.append(1)
if 1 in ans:
    allans.append(1)

#vertical check
vertical=[] 
for a in range(4):
    vert=[]
    for line in lines:
        vert.append(line[a])
    vertical.append(vert)
    
ans2=[]
for c in range(4):
    for d in range(4):
        if check[d] not in vertical[c]:
            ans2.append(1)
if 1 in ans2:
    allans.append(1)
if 1 in allans:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")
        
#lineslist=[]
#numlists=[]
#for line in lines:
    ##line=line[:len(line)-1]
    #lineslist.append(line)
    #print(lineslist)
    #chars=[]
    #for char in line:
        #char=eval(char)
        #chars.append(char)
    ##print(chars)
#print(numlists.append(chars))

#checker=[1,2,3,4,5,6,7,8,9]
#allans=[]
#def horizon(numlists,checker):    
    #ans=[]
    #for i in range (len(numlists)):
        #for j in range (len(checker)):
            #if checker[j] not in numlists[i]:
                #ans.append("y")
                
    #if "y" in ans:
        #allans.append("wrong")
    
#def longi(numlists,checker):   
    #ans2=[]    
    #longitude=[]
    #for a in range (len(numlists)):
        #longs=[]
        #for line in numlists:
            #longs.append(line[a])
        ##print(longs)
        #longitude.append(longs)        
    #print(longitude)
    #for b in range (len(longitude)):
        #for c in range (len(checker)):
            #if checker[c] not in longitude[b]:
                #ans2.append("y")
    #if "y" in ans2:
        #allans.append("wrong")


#longi(numlists,checker)
#if "wrong" in allans:
    #print("Sudoku grid is not valid")
#else:
    #print("Sudoku grid is valid")
    
        
    
        
    



    
