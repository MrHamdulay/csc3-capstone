# Luke Joseph
# Question 3 of assignment 6
# 2014-04-20
def party():
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):")
    x=""
    y=[]
    while x!="DONE":
        x=input("")
        if x != "DONE":
            y.append(x) # Aquiring names of parties 
    l=len(y)
    el=[]
    a=0
    formata= '{0:<11}' #formatting output into correct layout
    for i in range(l):
        if y[i] in el:
            a+=1
        else:
            el.append(y[i])
    el.sort()
    print("\nVote counts:")
    for j in range(len(el)): # production of outputs
        print(formata.format(el[j]),end="")
        print("-",y.count(el[j]))
party()