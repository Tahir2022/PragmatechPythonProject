# Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a < b < c < d:
    print(d)
elif a < b < d < c:
    print(c)
elif a < c < d < b:
    print(b)
else:
    print(a)