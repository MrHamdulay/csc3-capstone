def get_integer (x):
        y=input("Enter " + x + ":\n")
        while not y.isdigit():
                y=input("Enter " + x + ":\n")
        x=eval(y)
        return (x)

def calc_factorial (x):
        i=1
        y=x
        while i<y:
                x=x*i
                i=i+1
        return (x)