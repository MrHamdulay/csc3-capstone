mes = input("Enter the message:\n")
count = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))

length = (2*thick) + len(mes) + 2
for i in range(thick):
    print(i*'|', '+', (length - (2*(1+i))) * '-', '+', i*'|',sep = '')
for j in range(count):
    print("|"* thick, mes, "|"*thick)
for k in  range(thick,0,-1):
    print((k-1)*'|', '+', (length - (2*(k))) * '-', '+', (k-1)*'|',sep = '')
