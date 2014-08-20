'''
Created on 04 May 2014
Palindrome checking with recursion
@author: Yusuf Khan
KHNYUS005
'''
def reverse(str1ng):
    last = str1ng[-1::]#last char assigned to variable
    str1ng = str1ng[0:-1:1]#last letter of string removed
    if last == '':#if no chars left
        return ''#stop recursion
    else:
        return (last + reverse(str1ng))#recursion

str1ng = input("Enter a string:\n")#input
if reverse(str1ng)==str1ng:#comparing input to recursion output
    print ("Palindrome!")
else:#outputs
    print ("Not a palindrome!")