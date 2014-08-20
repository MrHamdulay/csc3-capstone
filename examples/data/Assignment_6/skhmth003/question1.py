#Program that right-aligns a list of strings
#21/04/2014
#Gordon Skhosana

def string_collection():
    """Function that collects strings from user and stores them in a list"""
    global strings
    strings=[]
    next_string=""
    first_string=input("Enter strings (end with DONE):\n")
    if first_string!="DONE":
        strings.append(first_string)
        while next_string!="DONE":
                next_string=input("")
                if next_string!="DONE":
                    strings.append(next_string)
                else: break 
        return strings
    else: 
        return ""
    

def max_length():
    """Function that finds the length of the longest string"""
    #Finding the longest string
    strings
    global maximum
    maximum=0
    for i in strings:
        if len(i)>maximum:
            maximum=len(i)
        else: continue
    return maximum    
    
def main():
    """"Function that takes strings and right aligns them according to the longest one"""
    string_collection()
    max_length()
    print()
    print("Right-aligned list:")
    for i in strings:
        print(" "*(maximum-len(i)),i,sep="")
main()        