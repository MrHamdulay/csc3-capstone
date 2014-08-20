'''Sanele Mdlalose
MDLSAN019
22 April 2014'''

def marks():
    marks=input("Enter a space-separated list of marks:\n") #Get the marks
    marks=marks.split()
    mark_list=[]
    # Check for the ranges of marks  
    if marks!='':
        for i in range(len(marks)):
            if int(marks[i])>=75:
                mark_list.append('1')
                
            elif 70<=int(marks[i])<75:
                mark_list.append('2+')
                
            elif 60<=int(marks[i])<70:
                mark_list.append('2-')
                
            elif 50<=int(marks[i])<60:
                mark_list.append('3')
                
            elif int(marks[i])<50:
                mark_list.append('F')
       
        #Output the histogram    
    print('1'.ljust(2), '|','X'*mark_list.count('1'),sep='')    
    print('2+'.ljust(2), '|','X'*mark_list.count('2+'),sep='')
    print('2-'.ljust(2), '|','X'*mark_list.count('2-'),sep='')
    print('3'.ljust(2), '|','X'*mark_list.count('3'),sep='')
    print('F'.ljust(2), '|','X'*mark_list.count('F'),sep='')
        
marks()              