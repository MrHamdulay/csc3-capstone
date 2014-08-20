#Shaaheen Sacoor SCRSHA001
#19 April 2014
#Program to enter a right aligned list of names

def main():
    list_string =[] # Empty list to add into later
    strings = input("Enter strings (end with DONE):\n")
    if strings == "DONE":
        print("")
        print("Right-aligned list:")
    else:
        while strings!="DONE":
            list_string.append(strings) # Adds strings to list
            strings = input("")
            
        print("\nRight-aligned list:")
        lengthlist=[]
        for i in range(len(list_string)): #To find longest word from the list for the aligning
            lengthlist.append(len(list_string[i]))
            lengthlist.sort()
            lengthlist.reverse()
            longest_length =lengthlist[0]
            rightalign = '{:>'
            rightalign += str(longest_length)
            rightalign += '}'
        for i in range(len(list_string)): #Goes through list 
            print(rightalign.format(list_string[i]))
    
main()
        
