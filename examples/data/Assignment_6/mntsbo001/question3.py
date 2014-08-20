def main():
   #Entering title
   title="Independent Electoral Commission"
   print(title)
   print("-"*len(title))
   #Entering list
   name = input("Enter the names of parties (terminated by DONE):\n")
   list_of_names = [name]
   #Also making it a dictionary
   dict_of_names = {name:name}
   while name!="DONE":
      name = input("")
      if name != "DONE":
         list_of_names.append(name)
         dict_of_names.update({name:name})
   print(' ')
   #Sorting dictionary
   dict_of_names = sorted(dict_of_names)
   print ("Vote counts:")
   for i in dict_of_names:
      #counting parties
      a = list_of_names.count(i)
      print( "{0:<11}".format(i)+"-",a)
      
            
main()