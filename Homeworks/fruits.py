# Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.

fruits = {
    "apple": 1,
    "orange": 3,
    "watermelon": 2,
    "cherry": 5
}

add = input('Add fruit: ')
if add in fruits:
    print(fruits[add])
else:
    print('Error')