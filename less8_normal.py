import sys
import random
import curses


print ()
print ()
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
ques = str(input("Будете играть в Крестики-Нолики 5Х5?? (1- Да/2 - Нет): "))
print ()
if ques=="2":
    print ("Спасибо!! До новых встреч!!")
    sys.exit(0)
print ()
print ("Отлично!! Начинаем !!")
print ()
print ()
ident = int(input("Пожалуйста,выберите режим игры:\n1.Человек vs Человек\n2.Человек vs Компьютер\n3.Компьютер vs Компьютер \n\nВведите 1 или 2 или 3: "))
if ident  ==1:
    identname = "Человек vs Человек"
    plrname1 = str(input("Введите имя первого игрока: "))
    print ()
    plrside1 = int(input("Пожалуйста,выберите сторону,за которую будет играть игрок:\n1.Крестики (ходят первыми)\n2.Нолики (ходят вторыми)\n\nВведите 1 или 2: "))
    print ()
    plrname2 = str(input("Введите имя второго игрока: "))
    if plrside1 == 1:
        plrside2=int(2)
        plrchar1 = "X"
        plrchar2 = "O"
    if plrside1 == 2:
        plrside2=int(1)
        plrchar1 = "O"
        plrchar2 = "X"

if ident  ==2:
    identname = "Человек vs Компьютер"
    plrname1 = str(input("Введите имя первого игрока: "))
    print ()
    plrside1 = int(input("Пожалуйста,выберите сторону,за которую будет играть игрок:\n1.Крестики (ходят первыми)\n2.Нолики (ходят вторыми)\n\nВведите 1 или 2: "))
    print ()
    plrname2 = "Альтрон"
    if plrside1 == 1:
        plrside2=int(2)
        plrchar1 = "X"
        plrchar2 = "O"
    if plrside1 == 2:
        plrside2=int(1)
        plrchar1 = "O"
        plrchar2 = "X"

if ident  ==3:
    identname = "Компьютер vs Компьютер"
    plrname1 = "Джарвис"
    plrname2 = "Альтрон"
    if random.randint(0,10)<=5:
        plrside1 = 1
        plrside2 = 2
        plrchar1 = "X"
        plrchar2 = "O"
    else:
        plrside1 = 2
        plrside2 = 1
        plrchar1 = "O"
        plrchar2 = "X"

print ()   
print (f"Режим игры : {identname}\nИмя первого игрока: {plrname1}, играет символом: {plrchar1}\nИмя второго игрока: {plrname2}, играет символом: {plrchar2}\n" )
print ()

ques = str(input("Все верно? Приступаем к ИГРЕ?? (1- Да/2 - Нет): "))
print ()
if ques=="2":
    print ("Спасибо!! До новых встреч!!")
    sys.exit(0)
print ()
print ("Отлично!! Начинаем ИГРАТЬ !!")
print ()
print ()

all = []
for el in range (1,26):
    all.append(int(el))

print(" *  *  *  *  *  * * * *")
print(f" *  {all[0]}   {all[1]}   {all[2]}   {all[3]}   {all[4]}  *")
print(f" *  {all[5]}   {all[6]}   {all[7]}   {all[8]}  {all[9]} *")
print(f" * {all[10]}  {all[11]}  {all[12]}  {all[13]}  {all[14]} *")
print(f" * {all[15]}  {all[16]}  {all[17]}  {all[18]}  {all[19]} *")
print(f" * {all[20]}  {all[21]}  {all[22]}  {all[23]}  {all[24]} *")
print(" *  *  *  *  *  * * * *")


for el1 in range (1,28):
    num = int(input("Игрок "+plrname1+ "введите номер ячейки, куда хотите поставить" + plrchar1))
    all[num-1]=plrchar1
    print(" *  *  *  *  *  * * * *")
    print(f" *  {all[0]}   {all[1]}   {all[2]}   {all[3]}   {all[4]}  *")
    print(f" *  {all[5]}   {all[6]}   {all[7]}   {all[8]}  {all[9]} *")
    print(f" * {all[10]}  {all[11]}  {all[12]}  {all[13]}  {all[14]} *")
    print(f" * {all[15]}  {all[16]}  {all[17]}  {all[18]}  {all[19]} *")
    print(f" * {all[20]}  {all[21]}  {all[22]}  {all[23]}  {all[24]} *")
    print(" *  *  *  *  *  * * * *")




print("Извините, но дальше код не работает.\nЕсли вы хотите продолжения данного проекта,\nто обратитесь к КИВИКошельку Разработчика.\nЗаранее спасибо!!")
print("")
#sys.exit(0)





Viigr1 = [1,2,3,4,5]
Viigr2 = [6,7,8,9,10]
Viigr3 = [11,12,13,14,15]
Viigr4 = [16,17,18,19,20]
Viigr5 = [21,22,23,24,25]
Viigr6 = [1,6,11,16,21]
Viigr7 = [2,7,12,17,22]
Viigr8 = [3,8,13,18,23]
Viigr9 = [4,8,14,19,24]
Viigr10 = [5,10,15,20,25]
Viigr11 = [1,7,13,19,25]
Viigr12 = [5,9,13,17,21]

