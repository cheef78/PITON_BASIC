__author__ = 'Суслов Олег Александрович'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

print ("Решение первой задачи уровня Normal")
print ()
import math
start_list = [25, -15, 8, 81, -25, 225, 4, 18, 14, 21]
end_list=[]
count = 0
while count < len(start_list):
    if start_list[count]>0 and (math.sqrt(start_list[count])-(math.sqrt(start_list[count])//1))==0:
        end_list.append(int(math.sqrt(start_list[count])))
    count = count+1
print ("Исходный список = ", start_list)
print()
print ("Итоговый список = ", end_list)

        
        




