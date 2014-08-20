# Kimberley Naidoo
# 8 May 2014
# Count pairs of identical strings


count=0
def double_count(string,count):

    if len(string)==1 or len(string)==0: #If string has 1 or 0 letters, no pairs exist
        return count
    
    elif string[0]==string[1]: #If a pair is found, remove and increase count
        count+=1
        return double_count(string[2:],count)
    
    else: #Otherwise remove first letter
        return double_count(string[1:],count)

string=input('Enter a message:\n')
print('Number of pairs:',double_count(string,count))

    