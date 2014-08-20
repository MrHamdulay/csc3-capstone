def print_square():
    print("*****")
    for i in range(0,3):
        print("*   *")
    print("*****")

def print_rectangle(width, height):
    wi= (width)
    he=(height)
    print("*"*wi)
    he2=(he-2)
    for i in range(0,he2):
        print("*"," "*(wi-2),"*",sep='')
    print("*"*wi)    

def get_rectangle(width, height):
    wi= (width)
    he=(height)
    
    he2=(he-2)
    statement="*"*wi+"\n"
    for i in range(0,he2):
        statement=statement+"*"+" "*(wi-2)+"*\n"
    statement=statement+"*"*wi
    return(statement)