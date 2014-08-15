def input1():
    func=input("Enter a function f(x):\n")
    func=func.lower()
    return func


def plot():

    def f():
      yList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      func=input1()
      func=func.replace("x","(x)")
      for i in range(-10,11):
          x1=str(i)
          yList[(i+10)]=round(eval(str(func.replace("x",x1))))









    for y in range(10,-11,-1):
        displayList=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
        if(y==0):
            for x in range(-10,11):
                if(yList[(x+10)]==0):
                    displayList[(x+10)]="o"
                elif x==0:
                    displayList[(x+10)]="+"
                else:
                    displayList[(x+10)]="-"


        for i in range(21):
          print(displayList[i])
        print()



plot()

# [gvnmer006]
# [question2.py]

count=[0,0,0,0,0,0,0]
list=[500,200,100,50,20,10,5]
#GVNMER006
