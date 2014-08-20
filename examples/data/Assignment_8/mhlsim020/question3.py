"""recursive function program to encrypt a message
simlindile mahlaba
09 May 2014"""

def encrypt_string(list1, str_list):
    if len(list1)>0:
        if list1[0].islower():
            if list1[0]=='z':
                str1='a'
            else:
                str1=chr(ord(list1[0])+1)
        else:
            str1=list1[0]
        str_list.append(str1)
        list1=list1[1:len(list1)]
        return encrypt_string(list1, str_list)
    else:
        return str_list
    
def print1(str_list):
    if len(str_list)>0:
        print(str_list[0], end="")
        str_list=str_list[1:len(str_list)]
        return print1(str_list)
    
    
def main():
    list1=input("Enter a message:\n")
    str_list=[]
    print("Encrypted message:")
    print1(encrypt_string(list1, str_list))
main()