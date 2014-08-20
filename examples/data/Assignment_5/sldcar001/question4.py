def txtG():
    fx=input("Enter a function (fx):\n")
    gx=fx.replace('x','a')
    #fhold=10
    b=0
    for i in range(-10,11):
        x=i
        #a=i
        #G=eval(gx)
        F=eval(fx)
        for j in range(-10,11): 
            a=j
            G=eval(gx)
            if F in range(-10,11):
                if F==G and x!=a:
                    F,x,a=F,x,a
                else:
                    F=F
                
            else:
                F=b
        
        print(F,x,a)
        b+=1
                
        
        #if F in range(-10,11):
               # F=F
       # else:
       #     F="null"
       # print(F,x)
    
txtG()