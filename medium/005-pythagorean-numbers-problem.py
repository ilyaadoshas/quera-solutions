a = input()
a = int(a)
b = input()
b = int(b)
c = input()
c = int(c)
if c**2 == a**2 + b**2 or a**2 == b**2 + c**2 or b**2 == a**2 + c**2 :
    print("Yes")
else:
    print("No")
