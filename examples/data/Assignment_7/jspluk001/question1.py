'''Luke Joseph
2014-04-28
question 1 of assignment 7'''
def duplicate():
    print("Enter strings (end with DONE):")
    x=""
    y=[]
    while x!="DONE":
        x=input("")
        if x != "DONE":
            y.append(x) # Aquiring inputs 
    l=len(y)
    el=[]
    for i in range(l):
        if y[i] in el:
            pass
        else:
            el.append(y[i]) # Creating list with no duplicates 
    print("\nUnique list:")
    for j in range(len(el)): # producing list without duplicates
        print(el[j])
duplicate()