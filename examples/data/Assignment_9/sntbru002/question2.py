a = input()
c = input()
lenght = eval(input())
f = open(a,"r")
b = f.read()
#print(b)
f.close()
g = open(c,"w")
dic = b.split(" ")
#new.append(dic)
temp = ""
count=0
for i in dic:
    #temp=""
    count+=1
    if (len(temp)+len(i))+1<=lenght:
        if(len(temp)==0):
            if(i.count('\n')==2):
                temp = temp+""+i
                temp = temp + "%"*lenght
            else:
                temp = temp+""+i.replace('\n',' ')
        else:
            if(i.count('\n')==2):
                temp = i
                #temp = temp + "%"*lenght
            else:
                temp = temp+" "+i.replace('\n',' ')
       # print("L= ",len(temp)," ")
        
            
        #if(len(temp)+len(i))+1<=lenght:
    else:
        print(temp,file=g)
        temp=i.replace('\n',' ')
        if(i.count('\n')==2):
            temp =i #a\n\n
        else:
            temp =i.replace('\n',' ')
if(count==len(dic)):
    print(temp,file=g)
    
g.close()

#print(temp)
