"""program to check if SUDUKO is valid
Author: Divan Jagers
date: 13 May 2014"""
#The basic algorithm of this program is simple.It is known than that when each number is only repeated once in a suduko row,grid or column then the total of that row,grid or column should = 45


def check_rows():
     counter=0       # a counter that keeps track of the total of the rows sp far
     for item in rows:    #an iteration that goes through each itam in the rows list
          for j in range(9):
               counter+=eval(item[j])   #it then adds the numeric value of that item to the counter
                                 
     if counter==405:   #since the list consists of 9 lines the total should thus be 45x9(=405) for it to be suduko , else it is false
          return True
     else:
          return False
def check_columns():   # the same basic algorithm is follwed for checkin the columns
     counter=0
     for item in columns:
          counter+=eval(item)
     if counter == 405:
          return True
     else:
          return False
def check_grid1():   #checks each grid item and if the grid is equal to 45
     counter=0
     for item in grid1:
          for i in range(3):
               counter+=eval(item[i])
     if counter == 45:
          return True
     else:
          return False
def check_grid2():   #the same applies for all the other function as they are mirror copies of the check_grid1 function
     counter=0
     for item in grid2:
          for i in range(3):
               counter+=eval(item[i])
     if counter == 45:
          return True
     else:
          return False
def check_grid3():
     counter=0
     for item in grid3:
          for i in range(3):
               counter+=eval(item[i])
     if counter == 45:
          return True
     else:
          return False
def check_grid4():
     counter=0
     for item in grid4:
          for i in range(3):
               counter+=eval(item[i])
     if counter == 45:
          return True
     else:
          return False
def check_grid5():
     counter=0
     for item in grid5:
          for i in range(3):
               counter+=eval(item[i])
     if counter == 45:
          return True
     else:
          return False
def check_grid6():
     counter=0
     for item in grid6:
          for i in range(3):
               counter+=eval(item[i])
     if counter == 45:
          return True
     else:
          return False
def check_grid7():
     counter=0
     for item in grid7:
          for i in range(3):
               counter+=eval(item[i])
     if counter == 45:
          return True
     else:
          return False
def check_grid8():
     counter=0
     for item in grid8:
          for i in range(3):
               counter+=eval(item[i])
     if counter == 45:
          return True
     else:
          return False
def check_grid9():
     counter=0
     for item in grid9:
          for i in range(3):
               counter+=eval(item[i])
     if counter == 45:
          return True
     else:
          return False

if __name__=="__main__":
     rows=[]   #empty lists that are to be filled
     columns=[]
     grid1=[] 
     grid2=[]
     grid3=[]
     grid4=[]
     grid5=[]
     grid6=[]
     grid7=[]
     grid8=[]
     grid9=[]
     for i in range(9):
          values=input("") #promppts the user to enter valus
          rows.append(values)   #these are then created into a list of rows
     for i in range(9):   #iteration that fills up the column list
          
          for j in range(9):
               columns.append(rows[j][i])      
     for i in range(3):
          grid1.append(rows[i][:3])   #these iterations fill up the cgrid lists above
     for i in range(3):
          grid2.append(rows[i][3:6])
     for i in range(3):
          grid3.append(rows[i][6:9])
     for i in range(3,6):
          grid4.append(rows[i][:3])
     for i in range(3,6):
          grid5.append(rows[i][3:6])
     for i in range(3,6):
          grid6.append(rows[i][6:9])
     for i in range(6,9):
          grid7.append(rows[i][:3])
     for i in range(6,9):
          grid8.append(rows[i][3:6])
     for i in range(6,9):
          grid9.append(rows[i][6:9])
     check_rows()
     check_columns()
     check_grid1()
     check_grid2()
     check_grid3()
     check_grid4()
     check_grid5()
     check_grid6()
     check_grid7()
     check_grid8()
     check_grid9()
     if check_rows() and check_columns() and check_grid1() and check_grid2() and check_grid3() and check_grid4() and check_grid5() and check_grid6() and check_grid7() and check_grid8() and check_grid9()==True:
          print("Sudoku grid is valid")   #if all the checks are true then the grid is indeed valid
     else:
          print("Sudoku grid is not valid")   #if any one is not true then the grid is not valid