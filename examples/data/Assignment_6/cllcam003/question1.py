# Program that right aligns entered strings
# Cameron Collum
# 23 April 2014
lis=[ ]
string=input("Enter strings (end with DONE):\n")
lis.append(string)
if string=="DONE":
        print()
        print("Right-aligned list:")        
else:
        while string !="DONE":
                string=input()
                lis.append(string)
                #del lis[len(lis)-1] #-1 because list starts at 0, deletes word DONE
        del lis[len(lis)-1]
        print()
        print("Right-aligned list:") 
        longest=len(max(lis, key=len))
        for i in lis:
                print(i.rjust(longest, " ")) # aligns it to right

    
    


        


    