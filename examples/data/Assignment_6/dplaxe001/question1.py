'''Program to print out names
Axel du Plessis
20-04-2014'''

names = []
namelengths =[0]
print("Enter strings (end with DONE):")
name = input("")

while name not in "doneDoneDONE":
  names.append(str(name))
  namelengths.append(len(name))
  name = input("")

form = "{0:>"+str(max(namelengths))+"}"

print("\nRight-aligned list:")

for name in names:
  print(form.format(name))