import sys
import random
import curses
import time


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

def pole (massiv):

    print()
    print("  ------------------------- ")
    print(f" | {massiv[0]} | {massiv[1]} | {massiv[2]} | {massiv[3]} | {massiv[4]} |")
    print ("  ------------------------- ")    
    print(f" | {massiv[5]} | {massiv[6]} | {massiv[7]} | {massiv[8]} | {massiv[9]} |")
    print ("  ------------------------- ")
    print(f" | {massiv[10]} | {massiv[11]} | {massiv[12]} | {massiv[13]} | {massiv[14]} |")
    print ("  ------------------------- ")
    print(f" | {massiv[15]} | {massiv[16]} | {massiv[17]} | {massiv[18]} | {massiv[19]} |")
    print ("  ------------------------- ")
    print(f" | {massiv[20]} | {massiv[21]} | {massiv[22]} | {massiv[23]} | {massiv[24]} |")
    print("  ------------------------- ")
    print ()

all1 = [' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

    
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
    plrside1 = int(input("Пожалуйста,выберите сторону,за которую будет играть игрок:\n1.Крестики\n2.Нолики\n\nВведите 1 или 2: "))
    print ()
    plrname2 = str(input("Введите имя второго игрока: "))
    if plrside1 == 1:
        plrside2=int(2)
        plrchar1 = " X"
        plrchar2 = " O"
    if plrside1 == 2:
        plrside2=int(1)
        plrchar1 = " O"
        plrchar2 = " X"

if ident  ==2:
    identname = "Человек vs Компьютер"
    plrname1 = str(input("Введите имя первого игрока - Человека: "))
    print ()
    plrside1 = int(input("Пожалуйста,выберите сторону,за которую будет играть игрок:\n1.Крестики\n2.Нолики\n\nВведите 1 или 2: "))
    print ()
    plrname2 = "Джарвис"
    if plrside1 == 1:
        plrside2=int(2)
        plrchar1 = " X"
        plrchar2 = " O"
    if plrside1 == 2:
        plrside2=int(1)
        plrchar1 = " O"
        plrchar2 = " X"

if ident  ==3:
    identname = "Компьютер vs Компьютер"
    plrname1 = "Джарвис"
    plrname2 = "Альтрон"
    if random.randint(0,10)<=5:
        plrside1 = 1
        plrside2 = 2
        plrchar1 = " X"
        plrchar2 = " O"
    else:
        plrside1 = 2
        plrside2 = 1
        plrchar1 = " O"
        plrchar2 = " X"

print ()   
print (f"Режим игры : {identname}\nИмя первого игрока: {plrname1}, играет символом: {plrchar1}\nИмя второго игрока: {plrname2}, играет символом: {plrchar2}\n" )
print ()

ques = str(input("Все верно? Приступаем к ИГРЕ?? (1- Да/2 - Нет): "))
print ()
if ques=="2":
    print ("Спасибо!! До новых встреч!!")
    sys.exit(0)
print ()
print ("Отлично!! Начинаем ИГРАТЬ !!\n(для выхода из игры вместо номера ячейки ВВЕДИТЕ - Q)")
print ()
print ()


plrnumb1=[]
plrnumb2=[]
plrnumbAll=[]

if ident ==1:
    pole(all1)
    for i in range (1,26):
        num = 0
        num = (input("Игрок_"+plrname1+ "_введите номер ячейки, куда хотите поставить_" + plrchar1+"_: "))

        priznak = False
        while priznak==False:
            if num.isnumeric()==True and plrnumbAll.count(int(num)) == 0 and int(num)<=25 and int(num)>0:
               priznak=True
            else:
                if num == "Q" or num == "q":
                    print("СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
                    sys.exit(0)
                priznak = False
                print ()
                print ("Ошибка ввода номера ячейки:")
                print ("-Было введено не число\n-Эта ячейка уже занята\n-Введенное значение вне допустимого диапазона")
                print ("Повторите ввод")
                print ()
                pole(all1)
            
                num = (input("Игрок_"+plrname1+ "_введите номер ячейки, куда хотите поставить_" + plrchar1+"_: "))

        num = int(num)

        all1[num-1]=plrchar1

        pole(all1)

        plrnumb1.append(int(num))
        plrnumb1=sorted(plrnumb1)
        for el5 in range (0,12):
            if set(viigrAll[int(el5)]).issubset(plrnumb1)==True:# Входит ли list_1 в list_2 ?
                print ("ИГРОК "+ plrname1 + " ПОЗДРАВЛЯЕМ ВАС! ВЫ ВЫИГРАЛИ!!! УРА!!!")
                print("СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
                sys.exit(0)
        plrnumbAll= plrnumb1+plrnumb2
        plrnumbAll=sorted(plrnumbAll)
    
        if (len(plrnumbAll)) == 25:
            print("УВАЖАЕМЫЕ ИГРОКИ! ИЗВИНИТЕ, НО БОЕВАЯ НИЧЬЯ!!!\nПОБЕДИЛА ДРУЖБА!! СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
            sys.exit(0)
    

        num = 0
        num = (input("Игрок_"+plrname2+ "_введите номер ячейки, куда хотите поставить_" + plrchar2+"_: "))
    
        priznak = False
        while priznak==False:
            if num.isnumeric()==True and plrnumbAll.count(int(num)) == 0 and int(num)<=25 and int(num)>0:
               priznak=True
            else:
                if num == "Q" or num == "q":
                    print("СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
                    sys.exit(0)
                priznak = False
                print ()
                print ("Ошибка ввода номера ячейки:")
                print ("-Было введено не число\n-Эта ячейка уже занята\n-Введенное значение вне допустимого диапазона")
                print ("Повторите ввод")
                print ()

                pole(all1)
           
                num = (input("Игрок_"+plrname2+ "_введите номер ячейки, куда хотите поставить_" + plrchar2+"_: "))

        num = int(num)
        all1[num-1]=plrchar2

        pole(all1)

        plrnumb2.append(int(num))
        plrnumb2=sorted(plrnumb2)
        for el4 in range (0,12):
            if set(viigrAll[int(el4)]).issubset(plrnumb2)==True:# Входит ли list_1 в list_2 ?
                print ("ИГРОК "+ plrname2 + " ПОЗДРАВЛЯЕМ ВАС! ВЫ ВЫИГРАЛИ!!! УРА!!!")
                print("СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
                sys.exit(0)

        plrnumbAll= plrnumb1+plrnumb2
        plrnumbAll=sorted(plrnumbAll)
    
        if (len(plrnumbAll)) == 25:
            print("УВАЖАЕМЫЕ ИГРОКИ! ИЗВИНИТЕ, НО БОЕВАЯ НИЧЬЯ!!!\nПОБЕДИЛА ДРУЖБА!! СПАСИБО ЗА ИГРУ!!")
            sys.exit(0)
            
    
if ident ==2:
    pole(all1)
    for i in range (1,26):
        num = 0
        num = (input("Игрок_"+plrname1+ "_введите номер ячейки, куда хотите поставить_" + plrchar1+"_: "))

        priznak = False
        while priznak==False:
            if num.isnumeric()==True and plrnumbAll.count(int(num)) == 0 and int(num)<=25 and int(num)>0:
               priznak=True
            else:
                if num == "Q" or num == "q":
                    print("СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
                    sys.exit(0)
                priznak = False
                print ()
                print ("Ошибка ввода номера ячейки:")
                print ("-Было введено не число\n-Эта ячейка уже занята\n-Введенное значение вне допустимого диапазона")
                print ("Повторите ввод")
                print ()
                pole(all1)
            
                num = (input("Игрок_"+plrname1+ "_введите номер ячейки, куда хотите поставить_" + plrchar1+"_: "))

        num = int(num)

        all1[num-1]=plrchar1

        pole(all1)

        plrnumb1.append(int(num))
        plrnumb1=sorted(plrnumb1)
        for el5 in range (0,12):
            if set(viigrAll[int(el5)]).issubset(plrnumb1)==True:# Входит ли list_1 в list_2 ?
                print ("ИГРОК "+ plrname1 + " ПОЗДРАВЛЯЕМ ВАС! ВЫ ВЫИГРАЛИ!!! УРА!!!")
                print("СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
                sys.exit(0)
        plrnumbAll= plrnumb1+plrnumb2
        plrnumbAll=sorted(plrnumbAll)
    
        if (len(plrnumbAll)) == 25:
            print("УВАЖАЕМЫЕ ИГРОКИ! ИЗВИНИТЕ, НО БОЕВАЯ НИЧЬЯ!!!\nПОБЕДИЛА ДРУЖБА!! СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
            sys.exit(0)
    

        num = 0
        num = random.randint(0, 26)
    
        priznak = False
        while priznak==False:
            if plrnumbAll.count(int(num)) == 0 and int(num)<=25 and int(num)>0:
               priznak=True
            else:
                num = random.randint(0, 26)

        num = int(num)
        all1[num-1]=plrchar2

        print("Компьютерный Игрок_"+plrname2+ "_совершил ход")

        pole(all1)

        plrnumb2.append(int(num))
        plrnumb2=sorted(plrnumb2)
        for el4 in range (0,12):
            if set(viigrAll[int(el4)]).issubset(plrnumb2)==True:# Входит ли list_1 в list_2 ?
                print ("ИГРОК "+ plrname2 + " ПОЗДРАВЛЯЕМ ВАС! ВЫ ВЫИГРАЛИ!!! УРА!!!")
                print("СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
                sys.exit(0)

        plrnumbAll= plrnumb1+plrnumb2
        plrnumbAll=sorted(plrnumbAll)
    
        if (len(plrnumbAll)) == 25:
            print("УВАЖАЕМЫЕ ИГРОКИ! ИЗВИНИТЕ, НО БОЕВАЯ НИЧЬЯ!!!\nПОБЕДИЛА ДРУЖБА!! СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
            sys.exit(0)
        
if ident ==3:
    
    for i in range (1,26):

        num = 0
        num = random.randint(0, 26)
        priznak = False
        while priznak==False:
            if plrnumbAll.count(int(num)) == 0 and int(num)<=25 and int(num)>0:
               priznak=True
            else:
                num = random.randint(0, 26)

        num = int(num)
        all1[num-1]=plrchar1

        print("Компьютерный Игрок_"+plrname1+ "_совершил ход")

        pole(all1)

        time.sleep(2) #задержка в течение  секунд

        plrnumb1.append(int(num))
        plrnumb1=sorted(plrnumb1)

        for el5 in range (0,12):
            if set(viigrAll[int(el5)]).issubset(plrnumb1)==True:# Входит ли list_1 в list_2 ?
                print ("ИГРОК "+ plrname1 + " ПОЗДРАВЛЯЕМ ВАС! ВЫ ВЫИГРАЛИ!!! УРА!!!")
                print("СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
                sys.exit(0)
        plrnumbAll= plrnumb1+plrnumb2
        plrnumbAll=sorted(plrnumbAll)
    
        if (len(plrnumbAll)) == 25:
            print("УВАЖАЕМЫЕ ИГРОКИ! ИЗВИНИТЕ, НО БОЕВАЯ НИЧЬЯ!!!\nПОБЕДИЛА ДРУЖБА!! СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
            sys.exit(0)
    

        num = 0
        num = random.randint(0, 26)
    
        priznak = False
        while priznak==False:
            if plrnumbAll.count(int(num)) == 0 and int(num)<=25 and int(num)>0:
               priznak=True
            else:
                num = random.randint(0, 26)

        num = int(num)
        all1[num-1]=plrchar2

        print("Компьютерный Игрок_"+plrname2+ "_совершил ход")

        pole(all1)
        
        time.sleep(2) #задержка в течение  секунд

        plrnumb2.append(int(num))
        plrnumb2=sorted(plrnumb2)
        for el4 in range (0,12):
            if set(viigrAll[int(el4)]).issubset(plrnumb2)==True:# Входит ли list_1 в list_2 ?
                print ("ИГРОК "+ plrname2 + " ПОЗДРАВЛЯЕМ ВАС! ВЫ ВЫИГРАЛИ!!! УРА!!!")
                print("СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
                sys.exit(0)

        plrnumbAll= plrnumb1+plrnumb2
        plrnumbAll=sorted(plrnumbAll)
    
        if (len(plrnumbAll)) == 25:
            print("УВАЖАЕМЫЕ ИГРОКИ! ИЗВИНИТЕ, НО БОЕВАЯ НИЧЬЯ!!!\nПОБЕДИЛА ДРУЖБА!! СПАСИБО ЗА ИГРУ!!\n ДО НОВЫХ ВСТРЕЧ")
            sys.exit(0)
