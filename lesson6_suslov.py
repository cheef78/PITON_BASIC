# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class Human:

    def __init__(self, fname, name, sname):
        self.fname = fname
        self.name=name
        self.sname = sname
        

    def get_fulln(self):
        return self.fname + ' '+ self.name+ ' ' + self.sname

    def get_fio(self):
        return self.fname + ' '+ self.name[0]+ '.' + self.sname[0]+ '.'

class Student:
    def __init__(self, fname, name, sname, pear1, pear2, klass, subjj):
        self.fname = fname
        self.name=name
        self.sname = sname
        self.pear1 = pear1
        self.pear2 = pear2
        self.klass = klass
        self.subjj = subjj

    def get_fulln(self):
        return self.fname + ' '+ self.name+ ' ' + self.sname

    def get_fio(self):
        return self.fname + ' '+ self.name[0]+ '.' + self.sname[0]+ '.'

    def get_klass(self):
        return self.klass

    def get_subjj(self):
        return self.subjj

class Teacher:
    def __init__(self, fname, name, sname, subjname):
        self.fname = fname
        self.name=name
        self.sname = sname
        self.subjname = subjname

    def get_fulln(self):
        return self.fname + ' '+ self.name+ ' ' + self.sname

    def get_fio(self):
        return self.fname + ' '+ self.name[0]+ '.' + self.sname[0]+ '.'

    def get_subjname(self):
        return self.subjname


h1 = Human("Иванов","Иван","Иванович",)
print (h1.get_fulln())
print (h1.get_fio())

Pearnts = [Human("Иванов","Сергей","Иванович"),
        Human("Иванова","Анна","Петровна"),
        Human("Сидоров","Сергей","Иванович"),
        Human("Сидорова","Анна","Петровна"),  
        Human("Петров","Сергей","Иванович"),
        Human("Петрова","Анна","Петровна"),
        Human("Соколов","Сергей","Иванович"),
        Human("Соколова","Анна","Петровна"),
        Human("Чижов","Сергей","Иванович"),
        Human("Чижова","Анна","Петровна"),
        Human("Зайцев","Сергей","Иванович"),
        Human("Зайцева","Анна","Петровна"),
        Human("Кошкин","Сергей","Иванович"),
        Human("Кошкина","Анна","Петровна")]

students = [Student("Иванов","Петр","Сергеевич",Pearnts[0],Pearnts[1],"1Б",['математика', 'русский', 'литература']),
         Student("Сидорова","Анна","Сергеевна",Pearnts[2],Pearnts[3],"3В",['математика', 'русский', 'литература', 'Физкультура']),
         Student("Петров","Петр","Сергеевич",Pearnts[4],Pearnts[5],"5Е",['математика', 'русский', 'литература','геометрия']),
         Student("Соколова","Светлана","Сергеевна",Pearnts[6],Pearnts[7],"5Е",['математика', 'русский', 'литература', 'геометрия']),
         Student("Чижов","Петр","Сергеевич",Pearnts[8],Pearnts[9],"9А",['математика', 'русский', 'литература', 'ин.яз', 'физика']),
         Student("Зайцева","Ирина","Сергеевна",Pearnts[10],Pearnts[11],"10Д",['математика', 'русский', 'литература', 'ин.яз', 'физика', 'химия']),
         Student("Кошкин","Петр","Сергеевич",Pearnts[12],Pearnts[13],"11Ж",['математика', 'русский', 'литература', 'ин.яз', 'физика','химия','биология'])]

Teachers = [Teacher("Уваров","Петр","Иванович",'математика'),
        Teacher("Санина","Алена","Игоревна",'русский'),
        Teacher("Сатанеев","Михаил","Иванович", 'литература'),
        Teacher("Шемаханская","Валентина","Петровна", 'ин.яз'),  
        Teacher("Брыль","Семен","Иванович", 'физика'),
        Teacher("Марзина","Елена","Петровна", 'химия'),
        Teacher("Ковров","Юрий","Станилавович", 'биология'),
        Teacher("Камнеедов","Геннадий","Борисович", 'геометрия')]

list=[]

for el in range(0, len(students)):
    list.append((students[int(el)].get_klass()))
print("Полный перечень классов, в которых обучаются школьники:\n ", list)
print ()


klas=[]    
list=[]
klas = input ("Введите номер и литеру класса без пробелов, например 1А: ")

for el in range(0, len(students)):
    if students[int(el)].get_klass()==klas:
        list.append((students[int(el)].get_fio()))
if list == []:
    list.append("Учеников в таком классе нет или нет такого класса") 
print("Список школьников, которые обучаются в классе " + str(klas)+ ":\n ", list)
print ()


shkol=[]
info=[]
list=[]
for el in range(0, len(students)):
    list.append((str(el+1)+". " + str(students[int(el)].get_fio())))

print("Список школьников, которые обучаются в школе:\n")
for el in range(0, len(students)):
    print(list[int(el)])
print()

shkol = int(input ("Введите номер ученика для вывода информации по предметам: "))

list1=[]
for el1 in range(0, len(Teachers)):
    if (Teachers[int(el1)].get_subjname() in students[shkol-1].get_subjj())== True:
        list1.append(Teachers[int(el1)].get_fio())
    


print(str(students[shkol-1].get_fio())+"\nКласс: "+ str(students[shkol-1].get_klass())+"\nУчителя: "+ str(list1)+"\nПредметы: "+ str(students[shkol-1].get_subjj()))
              




