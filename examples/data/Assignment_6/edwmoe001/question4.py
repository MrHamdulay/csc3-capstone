"""Program to take list and output histogram
2014-04-24
Tauhirah Eguardo"""


def main():
    marks = input("Enter a space-separated list of marks:\n")
    mark_list = marks.split(" ")
    fail,third,lsecond,usecond,first = counter(mark_list)
    print("1 |","X"*first,sep="")
    print("2+|","X"*usecond,sep="")
    print("2-|","X"*lsecond,sep="")
    print("3 |","X"*third,sep="")
    print("F |","X"*fail,sep="")
    
    
def counter(array):
    #fn to count amount of each category
    fail,third,lsecond,usecond,first = 0,0,0,0,0
    for i in range(0,len(array)):
        if int(array[i]) >= 75:
            first += 1  
        elif int(array[i]) >=70:
            usecond += 1
        elif int(array[i]) >=60:
            lsecond += 1
        elif int(array[i]) >=50:
            third +=1
        elif 0 <= eval(array[i]):
            fail +=1
      
    return fail,third,lsecond,usecond,first


main()