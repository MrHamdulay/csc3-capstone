"""Using recursion to count the number of character pairs in a string
Carla Wilby
4th April 2014"""

string_in = input("Enter a message:\n")
tracker = 0 #tracks progress through string_in
count_pairs = 0

def repeat_check(tracker,count_pairs):
    if tracker<(len(string_in)-1): #while tracker is still in range
        if string_in[tracker] == string_in[tracker+1]:
            count_pairs+=1 #count the pair
            tracker+=2 #prevent rechecking the same character in case of three of the same
            repeat_check(tracker,count_pairs)
        else:
            tracker+=1 #move on to next character
            repeat_check(tracker,count_pairs)
    else:
        print("Number of pairs: "+str(count_pairs))

if __name__ == '__main__':     
    repeat_check(tracker,count_pairs)    