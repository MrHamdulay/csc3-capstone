
#kereshnee pillay
#7 may
#checking an returning the number of double letters in a string

#initial count
count=0
def double(string,count):
#if theres one letter then count remains 0
    if len(string)==1 or len(string)==0:
        return count
#when two lettere=s are equal, add to count    
    elif string[0]==string[1]:
        count+=1
        return double(string[2:],count)
#if not return from the next letter    
    else:
        return double(string[1:],count)
if __name__=='__main__':
    string=input('Enter a message:\n')
    print('Number of pairs:',double(string,count))