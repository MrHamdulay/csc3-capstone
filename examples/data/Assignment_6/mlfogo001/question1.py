array=[]
print("Enter strings (end with DONE):\n")
strings="" 
#loop used to populate list with strings
while strings!="DONE":
  strings= input("")
  array.append(strings)
while strings=="DONE":
    break
y= len(array)
array= array[:y-1]

if y!=1 and array[0]!="DONE":
  duplicate_array= array*1
  duplicate_array.sort(key=len)
  longest_string= duplicate_array[-1]
  length_longest= len(longest_string)
print("Right-aligned list:")


for i in (array):
  spaces= ((length_longest)-len(i))*" "
  print(spaces+i)
