'''Counting pairs of repeated characters
09/05/10
Limpho Parkies'''

string=input('Enter a message:\n')

n=0
pairs=0

def count(string,n):
    if len(string)<=1:
        return n
    else:
        if string[0]==string[1]:
            n+=1
            return count(string[2:],n)
        else:
            return count(string[2:],n)

print('Number of pairs:',count(string,0))