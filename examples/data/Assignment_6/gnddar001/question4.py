listing = input("Enter a space-separated list of marks:\n")
listing = listing.split(" ")

fail = ""
third = ""
lowersecond = ""
uppersecond = ""
first = ""

for i in range(len(listing)):
    
    num = eval(listing[i])
    
    if 0 <= num < 50:
        fail += "X"
        
    elif 50 <= num < 60:
        third += "X"
        
    elif 60 <= num < 70:
        lowersecond += "X"
        
    elif 70 <= num < 75:
        uppersecond += "X"
        
    elif 75 <= num <= 100:
        first += "X"
        
counters = ["1 ", "2+", "2-", "3 ", "F "]

numbers = [first, uppersecond, lowersecond, third, fail]

for j in range(len(counters)):
    print(counters[j] + "|" + numbers[j])

