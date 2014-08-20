plus_sign="+"
minus_sign="-"
stroke="|"
word=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
frame_thickness=eval(input("Enter the frame thickness:\n"))

#print(stroke*i,plus_sign,minus_sign
for i in range(frame_thickness):
    print(stroke*i+plus_sign+minus_sign*(len(word)+2*(frame_thickness-i))+plus_sign+stroke*i)

for i in range(repeat):
    print(stroke*frame_thickness,word,stroke*frame_thickness)
for i in range(frame_thickness-1,-1,-1):
    print(stroke*i+plus_sign+minus_sign*(len(word)+2*(frame_thickness-i))+plus_sign+stroke*i)