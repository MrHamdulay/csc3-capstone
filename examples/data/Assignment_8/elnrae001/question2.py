'''Find number of pairs in a string
Author:Raees Eland
Date:05 May 2014'''

def no_of_pairs(string):
     if len(string)==1: #stops if there is only one word left
          return 0
     elif string[0]==string[1] and len(string)==2: # if the last two words are a pair
          return 1 + no_of_pairs(string[1:])
     elif string[0]==string[1]: 
          return 1 + no_of_pairs(string[2:]) # moves two strings ahead if there is a pair    
     else:
          return no_of_pairs(string[1:])
     
if __name__ == '__main__':
     string=input('Enter a message:\n')
     print('Number of pairs:',no_of_pairs(string))