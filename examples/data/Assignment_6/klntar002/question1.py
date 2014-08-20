# tarisai kalinde 
# klntar002
# Right alignment of a list of words ,according to the longest word

enter_string=input('Enter strings (end with DONE):\n')   # for the string statements

end_array=[]                                             # initialization of the final array
while enter_string!='DONE':                              # while loop so that the input process can continue as long as 'DONE' is not entered
    
    end_array.append(enter_string)                       # adding each input to the array
    enter_string=input('')
    
# finding the maximum length of the or the array list    
max_len=0                                                # initial max length= 0                                       
for i in end_array:                                      # going thru each word in the array
    if len(i)>max_len:
        max_len=len(i)                                   # appointing the biggest length to variable 'max_len'
               
print('\nRight-aligned list:')
for k in end_array:
    difff=max_len-len(k)                                 # space calculation for correct alignment
    
    print(' '*difff,k,sep='')                            # printing the words i the required right alignment  (end of prog)
        

    
    
    

