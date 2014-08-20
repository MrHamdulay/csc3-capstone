def frame():
    message = input("Enter the message:\n")
    messagerepeat = eval(input("Enter the message repeat count:\n"))
    frame = eval(input("Enter the frame thickness:\n")) * 2
    tempframe = frame
    count = 0   
    
    for i in range(frame//2):
            print(count*'|','+',(len(message)+(tempframe - count*2))*'-','+', count*'|',sep = "")
            count += 1
        
    for j in range(messagerepeat):
            print('|' * (frame//2), message, '|' * (frame//2))
    
    for k in range(frame//2):
            print((count-1)*'|','+',(len(message)+(tempframe - (count-1)*2))*'-','+', (count-1)*'|',sep = "")
            count -= 1          
                
frame()
        
    
