def main():
    msg = input("Enter the message:\n")
    rep = int(input("Enter the message repeat count:\n"))
    thick = int(input("Enter the frame thickness:\n"))
    num = len(msg)
    dash = num + thick*2
    x = 0
    
    for top in range(thick):
        print("|"*x + "+" + dash*"-" + "+" + "|"*x)
        dash -= 2
        x+=1
        
    for words in range(rep):    print("|"*x,msg,"|"*x)
    for bot in range(thick): 
        x -=1
        dash += 2
        print("|"*x + "+" + "-"*dash + "+" + "|"*x)
        
        
main()