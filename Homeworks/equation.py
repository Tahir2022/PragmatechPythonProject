# Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.

import math
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == b == c == d:
    print(math.pow(a, 2))
else:
    print(a + b + c +d)