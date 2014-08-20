"""program to ask user to enter strings and list right-aligned 
Thabiso Beau
21 April 2014 
Assignment 6: #question1"""

def main():
    #eerste deel: om die naamlys te programmeer
    naam_1 = [''] #begin die lys 
    naam = input('Enter strings (end with DONE):\n') #moet name insit om lys te begin
    while naam!='DONE': #die 'sentinel' is 'DONE' - onthou dat 'n sentinel loop altyd 'n 'while' loop is!
        naam_1.append(naam) #elke naam word daarin ingesit
        naam=input('') #leeg snaar
        
        #tweede deel: om lys aan die regte kant te hou _ stryk-funksies
    Right_Align=0
    for i in range(len(naam_1)): #loop vir die lys algeheel
        if len(naam_1[i])> Right_Align: #as die woord nou groter as Right_Align is - maak die spasies
            Right_Align= len(naam_1[i]) 
    print()
    print("Right-aligned list:", end='')
    for j in naam_1:
        print(j.rjust(Right_Align))
main()