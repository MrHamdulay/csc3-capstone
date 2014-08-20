

"""sithembiso Mashinini 
2014 may 28
removing duplicate"""

def main():
    
    seen=[]#everything that is repeated is stored in seen
    unique_list=[]#this is a list that has no duplicates
    user_input=input('Enter strings (end with DONE):\n')
    while user_input!='DONE':#sentinal
        if user_input not in seen:
            unique_list.append(user_input)#if not a duplicate word it saved at uniques list but if duplicate is saved at seen
        seen.append(user_input)
        user_input=input()
    print('')
    print('Unique list:')
    
    for i in unique_list:
        print(i)
main()