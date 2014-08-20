# Program to count the number of pairs of repeated characters in a string
# Nomsa Gamedze
# 7 May 2014

def count_pairs(string, i, count):
    count = count
    x = len(string) - 1
    global saved_count
    saved_count = count
    if i < x:
        if string[i] == string[i+1]:
            count += 1
            i += 2
            saved_count = count
            count_pairs(string, i, count)
            return saved_count
        else:
            i += 1
            count_pairs(string, i, count)
            return saved_count
        
def main():
    string = input("Enter a message:"'\n')
    global count
    count = 0
    pairs = count_pairs(string, 0, count)
    print("Number of pairs:", pairs)
        
main()