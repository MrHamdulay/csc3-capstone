"""Sithembiso Mashinini 
2014/04/25
prints names onto the reight side"""


def main():
          #name list is an empty list 
          name_list=[] 
          user_input=input('Enter strings (end with DONE):\n')#prompts the user for inputs
          while user_input!='DONE':
                    
                   
                    name_list.append(user_input)#this appends the users input to the empty list 
                    user_input=input()#this keeps prompting the user until done 
                    
          #for item in name_list:
                   # print(item)
          print()
          
          print ('Right-aligned list:')
          numbers=[]
          for i in range(len(name_list)):
                    numbers.append(len(name_list[i]))#finds the maximum length in the list after it create a space using the maximum length
                    #each space change according to the word
          for ch in name_list:
          
                    print((max(numbers)-len(ch))*' '+ch)
                    
main()                   
          
              