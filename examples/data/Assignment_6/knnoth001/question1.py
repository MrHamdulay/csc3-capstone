''' Print a list of names from the right end to the left
Othniel KONAN
KNNOTH001
2014/04/19'''

#CREATION OF VARABLE
len_list=[]
array=[]

#ENTER THE LKST OF STRING
lt = input('Enter strings (end with DONE):\n')
t_list = []
while lt != 'DONE':                                             #Continue to take strings whle the user does not enter 'DONE'
    t_list.append(lt)
    lt = input()

#SAVE THE LENGTH OF EACH STRING
for a in t_list:
    len_list.append(len(a))                                     #Save the length of each string

#KEEP TRACK OF THE LONGEST STRING
a=0
for i in range(len(len_list)):
    if len_list[i]>a:                                           #Record a as the longuest string
        a=len_list[i]
        j=i

#CREATE AN 2D ARRAY OF len(t_list) by longuest string
for a in range(len(t_list)):                    
    array.append([' ']*len_list[j]) 
    

#INSERT THE LIST IN THE ARRAY
for i in range(len(t_list)):
    for k in range(len_list[i]):
        array[i][len_list[j]-k-1]=t_list[i][len(t_list[i])-1-k] #Add the string strating from the right end to the left
        
#PRINT THE RIGHT LIST
print('\nRight-aligned list:')
for x in range(len(t_list)):
    for y in range(len_list[j]):
        print(array[x][y],end='')
    print()
    