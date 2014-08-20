def mess():
    message = input('Enter the message:\n')
    count = input('Enter the message repeat count:\n')
    thick = input('Enter the frame thickness:\n')
    plus = '+'
    dash = '-'
    constant = 2*eval(thick)
    bar = '|'
    for i in range(eval(thick)):
        frame = bar*i + plus + dash*(len(message)+constant) + plus + bar*i
        print(frame)
        constant-=2
    for i in range(eval(count)):
        print(bar*eval(thick),message,bar*eval(thick))
    constant2 = 2
    for i in range(eval(thick)-1,-1,-1):
        frame = bar*i + plus + dash*(len(message)+constant2) + plus + bar*i
        print(frame)
        constant2+=2    
    

mess()