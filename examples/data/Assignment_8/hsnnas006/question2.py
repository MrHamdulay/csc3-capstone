'''program to recursively count number of pairs of repeated characters
nasreen hoosain
06/05/14'''

#recursive function to count repitition of characters
def count_repeat (string):
    count = 0
    if len(string) == 0 or len(string) == 1: #no double characters
        return 0
    elif string[0] != string[1]:
        return count_repeat(string[1:])
    else:
        count += 1 #increase the counter and return
        return count + count_repeat(string[2:])#cuts off the pair before recursing

if __name__ == '__main__':
    string = input('Enter a message:\n')
    print('Number of pairs:', count_repeat(string))