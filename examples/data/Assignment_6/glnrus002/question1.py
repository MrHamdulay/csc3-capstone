#glnrus002
#question 1
# April 22
#Write a Python program where the user can enter a list of strings followed by the sentinel "DONE" and the list of strings is then printed out right-aligned with the longest string.

def get_names():#from user
    names={}
    i=0
    tmp=""
    print("Enter strings (end with DONE):")
    while tmp !="DONE":
        tmp=input()
        names[i]=tmp
        i+=1
    del names[len(names)-1]
    return names

def get_longest(names):# finds longest word in list
    long=0#used to carry longest value for comparison
    place=0#used to keep track of which position in loop is the longest word at
    for i in names:
        if len(names[i])>long:
            place=i
            long=len(names[i])
    return place
    

if __name__== "__main__":
    names=get_names()
    if len(names)!=0:#only if list is NOT empty, do following:
        place=str(len(names[get_longest(names)]))
        form="{0:>"+place+"}"   
        print("\nRight-aligned list:")
        for i in range(len(names)):
            print(form.format(names[i]))
    else:
        print("\nRight-aligned list:")
