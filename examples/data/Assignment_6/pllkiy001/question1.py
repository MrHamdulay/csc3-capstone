#program to right allign a list of strings
#kiyarah pillay
#23 april 2014
def main():
    strings=input("Enter strings (end with DONE):\n")
    string_list=[]
    
    if strings=="DONE":
        print("")
        print("Right-aligned list:")
    
    else:
#use DONE as the sentinel value
        while strings!="DONE":
            string_list.append(strings)
            strings=input("")
        
#find the string with the longest length
        width=(max(string_list, key=len))
        print("")
        print ("Right-aligned list:")
        length=len(string_list)
        for i in range (length):
#print the remaining characters (longest string-number of spaces)
            print(" "*(len(width)-len(string_list[i])), string_list[i],sep="")
            
           
main()