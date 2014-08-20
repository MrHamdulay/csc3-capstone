#naadirah ismail
#25/4/2014
#histogram provided with a list of marks
def histogram():
   list_marks=input('Enter a space-separated list of marks:\n')
   marks=list_marks.split()
   
   list1=[]
   list2=[]
   list3=[]
   list4=[]
   list5=[]
   for mark in marks:
      mark=eval(mark)
      #append each mark to a list
      if mark<50:
         list1.append(mark)
      elif 50<=mark<60:
         list2.append(mark)
      elif 60<=mark<70:
         list3.append(mark)
      elif 70<=mark<75:
         list4.append(mark)
      elif mark>=75:
         list5.append(mark)
   #print histogram
   print('1 |','X'*len(list5),sep='')
   print('2+|','X'*len(list4),sep='')
   print('2-|','X'*len(list3),sep='')
   print('3 |','X'*len(list2),sep='')
   print('F |','X'*len(list1),sep='')
histogram()
      
      
   

    