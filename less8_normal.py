import sys 


print ("Игра КРЕСТИКИ - НОЛИКИ")
print ()
print ("         5X5          ")
print ()
print(" * * * * * * * * *")
print(" * X  X  0  X  0 *")
print(" * X  X  0  0  X *")
print(" * X  0  0  X  0 *")
print(" * 0  X  X  0  X *")
print(" * X  X  0  X  0 *")
print(" * * * * * * * * *")
print ()
ques = str(input("Будете играть в Крестики-Нолики 5Х5?? (Yes/No): "))
print ()
if ques=="No" or ques== "N" or ques== "NO" or ques== "nO" or ques== "n":
    print ("Спасибо за выбор!! До новых встреч!!")
    sys.exit(0)
print ()
print ("Отличный выбор!! Начинаем играть!!")
print ()
ident = int(input("Пожалуйста,выберите сторону,за которую хотите играть:\n1.Крестики (ходят первыми)\n2.Нолики (ходят вторыми)\nВведите 1 или 2: "))



print(" * * * * * * * * *")
print(" * 1  2  3  4  5 *")
print(" * 6  7  8  9  10*")
print(" *11 12 13 14  15*")
print(" *16 17 18 19  20*")
print(" *21 22 23 24  25*")
print(" * * * * * * * * *")

all = []
for el in range (1,26):
    all.append(int(el))

print(all)
print("")
