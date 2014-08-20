marx = (input("Enter a space-separated list of marks:\n"))
marx = marx.split(' ')


marx_fail=[]
marx_3rd=[]
marx_lsec=[]
marx_usec=[]
marx_1st=[]
for i in marx:
    if i < "50":
        marx_fail.append(i)
    elif i >= "50" and i < "60":
        marx_3rd.append(i)
    elif i >= "60" and i < "70":
        marx_lsec.append(i)
    elif i>= "70" and i <"75":
        marx_usec.append(i)
    elif i >= "75":
        marx_1st.append(i)
        
print("1 |" , "X"*len(marx_1st) , sep='')
print("2+|" , "X"*len(marx_usec) , sep = '')
print("2-|" , "X"*len(marx_lsec) , sep='')
print("3 |" , "X"*len(marx_3rd) , sep='')
print("F |" , "X"*len(marx_fail) , sep='')


      
      
    
