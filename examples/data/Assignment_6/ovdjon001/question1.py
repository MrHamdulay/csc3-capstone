""" Question 1 
20 April 2014
Jonathan Ovadia"""
import math
def format_list(l):
    output = ""
    if len(l) > 0:
        longest_word = max(l, key=len)
        for i in range(len(l)):
            output+= " "*(int(len(longest_word) - len(l[i]))) + l[i] + "\n"
    return output

def main():
    print("Enter strings (end with DONE):")
    strings = []
    line = input("")
    while line !="DONE":
        strings.append(line)
        line = input("")
    else:
        print("\nRight-aligned list:")
        print(format_list(strings))

main()                   
