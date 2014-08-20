#Program that outputs a histogram representation of marks
#Ayesha Marcus
#22/04/2014

def fFail(mark):          #Fail < 50%
  res = 0
  if mark < 50:
    res = 1              
  return res        

def fOne(mark):     
  res = 0
  if mark >= 75:
    res = 1
  return res

#70% <= upper 2nd < 75% 
def fTwoPlus(mark):
  res = 0
  if mark >= 70 and mark < 75:
    res = 1
  return res

#60% <= lower 2nd < 70%
def fTwoMinus(mark):
  res = 0
  if mark >= 60 and mark < 70:
    res = 1
  return res

#50% <= 3rd < 60% 
def fThird(mark):
  res = 0
  if mark >= 50 and mark < 60:
    res = 1
  return res

def main ():

  hist = {}
  #initialize dictionary 
  hist["F"]  = 0
  hist["1"]  = 0
  hist["2+"] = 0
  hist["2-"] = 0
  hist["3"]  = 0
  

  sInput=input(("Enter a space-separated list of marks:\n"))
  #sInput="12 23 34 45 56 67 78 89 90"
  
  aMarks = sInput.split(' ')
  for i in range(len(aMarks)):
    hist["1"] = int(hist["1"]) + fOne(int(aMarks[i]))
    hist["2+"] = int(hist["2+"]) + fTwoPlus(int(aMarks[i]))
    hist["2-"] = int(hist["2-"]) + fTwoMinus(int(aMarks[i]))
    hist["3"] = int(hist["3"]) + fThird(int(aMarks[i]))
    hist["F"] = int(hist["F"]) + fFail(int(aMarks[i]))
    
  print( str("1 |") + str(int(hist["1"])*"X"))
  print(str("2+|") + str(int(hist["2+"])*"X"))
  print(str("2-|") + str(int(hist["2-"])*"X"))
  print(str("3 |") + str(int(hist["3"])*"X"))
  print(str("F |") + str(int(hist["F"])*"X"))
  
if __name__ == "__main__":
   main()
