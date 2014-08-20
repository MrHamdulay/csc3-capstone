""" a program where the user can enter a list of strings followed by the sentinel "DONE
Fadzai Mupfunya
21/04/14"""
#to get the list of strings from the user

lists=[]
string_list=input("Enter strings (end with DONE):\n")
while string_list != "DONE":
        lists.append(string_list)
        string_list=input("")
print()
   
        
#to find the longest string   
if len(lists)!=0:
        longest_string=(max(lists, key=len))
        length=len(longest_string)
else:
        length=0
    

#to print out the strings 
if length==0:
        print("Right-aligned list:")
        print()
else:
        print("Right-aligned list:")
        for string in lists:
                right_aligned = '{0:>{1}}'.format(string ,length) #to right align the strings by the longest string
                print(right_aligned)    
        

