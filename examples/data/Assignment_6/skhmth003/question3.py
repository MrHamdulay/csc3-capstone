# Program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT
#21/04/2014
#Gordon Skhosana

def parties():
    """Function that collects party names"""
    global parties
    parties=[]
    next_party=""
    first_party=input("Enter the names of parties (terminated by DONE):\n")
    if first_party!="DONE":
        parties.append(first_party)
        while next_party!="DONE":
            next_party=input("")
            if next_party!="DONE":
                parties.append(next_party)
            else: break
        return parties.sort()
    else: return ""
def unique_parties():
    """Function that finds the names of all the different parties"""
    print("Independent Electoral Commission")
    print("--------------------------------")
    parties()
    print()
    print("Vote counts:")
    counters={}
    parties.sort()
    for word in parties:
        if not word in counters:
            counters[word]=0
            counters[word]+=1
        else: counters[word]+=1
    temp_names=list(counters.keys())
    names=list(counters.keys())
    count=list(counters.values())
    names.sort()
    for i in range(len(names)):
        for j in range(len(names)):
            if names[i]==temp_names[j]:
                present_count=count[j]
                names_frmat="{0:10}".format(names[i])
                print(names_frmat,"-",present_count)
            else:continue  
unique_parties()