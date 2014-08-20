def main():
   names= []
   x=input('Enter strings (end with DONE):\n')
   while x != 'DONE' : 
      names.append(x)
      x=input("")
   print("")
   print("Right-aligned list:")
   for name in names:
      longest=max(names,key=len)
      name=name.rjust(len(longest))
      print(name)
   
main()