#konrad Hugo
#question1
#25 April 2014
string_list = []   

end = False

print('Enter strings (end with DONE):')

while not end:
        string_input = input('') #strings inputed by user
        if string_input == 'DONE': #escape word
                end = True #This breaks the loop
        else:
                string_list.append(string_input) #
      
#This part is responsible for the alignment                
def align_func():
        maximum=''
        for i in string_list: #loop to find the word with max length
                if len(i) > len(maximum): 
                        maximum = i
        return len(maximum)

maximum_len = align_func()

print("\nRight-aligned list:")
for i in string_list: #loops through each word
        print("{0:>{length}}".format(i,length=maximum_len)) #formats list to the right hand side
        