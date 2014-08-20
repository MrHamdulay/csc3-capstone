'''Program producing histogram of results
Axel du Plessis
20-04-2014'''

data = {"1":0, "2+":0, "2-":0, "3":0, "F":0}

marks = input("Enter a space-separated list of marks:\n").split(" ")

for mark in marks:
        mark = eval(mark)
        if (75 <= mark):
                data["1"] += 1 
        elif (50 > mark):
                data["F"] += 1 
        elif (60 > mark):
                data["3"] += 1 
        elif (70 > mark):
                data["2-"] += 1 
        elif (75 > mark):
                data["2+"] += 1 
                
print("1 |"+"X"*data["1"]+"\n2+|"+"X"*data["2+"]+"\n2-|"+"X"*data["2-"]+"\n3 |"+"X"*data["3"]+"\nF |"+"X"*data["F"])