# Program that prints a frame around a message. 
# Name: Othniel KONAN
# Student number: KNNOTH001
# Date: 20/03/2014

def frameUp(nFrame,lenWord):
    for i in range(nFrame):
        print('|'*i,'+','-'*(2*(nFrame-i)+lenWord),'+','|'*i,sep='')
        
def frameDown(nFrame,lenWord):
    for i in range(nFrame-1,-1,-1):
        print('|'*i,'+','-'*(2*(nFrame-i)+lenWord),'+','|'*i,sep='')

def frameMiddle(nFrame,nRepeat,word):
    for i in range(nRepeat):
        print('|'*nFrame,' ',word,' ','|'*nFrame,sep='')
        
word = input('Enter the message:\n')
nRepeat = eval(input('Enter the message repeat count:\n'))
nFrame = eval(input('Enter the frame thickness:\n'))
lenWord = len(word)

frameUp(nFrame,lenWord)
frameMiddle(nFrame,nRepeat,word)
frameDown(nFrame,lenWord)