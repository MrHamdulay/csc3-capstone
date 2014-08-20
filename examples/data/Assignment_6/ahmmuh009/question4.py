def marks():
    marks=input("Enter a space-separated list of marks:\n")
    list_1=marks.split(" ")
    count_1=""
    count_2_1=""
    count_2_2=""
    count_3=""
    count_F=""
    for item in list_1:
        if int(item)>=75:
            count_1+="X"
        elif int(item)<75 and int(item)>=70:
            count_2_1+="X"
        elif int(item)<70 and int(item)>=60:
            count_2_2+="X"                      
        elif int(item)<60 and int(item)>=50:
            count_3+="X"
        elif int(item)<50 and int(item)>=0:
            count_F+="X"
    print("1 |",count_1,"\n2+|",count_2_1,"\n2-|",count_2_2,"\n3 |",count_3,"\nF |",count_F,sep="")

marks()