#THRIANKA NAIDOO
#NDXTHR005
#Assignment 4
#Question 1

#prints sqaure. 
def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")

#prints rectangle
def print_rectangle(width,height): 
    print(get_rectangle(width,height))
       
#prints rectangle = *
def get_rectangle(width,height): 
    x=height
    oput=""
    for i in range(1,height+1): 
        if i==1: 
            oput+=("*"* width + "\n")
        elif i == height: 
            oput+=("*"* width)    
        else:
            oput+=("*" +(" "*(width-2))+"*"+"\n")
    return oput
