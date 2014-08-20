def uniquelist():
   Initial = []
   Unique = []
   string = input ("Enter strings (end with DONE):\n")
   Initial.append(string)
   while string != "DONE":
      string = input ('')
      Initial.append(string)
      if string == str("DONE"):
         del Initial[len(Initial)-1]
   for i in Initial:
      if i not in Unique:
         Unique.append(i)   
   print()
   print ("Unique list:")
   if Unique[0] == "DONE":
      print()
   else:
      for i in Unique:
         print (i)
uniquelist()