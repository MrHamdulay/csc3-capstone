__author__ = 'TMPSTE002 - Stephen Temple'

def printMessage(message, repeat, frame):
    length = len(message) + (2*frame) + 2
    for i in range(frame):
        if i == 0:
            print('+' + '-'*(length-2) + '+')
        else:
            print('|'*(i) + '+' + '-'*(length-(2*i)-2) + '+' + '|'*(i))

    for i in range(repeat):
        print('|'*frame + ' ' + message + ' ' + '|'*frame)

    for i in range(frame-1, -1, -1):
        if i == 0:
            print('+' + '-'*(length-2) + '+')
        else:
            print('|'*(i) + '+' + '-'*(length-(2*i)-2) + '+' + '|'*(i))


if __name__ == '__main__':
    message = input("Enter the message:\n")
    repeat = eval(input("Enter the message repeat count:\n"))
    frame = eval(input("Enter the frame thickness:\n"))
    printMessage(message, repeat, frame)