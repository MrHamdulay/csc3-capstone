

count=0


def double_count(string,count):

    if len(string)==1 or len(string)==0: 
        return count
    
    elif string[0]==string[1]: 
        count+=1
        return double_count(string[2:],count)
    
    else: 
        return double_count(string[1:],count)



string=input('Enter a message:\n')
print('Number of pairs:',double_count(string,count))

    