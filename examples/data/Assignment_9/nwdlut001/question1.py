
filename=input("Enter the marks filename:\n") 
nfile=open(filename,"r")
list_n=nfile.readlines()
#getting the student's names and marks
if len(list_n)==3:
   student0=list_n[0]
   student1=list_n[1]
   student2=list_n[2]
   #getting the marks
   mark0=eval(student0[-3]+student0[-2])
   mark1=eval(student1[-3]+student1[-2])
   mark2=eval(student2[-3]+student2[-2])
   #calculating the average
   average=(mark0+mark1+mark2)/len(list_n)
   raverage=round(average,2)
   if average%len(list_n)==0:
      print(float(average))
   else:
      print("The average is:",raverage)

   #calculating the sd
   import math
   sd=math.sqrt(((mark0-raverage)**2+(mark1-raverage)**2+(mark2-raverage)**2)/len(list_n))

   rsd=round(sd,2)
   j=math.sqrt(((mark0-raverage)**2+(mark1-raverage)**2+(mark2-raverage)**2))
   if j%len(list_n)==0:
      print(float(sd))
   else:
      print("The std deviation is:",rsd)

   #student that need to go to the counsellor
   print("List of students who need to see an advisor:")
   if mark0<(raverage-sd):
      if len(student0)==7:
            print(student0[0:4])
      elif len(student0)==8:
          print(student0[0:4])
      elif len(student0)==9:
          print(student0[0:5])    
      elif len(student0)==10:
          print(student0[0:6])
      elif len(student0)==11:
        print(student0[0:7])
      elif len(student0)==12:
        print(student0[0:8])    
      elif len(student0)==13:
        print(student0[0:9])
      elif len(student0)==14:
        print(student0[0:10])
      elif len(student0)==15:
          print(student0[0:10])
      elif len(student0)==16:
        print(student0[0:10])   
   if mark1<(raverage-sd):
        if len(student1)==7:
            print(student1[0:4])
        elif len(student1)==8:
           print(student1[0:4])
        elif len(student1)==9:
            print(student1[0:5])    
        elif len(student1)==10:
            print(student1[0:6])
        elif len(student1)==11:
            print(student1[0:7])
        elif len(student1)==12:
            print(student1[0:8])    
        elif len(student1)==13:
            print(student1[0:9])
        elif len(student1)==14:
            print(student1[0:10])
        elif len(student1)==15:
            print(student1[0:10])
        elif len(student1)==16:
            print(student1[0:10])    
   if mark2<(raverage-sd):
       if len(student2)==7:
          print(student2[0:4])
       elif len(student2)==8:
          print(student2[0:4])
       elif len(student2)==9:
          print(student2[0:5])    
       elif len(student2)==10:
          print(student2[0:6])
       elif len(student2)==11:
          print(student2[0:7])
       elif len(student2)==12:
          print(student2[0:8])    
       elif len(student2)==13:
          print(student2[0:9])
       elif len(student2)==14:
         print(student2[0:10])
       elif len(student2)==15:
         print(student2[0:10])
       elif len(student2)==16:
         print(student2[0:10])        
