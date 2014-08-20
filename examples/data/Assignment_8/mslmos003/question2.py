#Rorisang Moseli
#May 2014
#Count repeated pairs in a string


def repeated_pairs(string,count):
    if len(string)>=2:
        #evaluates input to classify it is a string
        if string[0]==string[1]:
            return repeated_pairs(string[2:],(count+1))
        if string[0]!=string[1]:
            return repeated_pairs(string[1:],count)
    else:
        print("Number of pairs:",count)

  
string = str(input("Enter a message:\n")) #user input calls function and is evaluated
repeated_pairs(string,0)
