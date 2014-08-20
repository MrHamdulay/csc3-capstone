"""Mark analysis
B.Player
11/05/2014"""
import math

def gather_marks(students,names,filename):
   """extract marks and names from txt file and stores as dictionery"""
   try:
      f = open(filename,'r')
      for line in f:
         temp=line.split(",")
         name=temp[0]
         mark=eval(temp[1])      
         students[name]=mark
         names.append(name)
      f.close()
   except IOError as errorNo:
      print("There is an error with the file: ",errorNo)
   
def average(students):
   """calcualtes average of a list marks"""
   tot=0
   for key in students:
      tot+=students[key]   
   average=tot/len(students)
   return average
   
def calc_stdDiv(students,avg):
   """calculate standard diviation of a list of marks"""
   tot=0
   for key in students:
      tot+=(students[key]-avg)**2
   tot=tot/len(students)
   stdD=math.sqrt(tot)   
   return stdD 
   

def main():
   students = {}
   studentNames=[]
   filename=input("Enter the marks filename:\n")
   gather_marks(students,studentNames,filename)
   avg = average(students)
   std = calc_stdDiv(students,avg)
   if avg:
      print("The average is:","{0:.2f}".format(avg))
      print("The std deviation is:","{0:.2f}".format(std))
      if len(students)>2:
         print("List of students who need to see an advisor:")   
         for name in studentNames:
            for key in students:
               if name==key and (students[key]-avg<std*-1):
                  print(name)
   
   
   
main()