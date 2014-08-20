# a program that asks a series of questions to determine if you should eat the food or not
# mashau zwivhuya
# 7 march 2014
one="Did anyone see you? (yes/no)\n"
two="Was it a boss/lover/parent? (yes/no)\n"
three="Was it expensive? (yes/no)\n"
four="Can you cut off the part that touched the floor? (yes/no)\n"
five="Is it chocolate? (yes/no)\n"
six="Was it sticky? (yes/no)\n"
seven="Is it a raw steak? (yes/no)\n"
eight="Are you a puma? (yes/no)\n"
nine="Did the cat lick it? (yes/no)\n"
ten="Is your cat healthy? (yes/no)\n"
ele="Is it an Emausaurus? (yes/no)\n"
twe="Are you a Megalosaurus? (yes/no)\n"
no="Decision: Don't eat it."
maybe="Decision: Your call."
yes="Decision: Eat it."
def main():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    see=input(one)
    if see =="yes":
        lover=input(two)    
        if lover=="yes":
            expensive=input(three)
            if expensive=="yes":
                floor=input(four)
                if floor=="yes":
                    print(yes)
                elif floor=="no":
                    print(maybe)
                else:
                    print()
            elif expensive=="no":
                choc=input(five)
                if choc=="yes":
                    print(yes)
                else:
                    print(no)
        else:
            print(yes)
    elif see=="no":
        sticky=input(six)
        if sticky=="no":
            emaus=input(ele)
            if emaus=="yes":
                mega=input(twe)
                if mega=="yes":
                    print(yes)
                else:
                    print(no)
            elif emaus=="no":
                cat=input(nine)
                if cat=="yes":
                    health=input(ten)
                    if health=="yes":
                        print(yes)
                    elif health=="no":
                        print(maybe)
                elif cat=="no":
                    print(yes)
        if sticky=="yes":
            steak=input(seven)
            if steak=="yes":
                puma=input(eight)
                if puma=="yes":
                    print(yes)
                elif puma=="no":
                    print(no)
            elif steak=="no":
                lick=input(nine)
                if lick=="no":
                    print(yes)
                elif lick=="yes":
                    hea=input(ten)
                    if hea=="yes":
                        print(yes)
                    elif hea=="no":
                        print(maybe)
                    
main()    