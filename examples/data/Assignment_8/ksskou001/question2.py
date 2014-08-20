'''This program counts the number of pairs of repeated characters in a string
without overlap using a recursive function
By Hermann KOUASSI: KSSKOU001
On 3 May 2014'''

def pairs(the_str, counter):
    '''count the number of pairs of repeated characters in a given string'''
    
    #stop condition: when string remains only one character or if empty string is input
    if len(the_str) == 1 or the_str == '':
        print('Number of pairs:',counter)
    #when string is more than one character, compare first and second character,
    else:
        # if equallity incremente counter by one and call pairs to carry one counting 
        if the_str[0]==the_str[1]:
            counter += 1
            #new string leaves off the two counted characters to avoid overlap 
            pairs(the_str[2:], counter)
        else:
            #leave out just one character not to skip a repeated character
            pairs(the_str[1:], counter)

def main():
    '''main function creates a variable counter to avoid a global variable and then trouble'''
    counter = 0
    #get string
    the_str = input('Enter a message:\n')
    #call recursive function
    pairs(the_str, counter)
    


if __name__=="__main__":
    main()