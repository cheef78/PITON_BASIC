# Автор ____ Суслов Олег Алекчандрович_______:


'''
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print ()
print ()
print ("Решение первого задания уровня Нормал")
print ()
print ()
n=1
m=2

#VVod nachalnogo i konechnogo nomerov ryada fobonacchi
print ("Внимание!:")
print (" - Нумерация порядковых номеров элементов в ряду Фибоначи начинается со значения = 1")
print (" - Необходимо вводить целые числа.")
print (" - Начальный номер ряда должен быть меньше конечного.")
print ()
n=input ("Введите начальный порядковый номер элемента в ряду Фибоначчи:  ")
print ()
m=input ("Введите конечный порядковый номер элемента в ряду Фибоначчи:   ")
print ()
#Proverka korrektnosti vvoda
priznak = False
while priznak==False:
    if n.isnumeric()==True and m.isnumeric() == True:
        if int(n)>0 and int(m)-int(n)>0:
           priznak=True
        else:
            priznak = False
            print ("Ошибка ввода порядковых номеров ряда:")
            print (" - Нумерация порядковых номеров элементов в ряду Фибоначи начинается со значения = 1")
            print (" - Начальный номер ряда должен быть меньше конечного.")
            print ()
            print ("Повторите ввод")
            print ()
            n=input ("Введите начальный порядковый номер ряда Фибоначчи:  ")
            print ()
            m=input ("Введите конечный порядковый номер ряда Фибоначчи:   ")
            print ()
    else:
        priznak = False
        print ("Ошибка ввода порядковых номеров ряда:")
        print (" - Необходимо вводить целые числа.")
        print ()
        print ("Повторите ввод")
        print ()
        n=input ("Введите начальный порядковый номер ряда Фибоначчи:  ")
        print ()
        m=input ("Введите конечный порядковый номер ряда Фибоначчи:   ")
        print ()

def fibonacci(n, m):
    fib= []
    fib.append(1)
    fib.append(1)
    if int(n)==1 and int(m)==2:
        return print ("Элементы ряда Фибоначчи от номера " + str (n) + " до номера " +  str (m)+ " = " + str(fib))
    else:
        for el in range (int(2),int(m)):
            fib.append((fib[el-2]+fib[el-1]))
        return print ("Элементы ряда Фибоначчи от номера " + str (n) + " до номера " +  str (m)+ " = \n" + str(fib[(int(n)-1):int(m)]))
    
print(fibonacci(n, m))



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print ()
print ()
print ("Решение второго задания уровня Нормал")
print ()
print ()
#Generim origin_list
n = (input ("Введите необходимое количество элементов в случайном списке: "))
print ()
def list_sort (n):
    import random
    origin_list=[]
    origin_list1=[]
    sort_list=[]
    for el in range(0,int(n)):
        origin_list.append(random.randint(-100,100))
        origin_list1.append(int(origin_list[int(el)]))
    for el in range(0,(int(n)-1)):
        for el1 in range ((int(el)+1),int(n)):
            if int(origin_list[int(el)]) >= int(origin_list[int(el1)]):
                max_el = int(origin_list[int(el1)])
                min_el = int(origin_list[int(el)])
                origin_list[int(el)]= max_el
                origin_list[int(el1)] = min_el
    return print ("Итоговый несортированный список, состоящий из " + str(n)+" случайных элементов: \n" + str(origin_list1) + "\nИтоговый сортированный по возрастанию список, состоящий из " + str(n)+" случайных элементов: \n" + str(origin_list))
print (list_sort(n))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print ()
print ()
print ("Решение третьего задания уровня Нормал")
print ()
print ()
origin_list=[]
import random
n = int(input ("Введите количество элементов в последовательности: "))
print ()
var = int(input(" 1.Ввод последовательности с клавиатуры\n 2.Генерация числовой последовательности\n 3.Генерация текстовой последовательности\n Выберите вариант задания последовательности: "))
if var==1:
    for el in range (0,int(n)):
        k = input ("Введите в последовательность элемент №:"+ str(el)+" ")
        origin_list.append(k)
if var==2:
    for el in range (0,int(n)):
        origin_list.append(str(random.randint(-100,100)))
if var==3:
    for el in range (0,int(n)):
        k= random.choice("йцукенгшщзхъфывапролджэячсмитьбю")
        origin_list.append(k)
print ()
print ("Итоговая неотфильтрованная последовательность, состоящая из " + str(n)+" элементов: \n" + str(origin_list))
print ()
key = input ("Введите значение фильтра (тип фильтра - 'РАВНО'): ")
print ()
def My_filter (key, origin_list):
    filter_list=[]
    for el in range (0, int(len(origin_list))):
        if str(origin_list[int(el)])==str(key):
            if origin_list[int(el)].isnumeric()==True:
                filter_list.append(int(origin_list[int(el)]))
            else:
                filter_list.append(str(origin_list[int(el)]))
    if len(filter_list)==0:
        return print ("Элементы, удовлетворяющие условию фильтрации,\nв исходной последовательности ОТСУТСТВУЮТ!!!!")
    else:
        return print ("Итоговая отфильтрованная последовательность: \n" + str(filter_list))
print (My_filter (key, origin_list))

'''
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма

print ()
print ()
print ("Решение четвертого задания уровня Нормал")
print ()
print ()
print ("Даны четыре точки A - B - C - D")
cone_list = ['A','B','C','D']
coord_list = []
for el in (cone_list):
    x = input ("Введите координату Х точки " + el + " :")
    coord_list.append(int(x))
    y = input ("Введите координату Y точки " + el + " :")
    coord_list.append(int(y))
print (coord_list)            
if (int(coord_list[2])-int(coord_list[0]))!=0 and (int(coord_list[6])-int(coord_list[4]))!=0 and (int(coord_list[6])-int(coord_list[0]))!=0 and (int(coord_list[4])-int(coord_list[2]))!=0:
    Kab = (int(coord_list[3])-int(coord_list[1]))/(int(coord_list[2])-int(coord_list[0]))
    Kdc = (int(coord_list[7])-int(coord_list[5]))/(int(coord_list[6])-int(coord_list[4]))
    Kad = (int(coord_list[7])-int(coord_list[1]))/(int(coord_list[6])-int(coord_list[0]))
    Kbc = (int(coord_list[5])-int(coord_list[3]))/(int(coord_list[4])-int(coord_list[2]))
    if Kab==Kdc and Kad==Kbc and Kab!=Kad and Kab!=Kbc and Kdc!=Kad and Kdc!= Kbc:
        print("Данные точки ЯВЛЯЮТСЯ вершинами параллелограмма")
    else:
        print("Данные точки НЕ ЯВЛЯЮТСЯ вершинами параллелограмма")
else:
    print ("Одна из сторон параллельна оси Х. Данная ветвь решения еще не реализована. Обратитесь к разработчику.")

    

