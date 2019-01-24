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

    def __init__(self, fname, name, sname, role):
        self.fname = fname
        self.name=name
        self.sname = sname
        self.role = role

    def get_fulln(self):
        return self.fname + ' '+ self.name+ ' ' + self.sname

    def get_fio(self):
        return self.fname + ' '+ self.name[0]+ '.' + self.sname[0]+ '.'

class Student(Human):
    def __init__(self, fname, name, sname, role, pear1, pear2, klass, subjj):
        super().__init__(self, fname, name, sname, role)
        self.pear1 = pear1
        self.pear2 = pear2
        self.klass = klass
        self.subjj = subjj
    
class Teacher(Human):
    def __init__(self, fname, name, sname, role, subjname):
        super().__init__(self, fname, name, sname, role)
        self.subjname = subjname


h1 = Human("Иванов","Иван","Иванович","учитель")
print (h1.get_fulln())
print (h1.get_fio())

