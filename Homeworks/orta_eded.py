# Üç müxtəlif a, b, c ədələri verilmişdir. Onlardan qiymətcə orta olanı tapın.
# a, b, c = [0, 1000]

a, b, c = int(input()), int(input()), int(input())
if a < b < c:
    print(b)
if b < a < c:
    print(a)
if a < c < b:
    print(c)