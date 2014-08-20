#Thembekile Dubazana
#DBZPHI002

word=input('Enter the message:\n')
r=eval(input('Enter the message repeat count:\n'))
w=eval(input('Enter the frame thickness:\n'))

i=0
j=0
l=len(word)+2*w
k=w-1
word=" %s "%word #spacing of word

while i < w:#while loop for top
    print('|'*i,'+','-'*l,'+','|'*i,sep="")
    l=l-2
    i=i+1
    if i == w:#while loop for message and repeat
        while j < r: 
            print('|'*w +word+'|'*w)
            j=j+1
            if j == r:
                l=l+2
                while k > -1:#while loop for bottom
                    print('|'*k,"+",'-'*l,'+','|'*k,sep="")
                    l=l+2
                    k=k-1
        