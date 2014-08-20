#GLMSUM001
#Sumayah Goolam Rassool
#30 April 2014



strings = input("Enter strings (end with DONE): \n") #-----allows user to input a string 

data = [] #------------------------------------------------empty list created to store values

#------------------------------------------------------reloops untils "DONE" is entered
while strings != "DONE":
       
       if strings not in data: 
              
              data.append(strings)#--------------------adds string to list as long as "DONE" is not entered 
              
       strings = input("")  #--------------------------allows for continuous inout by user                           

print()
#----------------------------------------------displays heading an list of unique names
print("Unique list:") 

for i in data:   
       
       print(i)