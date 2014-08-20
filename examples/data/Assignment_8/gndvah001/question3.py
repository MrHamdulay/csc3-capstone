"""message thing
Vahin Gounden
2014-05-07"""

def main():
    word = input("Enter a message:\n")
    w = len(word)      
    counter = 0
    x = 0
    print("Encrypted message:")
    palin(word,w,counter,x)
       
def palin(word,w,counter,x): 
    if counter < w:
        x = ord(word[counter])
        if x == 122:
            x -= 26
        if x == 32 or x == 46 or x in range (65,90):
            x -= 1
        x += 1
        print(chr(x),end = "")
        palin(word,w,counter + 1,x)

    
        
            
main()
