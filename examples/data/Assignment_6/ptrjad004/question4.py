# A program that outputs a histogram for list of marks
# Wongwa Giqwa
# 23 April 2014

list_of_marks = input('Enter a space-separated list of marks:\n')
marks = list_of_marks.split(' ') # make a list of the marks

# make a counter for each grade category
first_counter = 0
sec_up_counter = 0
sec_low_counter = 0
third_counter = 0
fail_counter =0

# go through list and group the data in list
for mark in marks:
     if int(mark) < 50: # convert data in list to integers
          fail_counter+=1 # add to counter if numbers in category exist
          
     elif 50<=int(mark)<60:
          third_counter+=1
          
     elif 60<=int(mark)<70:
          sec_low_counter+=1
     
     elif 70<=int(mark)<75:
          sec_up_counter+=1
     
     elif int(mark) >= 75:
          first_counter+=1
# create histogram         
print('1 |'+'X'*first_counter)
print('2+|'+'X'*sec_up_counter)
print('2-|'+'X'*sec_low_counter)
print('3 |'+'X'*third_counter)
print('F |'+'X'*fail_counter)

          
           