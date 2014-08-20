def thirtysecRule():
    print("Welcome to the 30 second rule:")
    a=(eval(input(" how long have the cupcakes been on the floor? \n")))
    good= a<=30
        
    if good:
        b=(input("Please advise whether the icing landed top up or top down. t for icing top up and d for icing top down\n"))
        move_on=(b=='t')
        if move_on:
            c=(input(" Did your boss see you, enter yes or no \n"))
            ok=(c=='no')
            if ok:
                print("Safe you can eat them")
            else:
                print("Oooo you could eat them in your meeting but if your boss gets sick your in shit, rather get new ones\n")
        else:
            print(" Well you could just cut off the tops but I wouldn't")
    else:
        print("Eish, buy new ones these are definatley contaminated")

if __name__=='__main__':
    thirtysecRule()