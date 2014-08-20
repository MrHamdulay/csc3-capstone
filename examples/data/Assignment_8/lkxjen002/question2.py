#A program to count the number of pairs
#Created by:Jenna Lake
#Date: 4/5/2014

def repeated_letters(string1, new_list, count):
    if len(string1)>0: #if length of string not 0 then there are still characters to be checked
        if len(new_list)==0:#if nothing has been appended to newlist then first character is automatically appended
            new_list.append(string1[0])
        elif string1[0]!=new_list[len(new_list)-1]: #if the first character is not equal to the last letter new list(ie characters arent adjacent), append character to list
            new_list.append(string1[0])
        else: #if characters are adjacent(first character is not equal to the last letter new list)
            if  string1[0]==new_list[len(new_list)-1]:
                new_list.remove(string1[0]) # remove character from new_list
                count+=1
        string1=string1[1:len(string1)] #cut off first letter of the string for each recursion,such that one by one each character is checked
        return repeated_letters(string1, new_list, count)
    if len(string1)==0: # if the length of the original string is 0, then all characters have been checked, thus return a value for count
        return count

def main():
    string1=input("Enter a message:\n")
    new_list=[]
    count=0
    print("Number of pairs:",repeated_letters(string1, new_list, count)) #prints returned value of count
main()