a = int(input("enter a value: ")) #20
b = int(input("enter b value: ")) #25
while(a>0 and b>0):
    if (a > b):
        a = a - b
    else:
        b = b - a
if a == 0:
    print(b)
else:
    print(a)