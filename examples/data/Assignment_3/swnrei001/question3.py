def frameMessage(message, repeat, thickness):
    for i in range(thickness):
        print('|' * i + '+' + ('-'*(len(message) + 2* (thickness - i))) + '+' + '|' * i)
    for i in range(repeat):
        print('|' * thickness, message, '|' * thickness)
    for i in range(thickness):
        print('|' * (thickness - i - 1) + '+' + ('-'*(len(message) + 2 * (i+ 1))) + '+' + '|' * (thickness - i - 1)) 

if __name__ == '__main__':
    msg = input("Enter the message:\n")
    repeat = eval(input("Enter the message repeat count:\n"))
    thickness = eval(input("Enter the frame thickness:\n"))
    frameMessage(msg, repeat, thickness)