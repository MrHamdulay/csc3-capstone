#dhriven hamlall

def input1():
    message=input("Enter a message:\n")
    return message
    

def count(a):
    if len(a)<2:
        return 0
    elif a[0]==a[1]:
        return 1+count(a[2:])
    else:
        return count(a[1:])
    

print("Number of pairs:",count(input1()))