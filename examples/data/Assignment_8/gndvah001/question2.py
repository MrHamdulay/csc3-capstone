"""message thing
Vahin Gounden
2014-05-07"""

def main():
    word = input("Enter a message:\n")
    w = len(word)      
    counter = 0
    counter2 = 1
    counter3 = 0
    palin(word,w,counter,counter2,counter3)
       
def palin(word,w,counter,counter2,counter3): 
    if counter2 < w:
        if word[counter] == word[counter2]:
            counter3 += 1
            counter += 1
            counter2 += 1
        palin(word,w,counter + 1,counter2 + 1,counter3)
    if counter2 == w:
        print("Number of pairs:",counter3)
    
        
            
main()
