a = 3
b = -14
c = -5
d = b**2 - 4 * a * c
x1 = (-b + d**0.5) / 2 * a
x2 = (-b - d**0.5) / 2 * a
x3 = -(b / 2 * a)
if d > 0:
    print(d, x1, x2)
elif d == 0:
    print(x3)
else:
    print()