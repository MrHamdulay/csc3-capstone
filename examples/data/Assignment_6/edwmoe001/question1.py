"""Program to input string list and then right aliggn with longest string
Tauhir Edwards
4/22/2014"""
#function to return longest string position in list    
def longest_string(array):
    length = 0
    for i in range(len(array)):
        current_str_len = len(array[i])
        if current_str_len > length:
            length = current_str_len
        else:
            pass
    return length
#takes parameters of array and length and uses this to calculate spaces required for right alignment
#according to longest str in list, and adds them to each str.
def right_aligner(array,length):
    for i in range(len(array)):
        if len(array[i]) == length:
            pass
        else:
            spaces = length - len(array[i])
            array[i] = " "*spaces + array[i]
    return array

def main():
    string_list = []
    name =""
    print("Enter strings (end with DONE):")
    #while loop to add values to list
    while name != "DONE":
        name = input()
        string_list.append(name)
    print()    
    print("Right-aligned list:")
    length = longest_string(string_list)
    right_list = right_aligner(string_list,length)
    del right_list[-1] #removes DONE
    for i in range(len(right_list)):
        print(right_list[i])
        
main()

