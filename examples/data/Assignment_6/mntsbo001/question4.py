def main():
    #Creating the list of marks
    mark = input("Enter a space-separated list of marks:\n")
    mark = mark.split()
    mark = [int(i) for i in mark]
    #the levels
    lev1 = 0
    lev2_hi = 0
    lev2_lo = 0
    lev3 = 0
    fail = 0
    #the range of the marks 
    for j in mark:
        if j< 0 or j>100:
            continue
    
        if j >=75 and j<=100:
            lev1+=1
        elif j >=70 and j<75:
            lev2_hi+=1
        elif j>=60 and j<75:
            lev2_lo+=1
        elif j>=50 and j<60:
            lev3+=1
        elif j<50 and j>=0:
            fail+=1
    #printing the histogram form of the marks
    print("1 |"+"X"*lev1)
    print("2+|"+"X"*lev2_hi)
    print("2-|"+"X"*lev2_lo)
    print("3 |"+"X"*lev3)
    print("F |"+"X"*fail)
                     
main()