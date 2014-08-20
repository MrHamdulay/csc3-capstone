marks = map (int, input ("Enter a space-separated list of marks:\n").split(" "))
counts = [0] * 5
for mark in marks:
   cat = 4   
   if mark>=75:
      cat = 0
   elif mark>=70:
      cat = 1
   elif mark>=60:
      cat = 2
   elif mark >= 50:
      cat = 3   
   counts[cat] = counts[cat] + 1

labels = ["1 ", "2+", "2-", "3 ", "F "]
for i in range (len (counts)):
   print (labels[i] + "|" + "X" * counts[i])