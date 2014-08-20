def tri(n,ch):
    for i in range(n+1):
        print(" "*((n-i))+ch*(2*i-1))
        
size=eval(input("Enter the height of the triangle:"))
content="*"

tri(size,content)