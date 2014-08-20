message=input('Enter the message:\n')
repeat_count=eval(input('Enter the message repeat count:\n'))
frame_thick=eval(input('Enter the frame thickness:\n'))
message_fin=str(' ')+message+str(' ')                
frame_thick2=frame_thick*2

frame_width=frame_thick2+len(message_fin)
centre_thick=frame_width-2
side=0

for i in range(frame_thick):
    print('|'*side,'+','-'*centre_thick,'+','|'*side,sep='')
    side+=1
    centre_thick-=2
    

for i in range(repeat_count):
    print('|'*frame_thick,message_fin,'|'*frame_thick,sep='')

centre_thick+=2
side-=1
for i in range(frame_thick):
    print('|'*side,'+','-'*centre_thick,'+','|'*side,sep='')
    side-=1
    centre_thick+=2
    
    







#side=0
#while frame_width>len(message_fin):
    #print('|'*side,'+','-'*(frame_width-1),'+', '|'*side,sep='')
    #frame_width-=1
    #side+=1
