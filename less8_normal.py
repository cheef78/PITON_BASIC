import sys
import random
import curses

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
viigrAll =[]
viigrAll.append(Viigr1)
viigrAll.append(Viigr2)
viigrAll.append(Viigr3)
viigrAll.append(Viigr4)
viigrAll.append(Viigr5)
viigrAll.append(Viigr6)
viigrAll.append(Viigr7)
viigrAll.append(Viigr8)
viigrAll.append(Viigr9)
viigrAll.append(Viigr10)
viigrAll.append(Viigr11)
viigrAll.append(Viigr12)
for el in range (0,12):
    print (viigrAll[int(el)])
    
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

all1 = []
for el in range (1,26):
    all1.append(int(el))

print(" *  *  *  *  *  * * * *")
print(f" *  {all1[0]}   {all1[1]}   {all1[2]}   {all1[3]}   {all1[4]}  *")
print(f" *  {all1[5]}   {all1[6]}   {all1[7]}   {all1[8]}  {all1[9]} *")
print(f" * {all1[10]}  {all1[11]}  {all1[12]}  {all1[13]}  {all1[14]} *")
print(f" * {all1[15]}  {all1[16]}  {all1[17]}  {all1[18]}  {all1[19]} *")
print(f" * {all1[20]}  {all1[21]}  {all1[22]}  {all1[23]}  {all1[24]} *")
print(" *  *  *  *  *  * * * *")

plrnumb1=[]
plrnumb2=[]
plrnumbAll=[]
el1=0
while len(plrnumbAll) <= 25:
    num = 0
    el1 = el1+1
    num = int(input("Игрок_"+plrname1+ "_введите номер ячейки, куда хотите поставить_" + plrchar1+": "))
    all1[num-1]=plrchar1
    print(" *  *  *  *  *  * * * *")
    print(f" *  {all1[0]}   {all1[1]}   {all1[2]}   {all1[3]}   {all1[4]}  *")
    print(f" *  {all1[5]}   {all1[6]}   {all1[7]}   {all1[8]}  {all1[9]} *")
    print(f" * {all1[10]}  {all1[11]}  {all1[12]}  {all1[13]}  {all1[14]} *")
    print(f" * {all1[15]}  {all1[16]}  {all1[17]}  {all1[18]}  {all1[19]} *")
    print(f" * {all1[20]}  {all1[21]}  {all1[22]}  {all1[23]}  {all1[24]} *")
    print(" *  *  *  *  *  * * * *")

    plrnumb1.append(int(num))
    plrnumb1=sorted(plrnumb1)
    for el in range (0,12):
        if set(viigrAll[int(el)]).issubset(plrnumb1)==True:# Входит ли list_1 в list_2 ?
            print ("ИГРОК "+ plrname1 + " ПОЗДРАВЛЯЕМ ВАС! ВЫ ВЫИГРАЛИ!!! УРА!!!")
            sys.exit(0)
    print (plrnumb1)
    
    print (el1)
    el1 = el1+2
    num = 0
    num = int(input("Игрок_"+plrname2+ "_введите номер ячейки, куда хотите поставить_" + plrchar2+": "))
    all1[num-1]=plrchar2
    print(" *  *  *  *  *  * * * *")
    print(f" *  {all1[0]}   {all1[1]}   {all1[2]}   {all1[3]}   {all1[4]}  *")
    print(f" *  {all1[5]}   {all1[6]}   {all1[7]}   {all1[8]}  {all1[9]} *")
    print(f" * {all1[10]}  {all1[11]}  {all1[12]}  {all1[13]}  {all1[14]} *")
    print(f" * {all1[15]}  {all1[16]}  {all1[17]}  {all1[18]}  {all1[19]} *")
    print(f" * {all1[20]}  {all1[21]}  {all1[22]}  {all1[23]}  {all1[24]} *")
    print(" *  *  *  *  *  * * * *")

    plrnumb2.append(int(num))
    plrnumb2=sorted(plrnumb2)
    for el in range (0,12):
        if set(viigrAll[int(el)]).issubset(plrnumb2)==True:# Входит ли list_1 в list_2 ?
            print ("ИГРОК "+ plrname1 + " ПОЗДРАВЛЯЕМ ВАС! ВЫ ВЫИГРАЛИ!!! УРА!!!")
            sys.exit(0)
    print (plrnumb2)
    print (el1)
    plrnumbAll= plrnumb1+plrnumb2
    plrnumbAll=sorted(plrnumbAll)
    print (plrnumbAll)
    print (len(plrnumbAll))
print("УВАЖАЕМЫЕ ИГРОКИ! ИЗВИНИТЕ, НО БОЕВАЯ НИЧЬЯ!!!\nПОБЕДИЛА ДРУЖБА!! СПАСИБО ЗА ИГРУ!!")
print("")
sys.exit(0)
    
        
