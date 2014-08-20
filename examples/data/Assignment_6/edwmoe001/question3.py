"""Program to count votes
2014-04-23
Tauhirah Eguardo"""
from collections import Counter

def organiser(array,orig):
        #use counter function on original list, to get values in new list
        #
        x = Counter(orig)
        for i in range(len(array)):
                array[i] = "{:<10}".format(array[i]) +" - " + str(x[array[i]])
                i += 1    
    
#found fastest method using fromkeys() to remove duplicates in list.
#http://www.peterbe.com/plog/uniqifiers-benchmark
#Better than original cleaner, runs much much faster.
def cleaner(seq):
    
        return sorted({}.fromkeys(seq).keys())

def main():
        string_list = []
        name =""
        print("Independent Electoral Commission\n"
              "--------------------------------\n"
              "Enter the names of parties (terminated by DONE):")
        #while loop to add values to list
        while name != "DONE":
                name = input()
                string_list.append(name)
        del string_list[-1]
        new_list = cleaner(string_list)
        organiser(new_list,string_list)
        print()
        print("Vote counts:")
        for i in range(len(new_list)):
                print(new_list[i])
main()