elif len(list_n)==9:
   student0=list_n[0]
   student1=list_n[1]
   student2=list_n[2]
   student3=list_n[3]
   student4=list_n[4]
   student5=list_n[5]
   student6=list_n[6]
   student7=list_n[7]
   student8=list_n[8]
   #getting the marks
   mark0=eval(student0[-3]+student0[-2])
   mark1=eval(student1[-3]+student1[-2])
   mark2=eval(student2[-3]+student2[-2])
   mark3=eval(student3[-3]+student3[-2])
   mark4=eval(student4[-3]+student4[-2])
   mark5=eval(student5[-3]+student5[-2])
   mark6=eval(student6[-3]+student6[-2])
   mark7=eval(student7[-3]+student7[-2])
   mark8=eval(student8[-3]+student8[-2])   
   #calculating the average
   average=(mark0+mark1+mark2+mark3+mark4+mark5+mark6+mark7+mark8)/len(list_n)
   raverage=round(average,2)
   if average%len(list_n)==0:
      print(float(average))
   else:
      print("The average is:",raverage)
   
   #calculating the sd
   import math
   sd=math.sqrt(((mark0-raverage)**2+(mark1-raverage)**2+(mark2-raverage)**2+(mark3-raverage)**2+(mark1-raverage)**2+(mark4-raverage)**2+(mark5-raverage)**2+(mark6-raverage)**2+(mark7-raverage)**2+(mark8-raverage)**2)/len(list_n))
   
   
   j=math.sqrt((mark0-raverage)**2+(mark1-raverage)**2+(mark2-raverage)**2+(mark3-raverage)**2+(mark1-raverage)**2+(mark4-raverage)**2+(mark5-raverage)**2+(mark6-raverage)**2+(mark7-raverage)**2+(mark8-raverage)**2)
   if j%9==0:
       print(float(sd))
   else:
      print("The std deviation is:",rsd)
   
   #student that need to go to the counsellor
   print("List of students who need to see an advisor:")
   if mark0<(raverage-sd):
       if len(student0)==7:
            print(student0[0:4])
       elif len(student0)==8:
         print(student0[0:4])
       elif len(student0)==9:
             print(student0[0:5])    
       elif len(student0)==10:
             print(student0[0:6])
       elif len(student0)==11:
            print(student0[0:7])
       elif len(student0)==12:
           print(student0[0:8])    
       elif len(student0)==13:
           print(student0[0:9])
       elif len(student0)==14:
           print(student0[0:10])
       elif len(student0)==15:
             print(student0[0:10])
       elif len(student0)==16:
           print(student0[0:10])   
   if mark1<(raverage-sd):
         if len(student1)==7:
               print(student1[0:4])
         elif len(student1)==8:
              print(student1[0:4])
         elif len(student1)==9:
               print(student1[0:5])    
         elif len(student1)==10:
               print(student1[0:6])
         elif len(student1)==11:
               print(student1[0:7])
         elif len(student1)==12:
               print(student1[0:8])    
         elif len(student1)==13:
               print(student1[0:9])
         elif len(student1)==14:
               print(student1[0:10])
         elif len(student1)==15:
               print(student1[0:10])
         elif len(student1)==16:
               print(student1[0:10])    
   if mark2<(raverage-sd):
         if len(student2)==7:
             print(student2[0:4])
         elif len(student2)==8:
             print(student2[0:4])
         elif len(student2)==9:
             print(student2[0:5])    
         elif len(student2)==10:
             print(student2[0:6])
         elif len(student2)==11:
             print(student2[0:7])
         elif len(student2)==12:
             print(student2[0:8])    
         elif len(student2)==13:
             print(student2[0:9])
         elif len(student2)==14:
            print(student2[0:10])
         elif len(student2)==15:
            print(student2[0:10])
         elif len(student2)==16:
            print(student2[0:10])   
   if mark3<(raverage-sd):
       if len(student3)==7:
                     print(student3[0:4])
       elif len(student3)==8:
                  print(student3[0:4])
       elif len(student3)==9:
                      print(student3[0:5])    
       elif len(student3)==10:
                      print(student3[0:6])
       elif len(student3)==11:
                     print(student3[0:7])
       elif len(student3)==12:
                    print(student3[0:8])    
       elif len(student3)==13:
                    print(student3[0:9])
       elif len(student3)==14:
                    print(student0[0:10])
       elif len(student3)==15:
                      print(student3[0:10])
       elif len(student3)==16:
                    print(student3[0:10])   
   if mark4<(raverage-sd):
      if len(student4)==7:
                        print(student4[0:4])
      elif len(student4)==8:
                       print(student4[0:4])
      elif len(student4)==9:
                        print(student4[0:5])    
      elif len(student4)==10:
                        print(student4[0:6])
      elif len(student4)==11:
                        print(student4[0:7])
      elif len(student4)==12:
                        print(student4[0:8])    
      elif len(student4)==13:
                        print(student4[0:9])
      elif len(student4)==14:
                        print(student4[0:10])
      elif len(student4)==15:
                        print(student4[0:10])
      elif len(student4)==16:
                        print(student4[0:10])    
   if mark5<(raverage-sd):
         if len(student5)==7:
                      print(student5[0:4])
         elif len(student5)==8:
                      print(student5[0:4])
         elif len(student5)==9:
                      print(student5[0:5])    
         elif len(student5)==10:
                      print(student2[0:6])
         elif len(student5)==11:
                      print(student5[0:7])
         elif len(student5)==12:
                      print(student5[0:8])    
         elif len(student5)==13:
                      print(student5[0:9])
         elif len(student5)==14:
                     print(student5[0:10])
         elif len(student5)==15:
                     print(student5[0:10])
         elif len(student5)==16:
                     print(student5[0:10])   
   if mark6<(raverage-sd):
         if len(student6)==7:
                      print(student6[0:4])
         elif len(student6)==8:
                      print(student6[0:4])
         elif len(student6)==9:
                      print(student6[0:5])    
         elif len(student6)==10:
                      print(student6[0:6])
         elif len(student6)==11:
                      print(student6[0:7])
         elif len(student6)==12:
                      print(student6[0:8])    
         elif len(student6)==13:
                      print(student6[0:9])
         elif len(student6)==14:
                     print(student6[0:10])
         elif len(student6)==15:
                     print(student6[0:10])
         elif len(student6)==16:
                     print(student6[0:10])
   if mark7<(raverage-sd):
         if len(student7)==7:
                     print(student6[0:4])
         elif len(student7)==8:
                                           print(student7[0:4])
         elif len(student7)==9:
                                           print(student7[0:5])    
         elif len(student7)==10:
                                           print(student7[0:6])
         elif len(student7)==11:
                                           print(student7[0:7])
         elif len(student7)==12:
                                           print(student7[0:8])    
         elif len(student7)==13:
                                           print(student7[0:9])
         elif len(student7)==14:
                                          print(student7[0:10])
         elif len(student7)==15:
                                          print(student7[0:10])
         elif len(student7)==16:
                                          print(student7[0:10])   
   if mark8<(raverage-sd):
         if len(student8)==7:
                     print(student6[0:4])
         elif len(student8)==8:
                                           print(student8[0:4])
         elif len(student8)==9:
                                           print(student8[0:5])    
         elif len(student8)==10:
                                           print(student8[0:6])
         elif len(student8)==11:
                                           print(student8[0:7])
         elif len(student8)==12:
                                           print(student8[0:8])    
         elif len(student8)==13:
                                           print(student8[0:9])
         elif len(student8)==14:
                                          print(student8[0:10])
         elif len(student8)==15:
                                          print(student8[0:10])
         elif len(student8)==16:
                                          print(student8[0:10])   
    