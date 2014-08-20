markslist = input("Enter a space-separated list of marks:\n")
marks = markslist.split(" ")

first = 0
upsecond=0
lowsecond=0
third=0
fail=0

for mark in marks:
    mark = eval(mark)
    if mark >= 75:
        first += 1
    elif 70 <=  mark < 75:
        upsecond +=1
    elif 60 <=  mark < 70:
        lowsecond +=1 
    elif 50 <=  mark < 60:
        third +=1    
    elif mark < 50:
        fail +=1   
        
print("1 |","X"*first, sep = "")
print("2+|","X"*upsecond, sep = "")
print("2-|","X"*lowsecond, sep = "")
print("3 |","X"*third, sep = "")
print("F |","X"*fail, sep = "")
                
     