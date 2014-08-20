"""Program for lists1
Julian Albert
ALBJUL005
2014-04-20"""

list_of_strings = []   
end = False

print('Enter strings (end with DONE):')
while not end:
        string = input('') #input from user
        if string == 'DONE':
                end = True #ends string request
        else:
                list_of_strings.append(string) #appends input
      
#defines the alignment                
def right_len():
        longest=''
        for i in list_of_strings:
                if len(i) > len(longest):
                        longest = i
        return len(longest)

max_len = right_len()

print("\nRight-aligned list:")
for i in list_of_strings:
        print("{0:>{width}}".format(i,width=max_len)) #formats to the right
        