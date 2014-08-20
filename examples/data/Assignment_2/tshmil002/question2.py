#A program to determine whether dropped food should be eaten or not.
#Mila Tshaka
#10/03/2014

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

#seen* sticky* steak* person* expensive* chocolate* puma* cat_lick* emausaurus* megalosaurus* cat_healthy* cut_off*
decision_a,decision_b,decision_c="Eat it.","Don't eat it.","Your call."
seen=input("Did anyone see you? (yes/no)\n")

if seen=="yes":
        person=input("Was it a boss/lover/parent? (yes/no)\n")
        if person=="yes":
                expensive=input("Was it expensive? (yes/no)\n")
                if expensive=="yes":
                        cut_off=input("Can you cut off the part that touched the floor? (yes/no)\n")
                        if cut_off=="yes":
                                print("Decision:",decision_a)
                                
                        else:
                                
                                print("Decision:",decision_c)
                else:
                        chocolate=input("Is it chocolate? (yes/no)\n")
                        if chocolate=="yes":
                                print("Decision:",decision_a)
                        else:
                                print("Decision:",decision_b)  
        else:
                print("Decision:",decision_a)
                
elif seen =="no":
                sticky=input("Was it sticky? (yes/no)\n")
                if sticky=="yes":
                        steak=input("Is it a raw steak? (yes/no)\n")
                        if steak=="yes":
                                puma=input("Are you a puma? (yes/no)\n")
                                if puma=="yes":
                                        print("Decision:",decision_a)
                                else:
                                        print("Decision:",decision_b)
                        else:
                                cat_lick=input("Did the cat lick it? (yes/no)\n")
                                if cat_lick=="yes":
                                        cat_healthy=input("Is your cat healthy? (yes/no)\n")
                                        if cat_healthy=="yes":
                                                print("Decision:",decision_a)
                                        else:
                                                print("Decision:",decision_c)
                                else:
                                        print("Decision:",decision_a)
                else:
                        emausaurus=input("Is it an Emausaurus? (yes/no)\n")
                        if emausaurus=="yes":
                                megalosaurus=input("Are you a Megalosaurus? (yes/no)\n")
                                if megalosaurus=="yes":
                                        print("Decision:",decision_a)
                                else:
                                        print("Decision:",decision_b)
                        else:
                                cat_lick=input("Did the cat lick it? (yes/no)\n")       
                                if cat_lick=="yes":
                                        cat_healthy=input("Is your cat healthy? (yes/no)\n")
                                        
                                        if cat_healthy=="yes":
                                                print("Decision:",decision_a)
                                                                                                
                                        else: 
                                                print("Decision:",decision_c)
                                else:
                                        print("Decision:",decision_a)
                                                                                                               
                                                                                                                                            
                                                                
                                
                        
                        
                    
