#Outeur: Thabiso Beau
#Datum: 25 Maart 2014
#program om vierhoek te ontwerp
def rectangle():
    Rect_Height=eval(input('Enter the height of the rectangle: \n'))
    Rect_Width=eval(input('Enter the width of the rectangle: \n'))

    for i in range(Rect_Height):
        print('*'*Rect_Width)
    
rectangle()     