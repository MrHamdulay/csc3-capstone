#A program to encrypt a message by converting all lowercase characters to the next character 
#Created by:Jenna Lake
#Date: 4/5/2014

def convert_letter(list1, new_list):
    if len(list1)>0:
        if list1[0].islower(): #only converts lowercase letters
            if list1[0]=='z': #if character is a 'z', the corresponding shifted value is 'a'
                x='a'
            else:
                x=chr(ord(list1[0])+1)
        else:
            x=list1[0]
        new_list.append(x)
        list1=list1[1:len(list1)]
        return convert_letter(list1, new_list) #recursion through each letter of the list
    else:
        return new_list
    
def print1(new_list): #prints each individual letter of the converted list
    if len(new_list)>0:
        print(new_list[0], end="")
        new_list=new_list[1:len(new_list)]
        return print1(new_list)
    
    
def main():
    list1=input("Enter a message:\n")
    new_list=[]
    print("Encrypted message:")
    print1(convert_letter(list1, new_list))
main()