a = int(input())
if a < 10:
    print(-1)
else:
    b = 0
    for x in [500, 200, 100, 50, 20, 10]:
        b+=a//x
        a=a-x*(a//x)
    print(b)