#question 4
#GLNRUSOO2
#Write a program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT
 
def enter_marks():#input from user

    tmp=""
    names=input("Enter a space-separated list of marks:\n").split(" ")# just used for input
    for i in range(len(names)):#used to convert string numbers into ints
        names[i]=eval(names[i])
    return names

def categorise(names):#sort input into categories
    order={'1':0,'2+':0,'2-':0,'3':0,'F':0}#dELARE CRITERION AND ASSIGN TO ZERO 
    count=[0,0,0,0,0]
    for i in names:
        for j in count:
            if i>=75:                    #first
                count[0]+=1
                order["1"]=count[0]//5
            elif i>=70:                  #second plus
                count[1]+=1
                order["2+"]=count[1]//5
            elif i>=60:                 #second minus
                count[2]+=1
                order["2-"]=count[2]//5
            elif i>=50:
                count[3]+=1
                order["3"]=count[3]//5
            else:
                count[4]+=1
                order["F"]=count[4]//5
                
    return order
def output(order):
    print("1 |"+order["1"]*"X")
    print("2+|"+order["2+"]*"X")
    print("2-|"+order["2-"]*"X")
    print("3 |"+order["3"]*"X")
    print("F |"+order["F"]*"X")
        
if __name__ == "__main__":
    names=enter_marks()
    order=categorise(names)
    output(order)