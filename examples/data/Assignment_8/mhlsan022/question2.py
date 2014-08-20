'''This function checks if a string has double letters and returns the number of double letters
Sandile Christopher Mahlangu
4May 2014'''

#count starts off as 0
count=0
def double_count(string,count):
    '''This function returns The number of double letters in a string using recursion'''
    if len(string)==1 or len(string)==0:#If there's only one letter left return the numbers of doubles
        return count
    elif string[0]==string[1]:#If consecutive letters are found, slice them and add 1 to count.
        count+=1
        return double_count(string[2:],count)
    else:#Otherwise remove the first letter
        return double_count(string[1:],count)
if __name__=='__main__':
    string=input('Enter a message:\n')
    print('Number of pairs:',double_count(string,count))