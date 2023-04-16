a = input("Enter value of a:")
b = input("Enter value of b:")
c = input("Enter value of c:")
d = input("Enter value of d:")

if (a>b):
    great = a
else:
    great = b
if (great>c):
    great = great
else:
    great = c
if(great>d):
    great = great
else:
    great = d

print(great)