'''a program to count the number of repeated characters in a given string
Wandile Khowa
09-05-2014
'''
def recursive(a, b):
     if b == x:
          global count, match
          count = 0
          match = False
     if b != 0 and b != x:
          if a[b] == a[b-1] and not (match == True):
               count+=1
               match = True
               recursive(a, b-1)
          else:
               match = False
               recursive(a, b-1)
     elif b != 0 and b == x:
          if a[b] == a[b-1]:
               count+=1
               match = True
               recursive(a, b-1)
          else: 
               match = False
               recursive(a, b-1)          
     elif b == 0:
          print("Number of pairs:", count)
     
def main():
     s = input("Enter a message: \n")
     s_list = s.split()
     s_new = "".join(s_list)
     global x
     x = len(s_new)-1
     recursive(s_new, x)
     
if __name__=='__main__':
     main()
     
    