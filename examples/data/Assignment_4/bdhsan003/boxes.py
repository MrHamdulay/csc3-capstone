def print_square():
    print(5*"*")
    
    for i in range(3):
        print("*   *")
    print(5*"*")

def print_rectangle(wdh,hgh):
    print(wdh*"*")
    for i in range(hgh-2):
        print("*"+(wdh-2)*" "+"*")
    print(wdh*"*")

def get_rectangle(wdh,hgh):
    fig = (wdh*"*")
    for i in range(hgh-2):
        fig = fig + ("\n*"+(wdh-2)*" "+"*")
    fig = fig + ("\n"+wdh*"*")
    return fig
