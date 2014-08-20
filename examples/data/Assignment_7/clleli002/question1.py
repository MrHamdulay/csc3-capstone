"""Enter a list of strings and print list without duplicates
27/04/2014
Elizabeth Cilliers"""

def list():
   
      #create list
      list_of_strings=[]
      
      # get a list of names
      string = input ("Enter strings (end with DONE):\n")
      # as long as user has not typed done
      while string != "DONE":
            
            if string not in list_of_strings:     
                  #store name in list
                  list_of_strings.append (string)
            #get next string
            string = input ("") 
      
      
      print()
      print("Unique list:")
      for string in list_of_strings:
            print(string)
      

      
list()
                  

       
      
      
      
    