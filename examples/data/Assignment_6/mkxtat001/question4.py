#Tato Moaki MKXTAT001
#Program to print a histogram
#4/21/2014
def main():
    marks_array = input("Enter a space-separated list of marks:\n")
    
    #new instance of list with elements converted to int data type
    marks_array = [int(i) for i in marks_array.split()]
    
    #set the accumulators to zero
    count1 = 0 
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    
    #count marks obtained within given range
    for mark in marks_array:
        if(mark >= 75):
            count1 += 1
        elif(mark >= 70):
            count2 += 1
        elif(mark >= 60):
            count3 += 1
        elif(mark >= 50):
            count4 += 1
        else:
            count5 += 1
    #output the histogram 
    print("1 |","X"*count1,sep="")
    print("2+|","X"*count2,sep="")
    print("2-|","X"*count3,sep="")
    print("3 |","X"*count4,sep="")
    print("F |","X"*count5,sep="")        

if __name__=="__main__":
    main()
    