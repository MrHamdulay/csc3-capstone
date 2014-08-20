"""Program to count number of pairs within string
Pankaj Munbodh
7 May 2014"""


get_str=input('Enter a message:\n')
paircount={}             #create dictionary
paircount['pairs']=0     #count set to 0
def countpairs(string):
    if len(string)==2:            #stopping case so that recursion ends
        if string[0]==string[1]:  #compare first and second characters of string
            paircount['pairs']+=1     
            return paircount
    elif len(string)==1:          #stopping case. The stopping case which will execute depends on length of string supplied to program
        return paircount
    
    elif string[0]==string[1] or (string[0]!=string[1] and string[1]==string[2]): # The statement after the 'or' caters for the case when second character is equal to third. This is important because we are recursing by chopping off 2 characters at beginning each time.
        paircount['pairs']+=1
        countpairs(string[2::])
    else:
        countpairs(string[2::])
countpairs(get_str)

#Output
pairs_number=paircount['pairs']
print('Number of pairs:',pairs_number)
