import math

filename = input ("Enter the marks filename:\n")

f = open (filename, "r")
data = f.readlines ()
f.close ()

total = 0
count = 0
for line in data:
   line = line[:-1]
   fields = line.split (",")
   if len (fields) == 2:
      count += 1
      total += int (fields[1])
mean = total/count
print ("The average is: {:.2f}".format (mean))

stddev = 0
for line in data:
   line = line[:-1]
   fields = line.split (",")
   if len (fields) == 2:
      stddev += (int (fields[1]) - mean)**2
stddev = math.sqrt (stddev / count)      

print ("The std deviation is: {:.2f}".format (stddev))

heading = 0
for line in data:
   line = line[:-1]
   fields = line.split (",")
   if len (fields) == 2:
      if int(fields[1]) < mean-stddev:
         if heading == 0:
            heading = 1
            print ("List of students who need to see an advisor:")
         print (fields[0])
