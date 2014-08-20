#MHDLLO001
#18 May 14
#Reformatting

filename = input("Enter the input filename:\n")

f = open(filename,"r")

output = input("Enter the output filename:\n")


k = open(output,"w")


text=f.read()

position=0

num=-1

limit = eval(input("Enter the line limit:\n"))

length=len(text)
i=0
while(i<length):
    i=i+1

    if(i==len(text)-1):

            x=[]
            x.append(text[num+1])

            for j in range(num+2,i):

                if(text[j]!='\n'):

                    x.append(text[j])

                else:

                    x.append(" ")

            x.append(text[i])      

            for j in x:

                print(j,end='',file=k)

                

    elif(text[i+1]=="\n" and text[i]=="\n"):

        x=[]

        x.append(text[num+1])

        for j in range(num+2,i):
            t=text[j]
            if(t!='\n'):
                x.append(t)

            else:

                x.append(" ")

        x.append(text[i])

        for j in x:

            print(j,end='',file=k)

        print("",file=k)        

        

        num=i+1     

    

    elif(text[1+i]==" " and i==limit+num):

        x=[]
        x.append(text[num+1])

        for j in range(num+2,i):
            t2=text[j]

            if(t2!='\n'):

                x.append(t2)

            else:

                x.append(" ")

        x.append(text[i])

        for j in x:

            print(j,end='',file=k)
        print("",file=k)        

        

        num=i+1

    

    elif(text[i+1]!=" " and i==num+limit):       

        for j in range(i,num,-1):

            if(text[j]==" " or text[j]=="\n"):

                position=j

                break

        x=[]

        x.append(text[num+1])
        for j in range(num+2,position-1):

            if(text[j]!='\n'):

                x.append(text[j])

            else:

                x.append(" ")

        x.append(text[position-1])        
        for j in x:

            print(j,end='',file=k)

        print("",file=k)

        num=position

        
f.close()

k.close()