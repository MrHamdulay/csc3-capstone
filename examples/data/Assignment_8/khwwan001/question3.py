'''program to encrypt a message entered by user
Wandile Khowa
09-05-2014
'''
def recursive(a, b):
     if b == 0:
          global empty_list
          empty_list = []
     
     if b <= x:
          if a[b] == a[b].lower():
               if (ord(a[b]) != 32) and (ord(a[b]) != ord("z")) and (ord(a[b]) != ord(".")):
                    a[b] = chr(ord(a[b])+1)
                    empty_list.append(a[b])
                    recursive(a, b+1)
               elif (ord(a[b]) == 32):
                    empty_list.append(a[b])
                    recursive(a, b+1)
               elif (ord(a[b]) == ord("z")):
                    a[b] = chr(ord("a"))
                    empty_list.append(a[b])
                    recursive(a, b+1)
               elif (ord(a[b]) == ord(".")):
                    empty_list.append(a[b])
                    recursive(a, b+1)
          elif a[b] != a[b].lower():
               empty_list.append(a[b])
               recursive(a, b+1)

     if b == x+1:
          q = "".join(empty_list)
          print("Encrypted message: ")
          print(q)
     
def main():
     s = input("Enter a message: \n")
     s_list = list(s)
     global x
     x = len(s_list)-1
     recursive(s_list, 0)
     
if __name__=='__main__':
     main()
     