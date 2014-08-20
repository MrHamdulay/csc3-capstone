# Program that re-prints list with no duplicates
# Cameron Collum
# 29 April 2014
lis=[ ]
string=input("Enter strings (end with DONE):\n")
lis.append(string)
if string=="DONE":
        print()
        print("Unique list:")        
else:
        while string !="DONE":
                string=input()
                lis.append(string)
                #del lis[len(lis)-1] #-1 because list starts at 0, deletes word DONE
        del lis[len(lis)-1]
        print()
        print("Unique list:")
        lis_new=[ ]
        for i in lis:
                if i in lis_new:
                        continue
                else:
                        lis_new.append(i)
        for i in lis_new:
                print(i)