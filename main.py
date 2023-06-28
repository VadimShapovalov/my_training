import csv
<<<<<<< HEAD
<<<<<<< HEAD

with open(r'C:\Users\Vadim\Downloads\prices.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))
    min_g = 99999999
    for row in rows[1:]:
        min_ = int(min(row[1:], key=int))
        ind = row.index(str(min_))
        if min_ < min_g:
            lst = [(rows[0][ind], row[0])]
            min_g = min_
        elif min_ == min_g:
            lst.append((rows[0][ind], row[0]))
    result = sorted(lst, key=lambda x: (x[0], x[1]))

    print(f'{result[0][0]}: {result[0][1]}')
=======
>>>>>>> parent of 365a604 (add task 27.06.23)

with open(r'C:\Users\Vadim\Downloads\titanic.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    male, female = [], []
    for row in rows:
        if float(row['age']) < 18 and row['survived'] == '1':
            if row['sex'] == 'male':
                male.append(row['name'])
            else:
                female.append(row['name'])
print(*male, sep='\n')
print(*female, sep='\n')

<<<<<<< HEAD
# with open(r'C:\Users\Vadim\Downloads\student_counts.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file)
#     def sort_(x: str):
#         dig, word = x.split('-')
#         return (int(dig), word)
#     name_sorted = sorted(rows.fieldnames[1:], key=sort_ )
#     result = []
#     name_sorted.insert(0, 'year')
#     for row in rows:
#         lst = []
#         for i in name_sorted:
#             lst.append(row[i])
#         result.append(lst)
#     result.insert(0, name_sorted)
# with open(r'C:\Users\Vadim\Downloads\sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     for i in result:
#         writer.writerow(i)

# from datetime import datetime

# def condense_csv(filename, id_name):
#     with open(filename, encoding='utf-8') as file:
#         rows = csv.reader(file)
#         my_dict = dict()
#         lst = []
#         for i in rows:
#             lst.append(i)
#     for i in range(len(lst)):
#         if lst[i][0] not in my_dict.keys():
#             my_dict[lst[i][0]] = [(lst[i][1], lst[i][2])]
#         else:
#             my_dict[lst[i][0]].append((lst[i][1], lst[i][2]))
#     print(my_dict)
#     title = [id_name]
#     result = []
#     for key, val in my_dict.items():
#         lst2 = [key]
#         for i in val:
#             if i[0] not in title:
#                 title.append(i[0])
#             lst2.append(i[1])
#         result.append(lst2)
#     result.insert(0, title)
#     print(result)
#     with open(r'C:\Users\Vadim\Downloads\condensed.csv', 'w', encoding='utf-8', newline='') as file:
#         writer = csv.writer(file)
#         for i in result:
#             writer.writerow(i)
#
#
# filename = r'C:\Users\Vadim\Downloads\name_log.csv'
# id_name = 'ID'
# condense_csv(filename, id_name)

# with open(r'C:\Users\Vadim\Downloads\name_log.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file)
#     n_n_l = dict()
#     for row in rows:
#         if row['email'] not in n_n_l.keys():
#             n_n_l[row['email']] = [row['username'], row['dtime']]
#         else:
#             date = datetime.strptime(row['dtime'], '%d/%m/%Y %H:%M')
#             date2 = datetime.strptime(n_n_l[row['email']][1], '%d/%m/%Y %H:%M')
#             if date > date2:
#                 n_n_l[row['email']] = [row['username'], row['dtime']]
#             else:
#                 continue
# new_lst = []
# for key, val in n_n_l.items():
#     new_lst.append([val[0], key, val[1]])
# new_lst.sort(key=lambda x: x[1])
#
# with open(r'C:\Users\Vadim\Downloads\new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['username','email','dtime'])
#     for row in new_lst:
#         writer.writerow(row)


# with open(r'C:\Users\Vadim\Downloads\titanic.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file, delimiter=';')
#     male, female = [], []
#     for row in rows:
#         if float(row['age']) < 18 and row['survived'] == '1':
#             if row['sex'] == 'male':
#                 male.append(row['name'])
#             else:
#                 female.append(row['name'])
# print(*male, sep='\n')
# print(*female, sep='\n')
=======
>>>>>>> parent of 365a604 (add task 27.06.23)
=======

with open(r'C:\Users\Vadim\Downloads\titanic.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    male, female = [], []
    for row in rows:
        if float(row['age']) < 18 and row['survived'] == '1':
            if row['sex'] == 'male':
                male.append(row['name'])
            else:
                female.append(row['name'])
print(*male, sep='\n')
print(*female, sep='\n')

>>>>>>> parent of 365a604 (add task 27.06.23)

# with open(r'C:\Users\Vadim\Downloads\wifi.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file, delimiter=';')
#     my_dict = dict()
#     for row in rows:
#         my_dict[row['district']] = my_dict.get(row['district'], 0) + int(row['number_of_access_points'])
# my_dict = sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))
# for i in my_dict:
#     print(f"{i[0]}: {i[1]}")
#


# with open(r'C:\Users\Vadim\Downloads\data.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file)
#     my_dict = {}
#     for row in rows:
#         _, domain = row['email'].split('@')
#         if domain not in my_dict.keys():
#             my_dict[domain] = 1
#         else:
#             my_dict[domain] += 1
#     my_dict = sorted(my_dict.items(), key=lambda x: (x[1], x[0]))
# with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['domain', 'count'])
#     for row in my_dict:
#         writer.writerow(row)

# filename = 'file.csv'
# def csv_columns(filename):
#     with open(r'C:\Users\Vadim\Downloads\file.csv', encoding='utf-8') as file:
#         rows = csv.DictReader(file)
#         my_dict = {}
#         for row in rows:
#             for key, val in row.items():
#                 my_dict.setdefault(key, []).append(val)
#         print(my_dict)

# with open(r'C:\Users\Vadim\Downloads\file.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file)
#     my_dict = {}
#     for row in rows:
#         for key, val in row.items():
#             my_dict.setdefault(key, []).append(val)
#     print(my_dict)


# with open('products.csv', encoding='utf-8') as file:
#    rows = csv.reader(file)                               # создаем reader объект
#    for i in rows:
#        print(row)


#     print(*rows)
#     name, grade = rows[0][0], rows[0][1]
#     my_dict = {name: [], grade: []}
#     for i in range(1, len(rows)):
#         my_dict[name].append(rows[i][0])
#         my_dict[grade].append(rows[i][1])
#         return my_dict
#
# csv_columns(text)
# n = int(input())
# with open(r'C:\Users\Vadim\Downloads\deniro.csv', 'r', encoding='utf-8') as file:
#     rows = list(csv.reader(file, delimiter=','))
#     if n == 1:
#         rows.sort(key=lambda x: x[n-1])
#     else:
#         rows.sort(key=lambda x: int(x[n-1]))
# for i in rows:
#     print(','.join(i))
# with open(r'C:\Users\Vadim\Downloads\salary_data.csv', 'r', encoding='utf-8') as file:
#     rows = csv.reader(file, delimiter=';')
#     next(rows)
#     print(rows)
#     my_dict = {}
#     for line in rows:
#         my_dict.setdefault(line[0], []).append(int(line[1]))
#     for key, val in my_dict.items():
#         my_dict[key] = sum(val) / len(val)
#     my_dict = sorted(my_dict.items())
#     result = sorted(my_dict, key=lambda x: x[1])
# for i in result:
#     print(i[0])


# with open(r'C:\Users\Vadim\Downloads\sales.csv', 'r', encoding='utf-8') as file:
#     rows = csv.reader(file, delimiter=';')
#     for item in rows:
#         if item[1].isdigit() and item[2].isdigit():
#             if int(item[1]) > int(item[2]):
#                 print(item[0])

# check
# check new branch
# import sys
#
# numbers = [int(line) for line in sys.stdin]
# delta_a = numbers[1] - numbers[0]
# delta_g = numbers[1] / numbers[0]
# is_ar, is_ge = True, True
# for i in range(2, len(numbers)):
#     if numbers[i] - numbers[i - 1] != delta_a:
#         is_ar = False
#         break
# for i in range(2, len(numbers)):
#     if numbers[i] / numbers[i - 1] != delta_g:
#         is_ge = False
#         break
# if is_ar:
#     print("Арифметическая прогрессия")
# if is_ge:
#     print("Геометрическая прогрессия")
# else:
#     print("Не прогрессия")

# dates = []
# for line in sys.stdin:
#     dates.append(datetime.datetime.strptime(line.strip(), '%d.%m.%Y'))
# for date in dates:
#     if dates.count(date) > 1:
#         repeat = True
#         break
#     else:
#         repeat = False
# if dates == sorted(dates) and repeat != True:
#     print("ASC")
# elif dates == sorted(dates, reverse=True) and repeat != True:
#     print("DESC")
# else:
#     print("MIX")

# news = dict()
# for line in sys.stdin:
#     if '/' in line:
#         text = line.strip().split("/")
#         if text[1].strip() not in news.keys():
#             news[text[1].strip()] = [[text[0].strip(), float(text[2].strip())]]
#         else:
#             news[text[1].strip()].append([text[0].strip(), float(text[2].strip())])
#     else:
#         result = sorted(news[line])
#         result = sorted(result, key=lambda x: x[1])
# for i in result:
#     print(i[0])

# for line in sys.stdin:
#     if not line.strip().startswith('#'):
#         print(line.rstrip())

# lst = []
# for line in sys.stdin:
#     lst.append(int(line))
# if len(lst) < 1:
#     print('нет учеников')
# else:
#     print(f'Рост самого низкого ученика: {min(lst)}')
#     print(f'Рост самого высокого ученика: {max(lst)}')
#     print(f'Средний рост: {sum(lst) / len(lst)}')

# import sys
# import datetime
#
# lst = []
# for line in sys.stdin:
#    lst.append(int(line.strip()))
# if len(lst) % 2 == 0:
#     last_step, another = "Дима", "Анри"
# else:
#     last_step, another = "Анри", "Дима"
# print(last_step if lst[-1] % 2 == 0 else another)

# lst = []
# for line in sys.stdin:
#     data = datetime.date.fromisoformat(line.strip())
#     lst.append(data.toordinal())
# sorted_lst = sorted(lst)
# delta = sorted_lst[-1] - sorted_lst[0]
# print(delta)
#
#

# for line in sys.stdin:
#     print("".join(reversed(line.strip())))


# gen = (for i in range(0, 101) for j in str(i) if int(j)

# for i in range(0, 101):
#     if i % 2 == 0:
#         s = 0
#         for j in str(i):
#             s += int(j)
#         if s != 8:
#             print(i)

# ✔Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# ✔Таблицу создайте в виде однострочного генератора, где каждый элемент генератора
# — отдельный пример таблицы умножения.
# ✔Для вывода результата используйте «принт» без перехода на новую строку.

# print('\n\n'.join(('\n'.join('\t\t'.join(f'{i:^3} x {j:^3} = {i * j:^3}' for i in range(i[0], i[1]))
# for j in range(2, 11)) for i in [(2,6), (6,10)])), sep='')

# import calendar
# import datetime
#
# def get_day_free(year):
#     for month in range(1, 13):
#         for week in calendar.monthcalendar(year, month):
#             thursday = week[3]
#             if thursday:
#                 print(datetime.date(year, month, thursday + 14).strftime("%d.%m.%Y"))
#                 break
#
# year = int(input())
# get_day_free(year)
# import datetime
#
# def get_all_mondays(year):
#     list_monday = []
#     first_day = datetime.date(year, 1, 1).weekday()
#     if first_day == 3:
#         first_th = datetime.date(year, 1, 1)
#         print(first_th, first_th.weekday())
#     else:
#         first_th = datetime.date(year, 1, 1 + (7 - first_day))
#         print(first_th.weekday(), first_th)
#     # while data_monday.year == year:
#     list_monday.append(data_monday)
#     data_monday = data_monday + datetime.timedelta(days=7)
# return list_monday


# get_all_mondays(2023)


# from itertools import chain, combinations
#
# items = {'Спальник': 5.0,
#          'Палатка': 10.0,
#          'Топор': 2.5,
#          'Еда': 7.0,
#          'Вода': 5.0,
#          'Бадминтон': 1.5,
#          'Радио': 3.0}
#
#
# def max_cargo(inventory: dict[str, float], capacity: int) -> list[list[str], float]:
#     backpack = [[], 0]
#     for item, weight in inventory.items():
#         if backpack[1] + weight <= capacity:
#             backpack[0].append(item)
#             backpack[1] += weight
#         else:
#             break
#     return backpack
#
#
# print(max_cargo(items, 30))
#
#
# def powerset(inventory: list[str]):
#     return chain.from_iterable(combinations(inventory, r) for r in range(len(inventory) + 1))
#
#
# def all_options(inventory: dict[str, float], capacity: int):
#     result = []
#     for cur_option in powerset(list(inventory)):
#         if cur_option:
#             weight = 0
#             for item in cur_option:
#                 weight += inventory.get(item)
#             if weight <= capacity:
#                 result.append((cur_option, weight))
#     return result
#
#
# for option in all_options(items, 30):
#     print(option)
#
#
# print(max_cargo(items, 30))
#
#
# def powerset(inventory: list[str]):
#     return chain.from_iterable(combinations(inventory, r) for r in range(len(inventory) + 1))
#
#
# def all_options(inventory: dict[str, float], capacity: int):
#     result = []
#     for cur_option in powerset(list(inventory)):
#         if cur_option:
#             weight = 0
#             for item in cur_option:
#                 weight += inventory.get(item)
#             if weight <= capacity:
#                 result.append((cur_option, weight))
#     return result
#
#
# for option in all_options(items, 30):
#     print(option)

# Решить задачи, которые не успели решить на семинаре

# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

# import re
#
# text = "Тверской бульвар был почти таким же, как и два года назад, когда я последний раз его видел – опять был февраль, " \
#        "сугробы и мгла, странным образом проникавшая даже в дневной свет. На скамейках сидели те же неподвижные старухи;" \
#        " вверху, над черной сеткой ветвей, серело то же небо, похожее на ветхий, до земли провисший под тяжестью" \
#        " спящего Бога матрац."
# 1
# def print_by_word(text: str):
#     my_list = re.sub(r'[.,"\'-?-:–!;]', "", text.lower()).split()
#     max_length = len(max(my_list, key=len))
#     sorted_list = sorted(my_list)
#
#     for i, el in enumerate(sorted_list, 1):
#         print(f"{i} {el:>{max_length}}")
#
# print_by_word(text)

# 2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

# list_ord = []
# for i in text:
#     list_ord.append(ord(i))
#     print(i)
# print(sorted(list_ord, reverse=True))

# 3
# Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

# def creat_dict():
#     print("Введите два числа через пробел: ")
#     a, b = input().split()
#     if int(a) < int(b):
#         min_ = int(a)
#         max_ = int(b)
#     else:
#         max_ = int(a)
#         min_ = int(b)
#     my_dict = dict()
#     for i in range(min_, max_ + 1):
#         str_ = ""
#         my_list = list(str(i))
#         for j in range(len(my_list)):
#             str_ += str(ord(my_list[j]))
#         my_dict[str_] = i
#     return my_dict
# print(creat_dict())
# print(ord('4'))
# 8
# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


# import calendar
# import datetime
#
# def get_days_in_month(year: int, month: str):
#     dates_list = []
#     lst_month = calendar.month_name
#     for i in range(13):
#         if month == lst_month[i]:
#             num_month = i
#             break
#     _, days = calendar.monthrange(year, num_month)
#     for i in range(1, days + 1):
#         data = datetime.date(year, num_month, i)
#         dates_list.append(data)
#     return dates_list


# ✔Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки. ✔Строки нумеруются начиная с единицы.
# ✔Слова выводятся отсортированными согласно кодировки Unicode. ✔Текст выравнивается по правому краю так,
# чтобы у самого длинного слова был один пробел между ним и номером строки.

# text = "У нас все хорошо. А будет еще лучшееее!"
#
# def every_word(text: str):
#     text = text.lower().split()
#     max_ = len(max(text, key=len))
#     text.sort()
#     for i, el in enumerate(text, 1):
#         print(f"{i} {el:>{max_}}")
#
# every_word(text)


# ✔Напишите функцию, которая принимает строку текста.
# ✔Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

# text = "У нас все хорошо!"
# def sorted_unicod(text):
#     my_list = []
#     for i in text:
#         if ord(i) not in my_list:
#             my_list.append(ord(i))
#     my_list.sort()
#     return my_list
# print(sorted_unicod(text))


# ✔Функция получает на вход строку из двух чисел через пробел.
# ✔Сформируйте словарь, где ключом будет символ из Unicode, а значением —  целое число
# ✔Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
#
# def creat_dict():
#     my_dict = {}
#     start, end = map(int, input("Введите два числа через пробел: ").split())
#     if start > end:
#         start, end = end, start
#     for i in range(start, end + 1):
#         my_dict[chr(i)] = i
#     return  my_dict
# print(creat_dict())


# Функция получает на вход список чисел. ✔Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔Как вариант напишите сортировку пузырьком. Её описание есть в википедии

# my_list = [5, 1, 34, 76, 12, 56, 3, 1, 92]
# print(my_list)
# def sorted_list(my_list):
#     for i in range(len(my_list)):
#         for j in range(len(my_list) - 1 - i):
#             if my_list[j] > my_list[j + 1]:
#                 my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
#                 # temp = my_list[j]
#                 # my_list[j] = my_list[j + 1]
#                 # my_list[j + 1] = temp
#
# sorted_list(my_list)
# print(my_list)


# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии

# name = ["Vasya", "Petya", "Ira"]
# salery = [100000, 230000, 60000]
# salary
# premium_ = [10.25, 15.4, 12.2]
# def premium(name, salery, premium):
#     my_dict = {}
#     for i in range(len(name)):
#         my_dict[name[i]] = salery[i] / 100 * premium_[i]
#     return my_dict
# print(premium(name, salery, premium_))
# import math
# import time
# import calendar
# import datetime
#
# year, month = input().split()
# months = list(calendar.month_name)
# for i in range(len(months)):
#     if months[i] == month:
#         print(calendar.monthrange(int(year), i)[1])

# data = datetime.datetime.strptime(input(), "%Y-%m-%d")
# days = list(calendar.day_name)
# print(days[data.weekday()])
# year, month = input().split()
# names = list(calendar.month_abbr)
# for i in range(len(names)):
#     if names[i] == month:
#         print(calendar.month(int(year), i))
#         break

# for i in range(int(input())):
#     year = int(input())
#     print(calendar.isleap(year))


# print(time.localtime(time.time()))
# def for_and_append():  # с использованием цикла for и метода append()
#     iterations = 10_000_000
#     result = []
#     for i in range(iterations):
#         result.append(i + 1)
#     return result
#
#
# def list_comprehension():  # с использованием списочного выражения
#     iterations = 10_000_000
#     return [i + 1 for i in range(iterations)]
#
# # def factorial_recurrent(n):  # рекурсивная функция
# #     if n == 0:
# #         return 1
# #     return n * factorial_recurrent(n - 1)
# #
# #
# # def factorial_classic(n):  # итеративная функция
# #     f = 1
# #     for i in range(2, n + 1):
# #         f *= i
# #     return f
#
#
# def get_the_fastest_func(funcs: list):
#     fast_f = funcs[0]
#     best_time = 9999999999999
#     for i in funcs:
#         start = time.perf_counter()
#         i()
#         finish = time.perf_counter()
#         delta = finish - start
#         print(delta)
#         if delta < best_time:
#             best_time = delta
#             fast_f = i
#     return fast_f
#
#
# lst = [for_and_append, list_comprehension]
# print(f"fast_funkt: {get_the_fastest_func(lst)}")

# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔Строки нумеруются начиная с единицы. ✔Слова выводятся отсортированными согласно кодировки Unicode.
# ✔Текст выравнивается по правому краю так,
# чтобы у самого длинного слова был один пробел между ним и номером строки.

# text = "У нас все хорошо, а будет еще лучше"
# my_list = text.split()
# my_list.sort('Unicod')
# for i, j in enumerate(my_list, 1):
#     print(f"{i} {j}")


# s = "Привет, как дела!"
# my_list = s.split()
# my_list.sort()
# print(my_list)
# new_list = enumerate(my_list, 1)
# for i, j in new_list:
#     print(f"{i} {j}")


# Создайте вручную кортеж содержащий элементы разных типов.
# ✔Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.
#
# my_tuple = (3, 4.5, True, "Hello", 5, False)
# my_dict = {}
# for i in my_tuple:
#     if type(i) not in my_dict:
#         my_dict[type(i)] = [i]
#     else:
#         my_dict[type(i)].append(i)
#
# print(my_dict)
#
# my_list = list(range(10))
# new_list = my_list[1::2]
# list_2 = list(enumerate(new_list))
# print(new_list)
# print(my_list)
# print(list_2)


# my_tuple = (1, 4.5, True, "Hello")
# my_dict = {}
# for i in range(len(my_tuple)):
#     my_dict[type(my_tuple[i])] = my_tuple[i]
# print(my_dict)


# from datetime import *
# from time import time
#
#
# def calculate_it(func, *args):
#     start_time = time.monotonic()
#     result = func(*args)
#     end_time = time.monotonic()
#     delta = end_time - start_time
#     return result, delta


# def choose_plural(amount, declensions):
#     d = amount % 10
#     h = amount % 100
#     if d == 1 and h != 11:
#         return f"{amount} {declensions[0]}"
#     elif 1 < d < 5 and not 11 < h < 15:
#         return f"{amount} {declensions[1]}"
#     else:
#         return f"{amount} {declensions[2]}"
#
# current_date = datetime.strptime(input(), "%d.%m.%Y %H:%M")
# release_date = datetime(2022, 11, 8, 12)
# time_left = release_date - current_date
# days, hours, minuts = time_left.days, time_left.seconds // 60 // 60, time_left.seconds // 60 % 60
# decl_days = ("день", "дня", "дней")
# decl_hours = ("час", "часа", "часов")
# decl_min = ("минута", "минуты", "минут")
# if current_date >= release_date:
#     print("Курс уже вышел!")
# elif days > 0 and hours > 0:
#     print(f"До выхода курса осталось: {choose_plural(days, decl_days)} и {choose_plural(hours, decl_hours)}")
# elif days > 0 and hours == 0:
#     print(f"До выхода курса осталось: {choose_plural(days, decl_days)}")
# elif days == 0 and hours > 0 and minuts > 0:
#     print(f"До выхода курса осталось: {choose_plural(hours, decl_hours)} и {choose_plural(minuts, decl_min)}")
# elif days == 0 and hours > 0 and minuts == 0:
#     print(f"До выхода курса осталось: {choose_plural(hours, decl_hours)}")
# elif days == 0 and hours == 0 and minuts > 0:
#     print(f"До выхода курса осталось: {choose_plural(minuts, decl_min)}")
# print(days)
# print(hours)
# print(minuts)
# print(time_left)
# year = 2020
# current_data = datetime.strptime(input(), "%d.%m.%Y").replace(year=year)
#
# border = timedelta(days=7)
# dic = {}
# for i in range(int(input())):
#     employee = input().split()
#     data_real = datetime.strptime(employee[2], "%d.%m.%Y")
#     data_fantom = datetime.strptime(employee[2], "%d.%m.%Y").replace(year=year)
#     if current_data < data_fantom <= current_data + timedelta(days=7) or current_data < data_fantom + timedelta(days=365) <= current_data + timedelta(days=7):
#     # if (data_fantom > current_data and data_fantom - current_data <= border) or \
#     #     (data_fantom > (current_data + timedelta(days=365)) and data_fantom - (current_data + timedelta(days=365)) <= border):
#         dic[data_real] = employee[0] + " " + employee[1]
# sorted_data = sorted(dic.items())
# if len(sorted_data) < 1:
#     print("Дни рождения не планируются")
# else:
#     print(sorted_data[-1][1])
#

#     data = datetime.strptime(input().split()[2],"%d.%m.%Y")
#     if data not in db.keys():
#
# fo
#         db[data] = 1
#     else:
#         db[data] +=1


#
# data = [5, 'text', 2.45, False, datetime.date(1988, 12, 21)]
# for i in range(0, len(data)):
#     print(i + 1, sep=" ")
#     print(data[i], sep=" ")
#     print(id(data[i]), sep=" ")
#     print(hash(data[i]), sep=" ")
#     if data[i] == int:
#         print("целое число", sep=" ")
#     else:
#         print("не целое число", sep=" ")
#     if data[i] == str:
#         print("это строка", sep=" ")
#     else:
#         print("это не строка", sep=" ")
#     print()
#
# num = '1024'
# print(int(num, 10))
# print(int(num, 8))
# print(int(num, 16))
#
# help(int)

# print(i, data[i], id(data[i]), hash(data[i]), "целое число" if data[i].isdecimal() else None, \
#       "string" if data[i].isalnum() else None)

# a: int = 23
# s: str = 'sld'
# b: float = 3.0
# print(type(b))

# text = input("Введите Ваш текст: ")
# if text.isdigit():
#     print(bin(int(text)), oct(int(text)), hex(int(text)))
# else:
#     print("Текст написан в кодировке ASCII" if text.isascii() else "Текст написан в другой кодировке")
#

# from datetime import datetime, timedelta
# from time import strptime, strftime
#
# db = {}
# for i in range(int(input())):
#     data = datetime.strptime(input().split()[2],"%d.%m.%Y")
#     if data not in db.keys():
#         db[data] = 1
#     else:
#         db[data] +=1
# db = dict(sorted(db.items()))
# sorted_tuple = sorted(db.items(), key=lambda x: x[1])
# for i in range(len(sorted_tuple)-1):
#     if sorted_tuple[i][1] == sorted_tuple[-1][1]:
#         print(sorted_tuple[i][0].strftime("%d.%m.%Y"))
# print(sorted_tuple[-1][0].strftime("%d.%m.%Y"))


# people = [input().split() for i in range(int(input()))]


# for i in range(n):
#     man = input().split()
#     people.append(man)
# sorted_people = sorted(people, key=lambda x: datetime.strptime(x[2], "%d.%m.%Y"))
# #print(sorted_people)
# bd = sorted_people[0][2]
# def fun(ls):
#     if ls[2] == bd:
#         return True
# old_men = list(filter(fun, sorted_people))
# if len(old_men) > 1:
#     print(bd, len(old_men))
# else:
#     print(bd, old_men[0][0], old_men[0][1])
# print(list(p))

# data1, data2 = datetime.strptime(input(), "%d.%m.%Y"), datetime.strptime(input(), "%d.%m.%Y")
# count = 3
# while data1 <= data2:
#     if data1.day + data1.month % 2 != 0 and data1.weekday() != 0 and data1.weekday() != 3 and count % 3 == 0:
#         print(data1)
#         data1 = data1 + timedelta(days=1)
#         count += 1
# print("Введите дату Вашего рождения в формате: dd.mm.yyyy")
# datebirth = datetime.strptime(input(), "%d.%m.%Y")
# age = datetime.now() - datebirth
# print(age.
# ag = age.fromordinal


# def fill_up_missing_dates(dates: list):
#     res = []
#     lst = sorted([datetime.strptime(i, "%d.%m.%Y") for i in dates])
#     currentdata = lst[0]
#     while currentdata <= lst[-1]:
#         res.append(currentdata.strftime("%d.%m.%Y"))
#         currentdata += timedelta(days=1)
#     return res
# dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
# fill_up_missing_dates(dates)
# result = []
# dates = input().split()
# for i in range(len(dates)-1):
#     result.append(abs(datetime.strptime(dates[i], "%d.%m.%Y").toordinal() - datetime.strptime(dates[i+1], "%d.%m.%Y").toordinal()))
# print(result)

# data = datetime.strptime(input(), '%d.%m.%Y')
# td = 0
# for i in range(2, 12):
#     print(datetime.strftime(data + timedelta(days=td), '%d.%m.%Y'))
#     td +=i
from datetime import date

# def saturdays(date1: date, date2: date):
# if date1 > date2: start, end = date2, date1
# else: start, end = date1, date2
# def num_of_sundays(year):
# #year = int(input())
#     start = datetime(year=year, month=1, day=1)
#     end = datetime(year=year, month=12, day=31)
#     days_start = start.toordinal()
#     days_end = end.toordinal()
#     firstsun = days_start + (6 - start.weekday())
#     # if firstsub < days_start:
#     #     firstsub +=7
#     return (days_end - firstsun) // 7 + 1
#
# year = 2000
# print(num_of_sundays(year))
# data = datetime(year=2023, month=5, day=29)
# print(data.weekday())

# lst = input().split(':')
# data = datetime(year=1, month=1, day=1, hour=int(lst[0]), minute=int(lst[1]), second=int(lst[2]))
# delta = timedelta(seconds=int(input()))
# print((data + delta).time())
# lst = input().split('.')
# delta = timedelta(hours=float(lst[0]), minutes=float(lst[1]), seconds=float(lst[2]))
# print(round(delta.total_seconds()))

# print(delta.total_seconds())
# data = datetime.strptime(input(), '%d.%m.%Y')
# print((data - timedelta(hours=24)).strftime('%d.%m.%Y'), (data + timedelta(hours=24)).strftime('%d.%m.%Y'), sep='\n')
#
# today = date(2021, 11, 4)
# birthday = date(2022, 10, 6)
#
# days = birthday - today
#
# print(days.days)

# from datetime import datetime, timedelta
#
# dt = datetime(2021, 11, 4, 13, 6) + timedelta(days=7, hours=12)
#
# print(dt.strftime('%d.%m.%Y %H:%M:%S'))

# def is_available_date(b_d: list, d_f_b: str):
#     booked = set()
#     for_book = set()
#     for i in b_d:
#         if '-' in i:
#             lst = i.split('-')
#             start_data = datetime.strptime(lst[0], "%d.%m.%Y").toordinal()
#             finish_data = datetime.strptime(lst[1], "%d.%m.%Y").toordinal()
#             for j in range(start_data, finish_data + 1):
#                 booked.add(j)
#         else:
#             data = datetime.strptime(i, "%d.%m.%Y").toordinal()
#             booked.add(data)
#     if '-' in d_f_b:
#         lst = d_f_b.split('-')
#         start_data = datetime.strptime(lst[0], "%d.%m.%Y").toordinal()
#         finish_data = datetime.strptime(lst[1], "%d.%m.%Y").toordinal()
#         for j in range(start_data, finish_data + 1):
#             for_book.add(j)
#     else:
#         data = datetime.strptime(d_f_b, "%d.%m.%Y").toordinal()
#         for_book.add(data)
#     if booked.intersection(for_book):
#         return False
#     else:
#         return True

# with open(r'\Users\Vadim\Downloads\diary.txt', 'r', encoding='utf-8') as file:
#     lst = file.readlines()
#
# res_dic = {}
# list_all = []
# list_mess = []
# index = -1
# for i in range(len(lst)):
#     index = i
#     if not lst[i].strip():
#         list_all.append(list_mess)
#         list_mess = []
#     else:
#         list_mess.append(lst[i])
# list_mess.pop(len(list_mess) - 1)
# list_mess.append(lst[index] + '\n')
# list_all.append(list_mess)
# for i in range(len(list_all)):
#     data = datetime.strptime(list_all[i][0].strip(), "%d.%m.%Y; %H:%M")
#     res_dic[data] = []
#     for j in range(1, len(list_all[i])):
#         res_dic[data].append(list_all[i][j])
# res_sorted = sorted(res_dic.items())
# for i in range(len(res_sorted)):
#     datas = datetime.strftime(res_sorted[i][0], "%d.%m.%Y; %H:%M")
#     print(datas)
#     for j in range(len(res_sorted[i][1])):
#         print(res_sorted[i][1][j], end="")
#     if i < len(res_sorted) - 1:
#         print()
#     # print(*res_sorted[i][1])
# from datetime import date, time, datetime
#
# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
#         'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
#         'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
#         'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
#         'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
#         'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
#         'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
#         'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
#         'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
#         'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
#
# result = {}
# lst_key = list(data.keys())
# for i in range(len(lst_key)):
#     start_sec = datetime.strptime(data[lst_key[i]][0], "%d.%m.%Y %H:%M:%S").timestamp()
#     finish_sec = datetime.strptime(data[lst_key[i]][1], "%d.%m.%Y %H:%M:%S").timestamp()
#     dif = finish_sec - start_sec
#     result[lst_key[i]] = dif
# sorted_result = sorted(result.items(), key=lambda items: items[1])
# print(sorted_result[0][0])
# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
# lst = []
# for i in range(len(dates)):
#     lst.append(datetime.combine(dates[i], times[i]))
# lst = sorted(lst, key=lambda x: x.second)
# for data in lst:
#     print(data)
# map(lambda x: x.time().second, lst)

# from datetime import time
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
#
# num = 0
# check_data = time(12)
# print(check_data)
# for data in times_of_purchases:
#     if data.time() > check_data:
#         print(data.time())
#         num += 1
#     else:
#         num -= 1
# if num > 0:
#     print('После полудня')
# else:
#     print('До полудня')
# def is_correct(day, month, year):
#     try:
#         my_date = date(year, month, day)
#         return True
#     except:
#         return False
#
# num_correct = 0
# data = ''
# # while not (data == "end"):
# while True:
#     data = input()
#     if data == "end":
#         break
#     lst = data.split('.')
#     try:
#         my_data = date(int(lst[2]), int(lst[1]), int(lst[0]))
#         print("Корректная")
#         num_correct += 1
#     except:
#         print("Некорректная")
# print(num_correct)


# def print_good_dates(dates: list):
#     good_lst = []
#     for data in dates:
#         if data.year == 1992 and data.month + data.day == 29:
#             good_lst.append(data)
#     good_lst = sorted(good_lst)
#     for data in good_lst:
#         print(data.strftime('%B %d, %Y'))
#
# dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
# print_good_dates(dates)

# n = int(input())
# lst = []
# for i in range(n):
#   lst.append(date.fromisoformat(input()))
# lst = sorted(lst)
# for i in range(n):
#     print(lst[i].strftime("%d/%m/%Y"))
# date1 = date.fromisoformat(input())
# date2 = date.fromisoformat(input())
# if date2 < date1:
#     print(date2.strftime("%d-%m (%Y)"))


# from datetime import date
#
# from datetime import date
#
# andrew = date(1992, 8, 24)
#
# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%j'))   # выводим дату в формате YYYY-day_number

# from datetime import date
#
# def saturdays_between_two_dates(date1: date, date2: date):
#     if date1 > date2: start, end = date2, date1
#     else: start, end = date1, date2
#     days_start = start.toordinal()
#     days_end = end.toordinal()
#     firstsub = days_start + (5 - start.weekday())
#     if firstsub < days_start:
#         firstsub +=7
#     return (days_end - firstsub) // 7 + 1
#
# date1 = date(2018, 7, 13)
# date2 = date(2018, 7, 13)
#
# print(saturdays_between_two_dates(date1, date2))


# from datetime import date
#
# def get_date_range(date1: date, date2: date):
#     lst = []
#     days1 = date1.toordinal()
#     days2 = date2.toordinal()
#     while days1 <= days2:
#         lst.append(date.fromordinal(days1))
#         days1 +=1
#     return lst
# date1 = date(2019, 6, 5)
# date2 = date(2022, 6, 6)
# print(len(get_date_range(date1, date2)))
#
#
# print(*get_date_range(date(2021, 10, 1), date(2021, 10, 5)))
# dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
#
# def get_min_max(dates):
#     if dates:
#         return min(dates), max(dates)
#     return ()
#
# print(get_min_max(dates))
# # счетчик для нужного количества ураганов
# import datetime
#
# from datetime import date
#
# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

# # импортируем тип date из модуля datetime
# import datetime
# from datetime import date
#
# # создаем объект, соответсвующий дате урагана
# hurricane_andrew = datetime.date(1992, 8, 24)
#
# # выводим день недели
# print(hurricane_andrew.weekday())

# def counter(lst: []):
#     b = 0
#     if lst[2].rstrip() == 'B':
#         b = int(lst[1])
#     elif lst[2].rstrip() == 'KB':
#         b = int(lst[1]) * 1024
#     elif lst[2].rstrip() == 'MB':
#         b = int(lst[1]) * 1024 * 1024
#     elif lst[2].rstrip() == 'GB':
#         b = int(lst[1]) * 1024 * 1024 * 1024
#     return b
#
# def converter(b: int):
#     if b < 1024:
#         return f'{b} B'
#     elif b < 1024 * 1024:
#         return f'{round(b / 1024)} KB'
#     elif b < 1024 * 1024 * 1024:
#         return f'{round(b / 1024 / 1024)} MB'
#     elif b >= 1024 * 1024 * 1024:
#         return f'{round(b / 1024 / 1024 / 1024)} GB'
#
#
# with open(r'\Users\Vadim\Downloads\files.txt', 'r', encoding='utf-8') as file:
#     lst = file.readlines()
# d = {}
# print(sorted(lst))
# for i in range(len(lst)):
#     key = lst[i].split()[0].split('.')[-1]
#     if key in d.keys():
#         d[key].append(lst[i])
#     else:
#         d[key] = [lst[i]]
#
# sorted_list = sorted(d.items())
# print(sorted_list)
# dict_sizes = {}
#
# for i in sorted_list:
#     dict_sizes[i[0]] = converter(sum(map(lambda x: counter(x.split()), i[1])))
#
# for i in sorted_list:
#     slst = sorted(i[1])
#     for j in slst:
#         print(j.split()[0])
#     print('-' * 10)
#     print(f"Summary: {dict_sizes[i[0]]}")
#     print()

# for i in range(len(lst)):
#     s.add(lst[i].split()[0].split('.')[-1])

# set.add(lst[i].split()[-1])
# print(s)
# print(type(s))
# s = sorted(s)
# print(s)
# print(type(s))
# lst2 = []
# for i in s:
#     for j in lst:
#         if j.split()[0].split('.')[-1] == i:
#             lst2.append(s[i])

# d = {'er': 3, '4sr': 9, 'dkt': ''}
# print(d)
# s = d.get('45', 12)
# print(s)
# print(d)
# n = int(input())
# emails = [input() for i in range(n)]
# m = int(input())
# names = [input() for i in range(m)]
# #dic = {}
#
# for i in names:
#     ema = f"{i}@beegeek.bzz"
#     if ema not in emails:
#         print(ema)
#         emails.append(ema)
#     else:
#         for j in range(1,100):
#             ema = f"{i}{j}@beegeek.bzz"
#             if ema not in emails:
#                 print(ema)
#                 emails.append(ema)
#                 break

# for i in range(len(emails)):
#     flag = True
#     for j in range(len(emails[i])):
#         if emails[i][j].isdigit():
#             # num += emails[i][j]
#             # if emails[i][j+1].isdigit():
#             #     num += emails[i][j+1]
#             fio = emails[i][:j]
#             dic[fio] = dic[fio] + 1
#             print(fio, dic[fio], 'n')
#             flag = False
#             break
#     if flag:
#         fio = emails[i][:-12]
#         dic[fio] = 0
#         print(fio, dic[fio], 't')
#
#
# for i in names:
#     if i in dic.keys():
#         #if dic[i] == 0:
#         print(f"{i}{dic[i]+1}@beegeek.bzz")
#     else:
#         dic[i] = 0
#         print(f"{i}@beegeek.bzz")


# vowels = 'а, у, о, ы, и, э, я, ю, ё, е'
# conson = 'б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ'
# origin = list(input())
# n = int(input())
# words = [input() for _ in range(n)]
# check = ['v' if i in vowels else 'n' for i in origin]
# checkword = "".join(check)
# lastindex = checkword.rfind('v')
# checkword = checkword[:lastindex + 1]
# for i in words:
#     word = list(i)
#     checkw = ['v' if j in vowels else 'n' for j in word]
#     checkthis = "".join(checkw)[:lastindex + 1]
#     if checkthis == checkword:
#         print(i)

# n = int(input())
# lst = [input() for i in range(n)]
# result = []
# first = lst[0].split(', ')
# for i in range(len(first)):
#     flag = True
#     for j in range(1, n):
#         if first[i] not in lst[j]:
#             flag = False
#     if flag:
#         result.append(first[i])
# result = sorted(result)
# if len(result) == 0:
#     print("Сериал снять не удастся")
# else:
#     print(*result, sep=', ')
#

# lst = [i for i in range(1, int(input()) + 1)]
# di = {}
# for num in lst:
#     summ = 0
#     while num != 0:
#         dig = num % 10
#         summ += dig
#         num //= 10
#     if summ in di.keys():
#         di[summ] += 1
#     else:
#         di[summ] = 1
# result = sorted(di.items(), key=lambda x: x[1])
# print(result[-1][-1])

# lst = [int(i) for i in input().split()]
# s = set()
# res = []
# for i in lst:
#     print(type(i))
#     if i in s:
#         res.append(i)
#     else:
#         s.add(i)
# print(*sorted(set(res)))

# def perevorator():
#     arg = [int(i) for i in input().split()]
#     n, x, y, a, b = arg[0], arg[1], arg[2], arg[3], arg[4]
#     lst = [i for i in range(0, n + 1)]
#     lst3 = lst[: x] + lst[y:x-1: -1] + lst[y+1:]
#     lst4 = lst3[:a] + lst3[b:a-1:-1] + lst3[b+1:]
#     lst4 = lst4[1:]
#     print(*lst4)
#
# perevorator()
# for i in range(lst4):

# n, x, y, a, b = int(input()), int(input()), int(input()), int(input()), int(input())
# perevorator(9, 3, 6, 5, 8)

# en, ru = 'AaBCcEeHKMOoPpTXxy', 'АаВСсЕеНКМОоРрТХху'
# e, r = 0, 0
# for i in range(3):
#     if input() in en:
#         e +=1
#     else:
#         r +=1
# if e == 3: res = "en"
# elif r == 3: res = "ru"
# else: res = "mix"
# print(res)
# print(e, r)

# def timur(d1, d2, d3):
#     a = d1 + d2 + d3
#     lst = sorted([d1, d2, d3])
#     if lst[0]*2 + lst[1]*2 > a:
#         print(a)
#     else:
#         print(lst[0]*2 + lst[1]*2)
#
# timur(100, 33, 34)
# def get_biggest(numbers):
#     if len(numbers) == 0:
#         return -1
#     else:
#         numbers = [str(i) for i in numbers]
#         m = len(max(numbers, key=len))
#         print(m)
#         numbers = sorted(numbers, key=lambda x: x * m, reverse=True)
#         if int(''.join(numbers)) == 0:
#             return '0'
#         else:
#             print(numbers)
#             return ''.join(numbers)

# key=lambda x, y: max(x, y) if len(x) == len(y) else max(len(x), len(y)
# print(get_biggest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
# get_biggest([5, 3, 9, 1])
# def choose_plural(amount, declensions):
#     d = amount % 10
#     h = amount % 100
#     if d == 1 and h != 11:
#         return f"{amount} {declensions[0]}"
#     elif 1 < d < 5 and not 11 < h < 15:
#         return f"{amount} {declensions[1]}"
#     else: return f"{amount} {declensions[2]}"
#
# print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))


# def spell(*args):
#     d = {}
#     for word in args:
#          if word.lower()[0] not in d.keys():
#              d[word.lower()[0]] = len(word)
#          else:
#              if d[word.lower()[0]] < len(word):
#                     d[word.lower()[0]] = len(word)
#     return d
#
#
# print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
# def index_of_nearest(numbers, num):
#     if len(numbers) == 0:
#         return -1
#     else:
#         ind = 0
#         dif = abs(numbers[0] - num)
#         for i in range(len(numbers)):
#             if abs(numbers[i] - num) < dif:
#                 dif = abs(numbers[i] - num)
#                 ind = i
#     return ind
# print(index_of_nearest([], 17))


# def likes(names):
#     if len(names) == 0:
#         return "Никто не оценил данную запись"
#     if len(names) == 1:
#         return names[0] + " оценил(а) данную запись"
#     if len(names) == 2:
#         return names[0] + ' и ' + names[1] + " оценили данную запись"
#     if len(names) == 3:
#         return names[0] + ', ' + names[1] + ' и ' + names[2] + " оценили данную запись"
#     if len(names) > 3:
#         return names[0] + ', ' + names[1] + ' и ' + str(len(names) - 2) + " других оценили данную запись"
#
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))
# def filter_anagrams(word, words):
#     lst = []
#     for w in words:
#         if sorted(list(w)) == sorted(list(word)):
#             lst.append(w)
#     return lst


# def convert(st):
#     s = list(st)
#     u, l = 0, 0
#     for word in s:
#         if word.isalpha() and word.isupper():
#             u +=1
#         if word.isalpha() and word.islower():
#             l +=1
#     if l >= u:
#         return st.lower()
#     else:
#         return st.upper()
#
# print(convert('pi31415!'))

# def print_given(*args, **kwargs):
#     for i in args:
#         print(i, type(i))
#     sorted_kwargs = dict(sorted(kwargs.items()))
#     for i, j in sorted_kwargs.items():
#         print(i, j, type(j))
# print_given(1, [1, 2, 3], 'three', two=2)
# def is_valid(s):
#     if 3 < len(s) < 7 and s.isdigit() and ' ' not in s:
#         return True
#     else:
#         return False
# print(is_valid('92134'))

# def same_parity(numbers):
#     return [i for i in numbers if numbers[0] % 2 == i % 2]
# lst = []
# for num in numbers:
#     if numbers[0] % 2 == num % 2:
#         lst.append(num)
# #return lst
# return [i for  i in numbers if numbers[0] % 2 == i % 2]
# print(same_parity([6, 0, 67, -7, 10, -20]))
# num = '2345 5883 3958 23 94'
# def hide_card(num):
#     num = num.replace(' ', '')
#     return '************' + num[-4:]
# print(hide_card(num))


# with open(input(), 'r') as file:
#     text = file.readlines()
# num = 0
# for i in range(len(text)):
#     if text[i].startswith('def ') and not text[i-1].startswith('#'):
#         index = text[i].find('(')
#         print(text[i][4:index])
#         num += 1
# if num == 0:
#     print('Best Programming Team')


# with open(r'\Users\Vadim\Downloads\cyrillic.txt', 'r', encoding='utf-8') as file,\
#     open(r'\Users\Vadim\Downloads\transliteration.txt', 'a', encoding='utf-8') as translit:
#     text = file.read()
#     d = {'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n',
#      'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y',
#      'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j',
#      'ф': 'f', 'я': 'ya', 'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch',
#      'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo',
#      'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U',
#      'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya'}
#     for i in range(len(text)):
#         if text[i] in d.keys():
#             translit.write(d[text[i]])
#         else:
#             translit.write(text[i])

# with open(r'\Users\Vadim\Downloads\data1.txt', 'r') as file,\
#     open(r'\Users\Vadim\Downloads\forbidden_words1.txt', 'r') as prohibit:
#     text = file.read()
#     textsmall = text.lower()
#     proh = prohibit.read().split()
# for i in proh:
#     textsmall = textsmall.replace(i, len(i) * '*')
# for i in range(len(text)):
#     if textsmall[i] == '*':
#         print('*', end='')
#     else:
#         print(text[i],end='')
#         text[i] = '*'
# print(text)

# with open(r'\Users\Vadim\Downloads\data1.txt', 'r') as file,\
#     open(r'\Users\Vadim\Downloads\forbidden_words1.txt', 'r') as prohibit:
#     lst = file.readlines()
#     proh = prohibit.read().split()
#     for line in lst:
#         text = line.split()
#             #text = file.read().split()
#
#         # print(text)
#         # print()
#         # print()
#         # print(proh)
#         # print()
#         # print()
#
#         for i in range(len(text)):
#             for j in range(len(proh)):
#                 if text[i].casefold().find(proh[j]) != -1:
#                     # print(j, proh[j])
#                     # print(text[i])
#                     # print(text[i].lower())
#                     # print(proh[j])
#                     text[i] = text[i].casefold().replace(proh[j], len(proh[j]) * '*')
#                     # print(i)
#                     # print(text[i])
#                     # print()
#         result = ' '.join(text) + ' '
#         print(result)
# with open(r'\Users\Vadim\Downloads\ledger.txt', 'r') as file:
#     lst = file.readlines()
#     if len(lst) < 100:
#         for i in lst:
#             print(i.rstrip())
#     else:
#         for i in range(-10, 1, 1):
#             print(lst[i].rstrip())

# with open(r'\Users\Vadim\Downloads\words.txt', 'r') as file:
#     text = file.read().split()
#     maxim = len(max(text, key=lambda x: len(x)))
#     for word in text:
#         if len(word) == maxim:
#             print(word)

# with open('grades.txt', 'r') as file:
#     count = 0
#     for line in file:
#         lst = line.split()
#         if int(lst[1]) > 64 and int(lst[2]) > 64 and int(lst[3]) > 64:
#             count +=1
# print(count)
# with open('ledger.txt', 'r') as file:
#     lst = file.readlines();
# s = 0
# for i in range(len(lst)):
#     s += int(lst[i][1:])
# print('$' + str(s))


# with open(input(), 'r') as file:
#     lst = file.readlines();
#     print(len(lst))

# def time_counter(start, finish):
#     st = start.split(':')
#     fist = int(st[0]) * 60 + int(st[1])
#     fn = finish.split(':')
#     second = int(fn[0]) * 60 + int(fn[1])
#     return second - fist
#
#
# with open(r'\Users\Vadim\Downloads\logfile.txt', 'r', encoding='utf-8') as file, open(r'\Users\Vadim\Downloads\output.txt', 'a', encoding='utf-8') as output:
#     lst = file.readlines()
#     for line in lst:
#         line = line.split(', ')
#         start = line[1]
#         finish = line[2]
#         dif = time_counter(start, finish)
#         if dif >= 60:
#             output.write(line[0] + '\n')
#             print(line[0], dif)

# n = int(input())
# with open('output.txt', 'a', encoding='utf-8') as output:
#     for i in range(n):
#         filename = input()
#         file = open(filename, 'r')
#         content = file.readlines()
#         output.writelines(content)
#         file.close()
#
#
#
# Шаповалов Вадим Владимирович 21.12.88 m 34858686
# Иванов Иван Иванович 23838485 21.23.12 m
# Сидоров Петр Иванович 21.32.45 38485 m
# Иванов Андрей Иванович 348485 3.2.67 m
# Пичугина Наталья Андреевна 21ю11ю90 394895 f
# Сидоров Антон Иванович 21.8.45 384466585 m
#
# with open(r'\Users\Vadim\Downloads\goats.txt', 'r', encoding='utf-8') as file, \
#         open(r'\Users\Vadim\Downloads\answer.txt', 'w', encoding='utf-8') as output:
#     lst = file.readlines()
#     pink = []
#     number_goats = []
#     for i in range(1,len(lst)):
#         if not lst[i].rstrip() == "GOATS":
#             pink.append(lst[i].rstrip())
#         else:
#             break
#     goats = lst[len(pink) + 2:]
#     for i in range(len(goats)):
#         goats[i] = goats[i].rstrip()
#     for i in pink:
#         num = goats.count(i)
#         number_goats.append((num, i))
#     result = []
#     for i in number_goats:
#         if (i[0] / (len(goats) / 100) > 7):
#             result.append(i[1])
#     result.sort()
#     for i in result:
#         output.write(i + '\n')
# with open(r'\Users\Vadim\Downloads\class_scores.txt', 'r', encoding='utf-8') as file, \
#         open(r'\Users\Vadim\Downloads\new_scores.txt', 'w', encoding='utf-8') as output:
#     lst = file.readlines();
#     for line in lst:
#         line = line.rstrip().split()
#         line[1] = int(line[1]) + 5
#         if line[1] > 100:
#             line[1] = 100
#         line[1] = str(line[1])
#         s = ' '.join(line)
#         output.write(s + '\n')

# import random
#
# with open(r'\Users\Vadim\Downloads\input.txt', 'r', encoding='utf-8') as file,\
#         open(r'\Users\Vadim\Downloads\output.txt', 'w', encoding='utf-8') as output:
#     lst = file.readlines()
#     for i in range(len(lst)):
#         print(str(i + 1) + ') ' + lst[i].rstrip(), file=output)

# for i in range(25):
#     output.write(str(random.randint(111, 778)) + '\n')

# def read_csv():
#     with open(r'\Users\Vadim\Downloads\data.csv') as file:
#         lst = []
#         lst2 = []
#         for i in file.readlines():
#             i = i.rstrip()
#             line = i.split(',')
#             lst.append(line)
#     for i in range(1, len(lst)):
#         d = {}
#         for j in range(len(lst[i])):
#             d[lst[0][j]] = lst[i][j]
#         lst2.append(d)
#     return lst2
# print(lst)
# with open(r'\Users\Vadim\Downloads\population.txt') as file:
#     s = file.readlines()
# lst = []
# for line in s:
#     line = line.split('\t')
#     lst.append(line)
# for i in range(len(lst)):
#     if lst[i][0].find('G') == 0 and int(lst[i][-1].rstrip()) > 500000:
#         print(lst[i][0])
# import random
#
# with open(r'\Users\Vadim\Downloads\first_names.txt') as names, open(r'\Users\Vadim\Downloads\last_names.txt') as lastnames:
#     lstname = names.readlines()
#     lstlastname = lastnames.readlines()
# for i in range(3):
#     print(f'{random.choice(lstname).strip()} {random.choice(lstlastname).strip()}')

# with open(r'\Users\Vadim\Downloads\file.txt') as file:
#     text = file.read()
# letters = 0
# lines = text.count('\n') + 1
# words = text.split()
# for i in text:
#     if i.isalpha():
#         letters +=1
# print('Input file contains:')
# print(f'{letters} letters')
# print(f'{len(words)} words')
# print(f'{lines} lines')
# lst = text.split()
# #lst2 = list(s)
# s2 = text.replace('.', '').replace(' ', '')
# lst2 = list(s2)
# print(len(lst2))
# l = len(lst)
# print(l)

#
# print(k)
# s = '3er45'
# s = list(s)
# s[1] = 'R'
# print(s)
# print(''.join(s))


# line = 'aaa456\n'
# line = list(line)
# for i in range(len(line)):
#     if not line[i].isdigit():
#         print(line[i])
#         line[i] = ' '
#         print(i, 2)
# print(line)
# with open(r'\Users\Vadim\Downloads\nums.txt') as file:
#     lst = file.readlines()
# s = 0
# for line in lst:
#     line = list(line)
#     for i in range(len(line)):
#         if not line[i].isdigit():
#             line[i] = ' '
#     line = ''.join(line)
#     line = line.split()
#     for j in line:
#         s += int(j)
# print(s)

# with open(r'C:\Users\Vadim\Downloads\numbers.txt') as file:
#     lst = file.readlines()
#     print(lst)
# for line in lst:
#     line = line.split()
#     s = 0
#     for i in line:
#         #print(i)
#         if i.isdigit():
#             s += int(i)
#     print(s)

# with open(r'C:\Users\Vadim\Downloads\lines.txt') as file:
#     lst = file.readlines()
#     length = len(max(lst, key=len))
#     print(length)
#     for line in lst:
#         #print(line)
#         if len(line) == length:
#             print(line.strip())


# file = open('prices.txt')
# sum = 0
# for line in file:
#     lst = line.split('\t')
#     sum += int(lst[1]) * int(lst[2])
# print(sum)
# file.close()

# lst = file.read().split()
# print(int(lst[0]) + int(lst[1]))
# file.close()
# a = int(file.readline().strip())
# b = int(file.readline().strip())
# print(a + b)
# import random
#
# file = open(r'C:\Users\Vadim\Downloads\lines.txt', 'r', encoding='UTF-8')
# lst = file.readlines()
# #print(lst)
# print(random.choice(lst))

# name = input()
# file = open(name)
# lst = file.readlines()
# print(lst[-2].strip())
# file.close()

# n = int(input())
# lst = [input() for i in range(int(input()))]
# for i in range(n):
#     lst.append(input())
#
# def fu(s):
#     s = s.split('.')
#     s = list(map(int, s))
#     num = s[0]*256**3 + s[1]*256**2 + s[2]*256**1 + s[3]
#     return num
#
# map(lambda s: s[0]*256**3 + s[1]*256**2 + s[2]*256**1 + s[3], list(map(int, s.split)))
#
# print(*sorted([input() for i in range(int(input()))], key=fu), sep='\n')

# n = int(input())
# for i in range(n):
#     s = input().upper()
#     num = 0
#     for j in s:
#         num += ord(j)
# def gem(s):
#     s = s.upper()
#     num = 0
#     for j in s:
#         num += ord(j) - ord('A')
#     return num
# # s = 'BaSis'
# # print(gem(s))
#
# lst = [input() for i in range(int(input()))]
# for i in lst:
#     print(i, gem(i))
# print(lst)
# print(*sorted(lst, key=gem), sep='\n')
# print(*lst, sep='\n')
#
# print(*sorted(sorted([input() for i in range(int(input()))]), key=gem), sep='\n')
# for i in range(int(input())):
#     lst.append(input())


# a = 'cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats CatAlo'.split()
# print(type(a))
# print(*sorted(input().split(), key=lambda x: x.lower()))
# def arithmetic_operation(operation):
#     if operation == '+':
#         return lambda x, y: x + y
#     if operation == '-':
#         return lambda x, y: x - y
#     if operation == '*':
#         return lambda x, y: x * y
#     if operation == '/':
#         return lambda x, y: x / y
#
# add = arithmetic_operation('+')
# div = arithmetic_operation('/')
#
# print(add(10, 20))
# print(div(20, 5))

# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
# def compose(fu, fu2):
#     return lambda x: fu(fu2(x))
#
#
# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))

# def mul7(x):
#     return x * 7
#
#
# def add2(x, y):
#     return x + y
#
#
# def add3(x, y, z):
#     return x + y + z
#
# def call(fu, *args):
#     return fu(*args)
#
# print(call(mul7, 10))
# print(call(add2, 2, 7))
# print(call(add3, 10, 30, 40))
# print(call(bool, 0))

# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
#
# sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)
#
# print(sorted_numbers)

# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*filter(lambda x: x != int(str(x)[::-1]), numbers))

# words = 'the world is mine take a look what you have started'.split()
#
# print(*map(lambda x: '"' + x + '"', words))

# from functools import reduce
#
# def product_of_odds(data):   # data - список целых чисел
#     return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)
#     result = 1
#     for i in data:
#         if i % 2 == 1:
#             result *= i
#     return result
# reduce(lambda x, y: x * y, map(filter(lambda x: x % 2 == 1, data)), 1)
# print(product_of_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# def concat(*args, sep=' '):
#     return sep.join(map(str, args))

# def pretty_print(data, side='-', delimiter='|'):
#     st2 = delimiter + ' ' + f' {delimiter} '.join(map(str, data)) + ' ' + delimiter
#     st = ' ' + side * (len(st2) - 2) + ' '
#     print(st)
#     print(st2)
#     print(st)
#
# pretty_print([1, 2, 10, 23, 123, 3000])

# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     return f'''To: {mail}
# Приветствую, {name}!
# Вам назначен экзамен, который пройдет {date}, в {time}.
# По адресу: {place}.
# Экзамен будет проводить {teacher} в кабинете {number}.
# Желаем удачи на экзамене!'''
#
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))
# lst = []
# for i in range(int(input())):
#     lst2 = []
#     for j in range(int(input())):
#         p = input().split()
#         if int(p[1]) == 5:
#             lst2.append(True)
#         else:
#             lst2.append(False)
#     if any(lst2):
#         lst.append(True)
#     else:
#         lst.append(False)
# if all(lst):
#     print("YES")
# else:
#     print("NO")
#
# lst2.append(any(map(lambda p: True if int(p[1]) == 5 else False, input().split())))
# s = input()
# print(('YES', 'NO')[any([len(s) < 7, s.islower(), s.isupper(), s.isalpha(), s.isdigit()])])

# par = input()
# if all([any(map(lambda x: x.isdigit(), par)), any(map(lambda  x: x.isupper(), par)), any(map(lambda x: x.islower(), par)), len(par) > 6]):
#     print("YES")
# else:
#     print("NO")


# a, b = int(input()), int(input())
# lst = [i for i in range(a, b + 1) if '0' not in str(i)]
# lst2 = []
# for i in lst:
#     if all(map(lambda x: True if i % int(x) == 0 else False, str(i))):
#         lst2.append(i)
# print(*lst2)

# if all(map(lambda x, i: True if i % int(x) == 0 else False, str(i))):
#     lst3.append(i)
# ip = [int(i) for i in input().split(".")]
# print(all(i.isdigit() and 0 <= int(i) <= 255 for i in input().split(".")))
# abscissas = []
# ordinates = []
# applicates = []
# abscissas = [float(i) for i in input().split()]
# ordinates = [float(i) for i in input().split()]
# applicates = [float(i) for i in input().split()]
# #print(all(map(lambda x, y, z: x**2 + y**2 + z**2 == 4, zip(abscissas, ordinates, applicates))))
# print(all(map(lambda x: x[0]**2 + x[1]**2 + x[2]**2 <= 4, zip(abscissas, ordinates, applicates))))
# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
# # <capital> is the capital of <country>, population equal <population> people.
#
# for co, ca, po in zip(countries, capitals, population):
#     print(f"{ca} is the capital of {co}, population equal {po} people.")
# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     return any(map(lambda x: x in command, ignore))
# ignore_command('get ip')
# from functools import reduce
#
# def evaluate():
#     coefficients = [int(i) for i in input().split()]
#     x = int(input())
#     step = [i for i in range(len(coefficients)-1, -1, -1)]
#     res = reduce(lambda c, d: c + d, list(map(lambda a, b: a * x ** b, coefficients, step)))
#     return res
#   n, y= x**(len(coefficients)-1-coefficients.index(n)): y , coefficients)

#     mn = 0
#     lengf = len(coefficients)
#     for i in range(lengf-1):
#         mn += coefficients[i] * (x **(lengf-1-i))
#     mn += coefficients[-1]
#     print(mn)
# coefficients = [1, 2, 3, 4, 5, 6, 7]
# x = 1
# print(evaluate())

# lst = [int(i) for i in input().split()]
# ls = lambda x: 255 - x
# print(*map(lambda x: 255 - x, [int(i) for i in input().split()]))

# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
#
# print(sorted(mixed_list, key=lambda x: (0 if type(x) == int else 1, x)))

# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
#
# print(max(mixed_list, key= lambda x: x if type(x) == int else 0))
# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
# print(*sorted(sorted(data), key=lambda x: len(x)))

# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
# data = sorted(data, key=lambda x: x[1][-1], reverse=True)
# for i in data:
#     print(i[1] + ': ' + str(i[0]))
# print(data)
# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# print(*map(lambda x: x // 2 if x % 2 == 0 else x, filter(lambda x: not (x % 2 == 1 and x > 47), numbers)))

# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
#
# res = sorted(filter(lambda x: len(x) == 6, ))
# print(*res)

# is_num = lambda x: True if x[0] in '-1234567890' and x.count('.') < 2 and x.upper() == x.lower() and '-' not in x[1:] else False

# func = lambda x: True if x[0].lower() == 'a' and  x[-1].lower() == 'a' else False
# print(func('Awgw'))

# func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False
# print(func(38))

# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
# res = reduce(lambda x, y: x + y + ', ', sorted(map(lambda x: x[0], filter(lambda p: p[2] == 'primary' and p[1] >= 10000000, data))), 'Cities: ')
# print(res[:-2])

# res = list(filter(lambda p: p[2] == 'primary', data))
# res = sorted(res, key=lambda x: x[0])
# print(res)
# print(res[0][0])
# re = reduce(lambda x, y: x + y[0] + ', ', res, 'City: ')
# print(re)
# def fu(data):
#         print(reduce(lambda x, y: x + y + ', ', sorted(map(lambda x: x[0], filter(lambda p: p[2] == 'primary', data))),
#                      'City: ')[:-2])
# fu(data)
# res = reduce(lambda x, y: x + y + ', ', sorted(map(lambda x: x[0], filter(lambda p: p[2] == 'primary', data))), 'City: ')
# print(res[:-2])
# print(reduce(lambda x, y: x + y + ', ', sorted(map(lambda x: x[0], filter(lambda p: p[2] == 'primary', data))), 'Cities: ')[:-2])
# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num**2,1), floats))
# filter_result = list(filter(lambda name: len(name) > 4 and name == name[::-1], words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


# def func_apply(fun, lst):
#     res = []
#     for i in lst:
#         res.append(fun(i))
#     return res
#

# from functools import reduce
#
#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
#
# def fu(n):
#     if (9 < n < 100 or -9 > n > -100) and n % 7 == 0:
#         return True
# def qwad(n):
#     return n**2
# print(sum(map(qwad, filter(fu, numbers))))


# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
# def su(a, b):
#     return a + b**2
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# print(reduce(su, numbers, 0))
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#

#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# def di(n):
#     if 99 < n < 1000 and n % 5 == 2:
#         return True
#     else:
#         return False
#
# def fu(n):
#     return n**3
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
# lst = map(fu, filter(di, numbers))

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
# def r(num):
#     return round(num, 2)
# numbers = map(r, numbers)
#
# for i in numbers:
#     print(i)

#
# lst =[int(i) for i in input().split()]
#
# def fu(n):
#     s = 0
#     ls = list(str(n))
#     for i in ls:
#         s += int(i)
#     return s, n
#
# lst = sorted(lst, key=fu)
#
# print(lst)
# # import math
#
#
# n = int(input())
# f = input()
# def f1(n):
#     return n**2
# def f2(n):
#     return n**3
# def f3(n):
#     return n**0.5
# def f4(n):
#     return abs(n)
# def f5(n):
#     return math.sin(n)
# #d = {}
# d = {'квадрат': f1  ,'куб': f2, 'корень': f3, 'модуль':  f4, 'синус': f5 }
# print(d[f](n))

# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
# def fun(n):
#     return n[m-1]
# m = int(input())
# athletes = sorted(athletes, key=fun)
# for i in athletes:
#     print(*i)
# print(*athletes, sep="\n")

# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
# def fun(n):
#     return  min(n) + max(n)
#
# numbers = sorted(numbers, key=fun)
#
# print(numbers)


# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# def fun(n):
#     return  (n[0]**2 + n[1]**2)**0.5
# points = sorted(points, key=fun)
#
# print(points)

# import numpy as np
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
#
# def av(n):
#     return sum(n)/ len(n)
# print(min(numbers, key=av))
# print(max(numbers, key=av))
# def avr(lst = []):
#     f = sum(
#     print(min(numbers, key=sum/len))
#     print(max(numbers, key=NumPy))


# def info_kwargs(**kwargs):
#     res = sorted(kwargs.items())
#     for i in res:
#         print(str(i[0]) + ": " + str(i[1]))
# 
# 
# 
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

# def print_products(*args):
#     lst = [i for i in args if type(i) is str and i != ""]
#     print(lst)
#     if len(lst) == 0:
#         print("Нет продуктов")
#     else:
#         for i in range(len(lst)):
#             print(str(i+1) + ") " + lst[i])
# print_products([4], {}, 1, 2, {'Beegeek'}, '')

# def greet(name, *args):
#     lst = list(args)
#     s = "Hello," + name
#     for i in range(0, len(lst)):
#         s = s + " and " + lst[i]
#     s += "!"
#     return s
# print(greet('Timur'))
# print(s, end=" ")
# s2 = *args, sep=" and ", end="!"
# print(*args, sep=" and ", end="!")
# print(*lst, sep=" and ", end="!")
# for i in lst:
#     print(*(lst), sep=" and ")
#     s = s + i + " and "
#     print(s)
# s += "!"
# print(s)
# greet('Timur', 'Roman', 'Ruslan')

# def mean(*args):
#     lst = list(args)
#     lst2 = [i for i in lst if type(i) is int or type(i) is float]
#     if len(lst2) == 0:
#         return 0.0
#     else:
#         res = sum(lst2) / len(lst2)
#         return res
# mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# lst2 = [i for i in lst if i is int or i is float]

# def sq_sum(*args):
#     lst = list(args)
#     su = 0
#     for i in lst:
#         su += i**2
#     return

# def count_args(*args):
#
#     print(len(args))
#     print(args)
# count_args(1, True)

# def matrix(n=1, m=None, value=0):
#     matr = []
#     if m is None:
#         m = n
#     for i in range(n):
#         matr2 = []
#         for j in range(m):
#             matr2.append(value)
#         matr.append(matr2)
#     return matr
#
# matrix(3, 4, 9)
#


# import turtle
#
# def rhombus():
#     for i in range(1, 5):
#         turtle.forward(100)
#         turtle.right(120 - 60 * (i % 2))
#
# for j in range(10):
#     turtle.right(36)
#     rhombus()
#
# turtle.done()

# for i in [120, 60, 120, 60]:
#   turtle.forward(100)
#   turtle.left(i)
# def hexagon(side):
#     t.shape('turtle')
#     for _ in range(6):
#         t.forward(side)
#         t.left(60)
#     t.forward(side)
#     t.right(60)
#
#
# for _ in range(6):
#     hexagon(50)
# t.exitonclick()
# import turtle
#
# def square(side):
#     for _ in range(4):
#         turtle.forward(side)
#         turtle.left(90)
#

# for _ in range(8):
#     turtle.left(45)
#     square(120)

# turtle.showturtle()
# turtle.forward(100)
# turtle.exitonclick()

# def rectangle(width, height):
#     turtle.forward(width)
#     turtle.right(90)
#     turtle.forward(height)
#     turtle.right(90)
#     turtle.forward(width)
#     turtle.right(90)
#     turtle.forward(height)
#
# rectangle(100, 50)

# import cmath
#
# n = int(input())
# z1 = complex(input())
# z2 = complex(input())
#
# print(z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n + 1))

# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
#
# s = {}
# for i in numbers:
#     s[abs(i)] = i
#
# #print(s)
# s = sorted(s.items())
# #print(s)
# print(s[-1][1])
# print(s[-1][0])


# z1 = complex(input())
# z2 = complex(input())
# print(f"{z1} + {z2} = {z1 + z2}")
# print(f"{z1} - {z2} = {z1 - z2}")
# print(f"{z1} * {z2} = {z1 * z2}")


# from fractions import Fraction
# from math import gcd
#
# n = int(input())
# lst = []
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if Fraction(j, i) < 1 and gcd(i, j) == 1:
#             lst.append(Fraction(j, i))
# lst = sorted(lst)
# for i in lst:
#     print(i)


# n = int(input())
# lst = []
# for i in range(n):
#     for j in range(n):
#         if i > j and i + j == n and gcd(i, j) == 1:
#             lst.append(Fraction(j, i))
# lst = sorted(lst)
# print(lst[-1])
# for i in range(len(lst)):

# from math import *
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     num = Fraction(1, factorial(i))
#     s += num
# print(s)
# a = input()
# b = input()
# n = Fraction(a)
# m = Fraction(b)
# print(f"{a} + {b} = {n + m}")
# print(f"{a} - {b} = {n - m}")
# print(f"{a} * {b} = {n * m}")
# print(f"{a} / {b} = {n / m}")


# m, n = int(input()), int(input())
# print(Fraction(m, n))

# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
#
# lst = [float(i) for i in s.split()]
# num = min(lst) + max(lst)
# print(Fraction(str(num)))
# lst = sorted(lst)
# print(lst)
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
#
# for i in numbers:
#     print(i + ' = ' + str(Fraction(i)))


# from decimal import *
#
# d = Decimal(input())
#
# print(d.exp() + d.ln() + d.log10() + d.sqrt())

# num = Decimal('-0.8853782')
# num2 = int(num)
# print(num2)
# print(num)
# num = num.as_tuple()
# print(num)
# print(type(num))
# print(type(num[1]))
# print(num[1])
# print(sorted(num[1]))
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
# lst = [Decimal(i) for i in s.split()]
# lst = sorted(lst, reverse=True)
# print(sum(lst))
# print(*lst[0:5])

# s = '1.34 3.45 1.00 0.03 9.25'
#
# numbers = [Decimal(i) for i in s.split()]
#
# maximum = max(numbers)
# minimum = min(numbers)
#
# numbers.sort()
#
# print(maximum)
# print(minimum)
# print(numbers)
# print(numbers[0] + numbers[1])


# import random
#
# n = 10**6
# k = 0
# s0 = 4
# for i in range(n):
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#     if x**2 + y**2 <= 1:
#         k += 1
# print(k / n * s0)
# print(sq)
# print(sq * s0)
# sq - p * 1 = 0

# import string

# def generate_password(length):
#     letter = ''.join((set(string.ascii_letters) | set(string.digits)) - set('lI1oO0'))
#     p = ''
#     dig = random.choice(''.join(set(string.digits) - set('lI1oO0')))
#     small = random.choice(''.join(set(string.ascii_lowercase) - set('lI1oO0')))
#     big = random.choice(''.join(set(string.ascii_uppercase) - set('lI1oO0')))
#     p = p + big + dig + small
#     for j in range(length-3):
#         p = p + random.choice(letter)
#     random.shuffle(list(p))
#     pas = ''.join(p)
#     print(pas)
#
# def generate_passwords(count, length):
#     letter = ''.join((set(string.ascii_letters) | set(string.digits)) - set('lI1oO0'))
#     for _ in range(count):
#         p = ''
#         dig = random.choice(''.join(set(string.digits) - set('lI1oO0')))
#         small = random.choice(''.join(set(string.ascii_lowercase) - set('lI1oO0')))
#         big = random.choice(''.join(set(string.ascii_uppercase) - set('lI1oO0')))
#         p = p + big + dig + small
#         for j in range(length-3):
#             p = p + random.choice(letter)
#         random.shuffle(list(p))
#         pas = ''.join(p)
#         print(pas)
#
# count, length = int(input()), int(input())
#
#
#
# count, length = int(input()), int(input())
# letter = ''.join((set(string.ascii_letters) | set(string.digits)) - set('lI1oO0'))
# for _ in range(count):
#     p = ''
#     for j in range(length):
#         p = p + random.choice(letter)
#     print(p)

#
# n = int(input())
# lst = []
# for _ in range(n):
#     lst.append(input())
# random.shuffle(lst)
# lst2 = lst.copy()
# lst3 = []
# s = set()
# s2 = set()
# while len(lst3) < len(lst):
#     friend = random.choice(lst)
#     tfriend = random.choice(lst2)
#     if friend not in s and tfriend not in s2 and friend != tfriend:
#         union = friend + " - " + tfriend
#         lst3.append(union)
#         s.add(friend)
#         s2.add(tfriend)
#         print(union)
# print(lst3)

# lst = []
# matrix = []
# for i in range(1, 76):
#     lst.append(i)
# random.shuffle(lst)
# k = 0
# for i in range(5):
#     raw = []
#     for j in range(5):
#         raw.append(lst[k])
#         k += 1
#     matrix.append(raw)
# matrix[2][2] = 0
# for i in range(5):
#     for j in range(5):
#         print(str(matrix[i][j]).ljust(3), end='')
#     print()


# print(lst)
# word = input()
# w = list(word)
# random.shuffle(w)
# nw = "".join(w)
# print(nw)
# lst = []
# while len(lst) <= 100:
#     num = random.randint(1000000, 9999999)
#     if num not in lst:
#         lst.append(num)
#
# for i in range(100):
#     print(lst[i])

# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# matrix2 = [len(matrix)][len(matrix)]
# print(matrix[0])
# for i in range(len(matrix)):
#     for j in random(len(matrix)):
#         random.shuffle(matrix[i])
# print(matrix)
# def generate_index():
#     l1 = chr(random.randint(65, 90))
#     l2 = chr(random.randint(65, 90))
#     num = random.randint(0, 99)
#     num2 = random.randint(0, 99)
#     l3 = chr(random.randint(65, 90))
#     l4 = chr(random.randint(65, 90))
#     #return l1 + l2 + num + '_' + num2 + l4 + l3
#     print(l1 + l2 + str(num) + '_' + str(num2) + l4 + l3)
# generate_index()
# def generate_ip():
#     ip = ""
#     lst = []
#     for i in range(4):
#         num = random.randint(0,255)
#         lst.append(str(num))
#         print(lst)
#     # ".".join(lst)
#     print(".".join(lst))
# generate_ip()

# lst = []
# for i in range(7):
#     lst.append(random.randint(1, 49))
# print(*sorted(lst))
# length = int(input())  # длина пароля
# for i in range(length):
#     n = random.randint(0, 2)
#     if n == 0:
#         print(chr(random.randint(65, 90)), end="")
#     else:
#         print(chr(random.randint(97, 122)), end="")


# s = {'write': 'W', 'read': 'R','execute': 'X'}
# n = int(input())
# lst = []
# di = {}
# for i in range(n):
#     lst = input().split()
#     di[lst[0]] = []
#     for j in range(1, len(lst)):
#         di[lst[0]].append(lst[j])
# print(di)
# m = int(input())
# for i in range(m):
#     ls = input().split();
#     for key, val in di.items():
#         if key == ls[1]:
#             if s[ls[0]] in val:
#                 print("OK")
#             else:
#                 print("Access denied")


# lst.append(input().split())
# m = int(input())
# for i in range(m):
#     ls = []
#     ls.append(input().split())
# for i in ls:
#     for key, val in s.items():
#         if ls[0] == key:


# n = int(input())
# d = {}
# n = 5
# b = ["b d 3", "a e 2", "r a 6", "b a 3", "b w 3"]
# for i in range(n):
#     s = b[i].split()
# #    s = input().split()
#     if s[0] not in  d.keys():
#         d[s[0]] = {s[1]: int(s[2])}
#     else:
#         if s[1] not in d[s[0]].keys():
#             d[s[0]][s[1]] = int(s[2])
#         else:
#             d[s[0]][s[1]] += int(s[2])
# di = dict(sorted(d.items()))
# # for i in di:
# #     i = sorted(i.items())
# print(di)
# print(type(di))
# for key, val in di.items():
#     print(key + ":")
#     f = dict(sorted(d[key].items()))
#     for key, val in f.items():
#         print(key, val)
# print(*f.items(), end="\n")


# def merge(values):      # values - это список словарей
#     d = {}
#     for di in values:
#         for key, val in di.items():
#             if key not in d.keys():
#                 d[key] = set()
#                 d[key].add(val)
#             else:
#                 d[key].add(val)
#     return d
#
# print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))

# def build_query_string(params):
#     #params = {}
#     s = ""
#     lst2 = []
#     for key, val in params.items():
#         # lst = []
#         # lst.append(str(key))
#         # lst.append(str(val))
#         # l = "=".join(lst)
#         # lst2.append(l)
#         lst2.append(str(key) + "=" + str(val))
#     lst = sorted(lst2)
#     s = "&".join(lst)
#     return s
#
# print(build_query_string({'name': 'timur', 'age': 28}))


# d = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
# word = input()
# s = 0;
# for i in word:
#     for key, val in d.items():
#         if i in val:
#             s += key
# print(s)

# s = input().split()
# di = {}
# for i in s:
#     if i not in di.keys():
#         di[i] = 1
#     else:
#         di[i] += 1
#     print(di[i])

# s = {"G": "C", "C": "G", "T": "A", "A": "U"}
# dnk = input()
# rnk = ""
# for i in dnk:
#     rnk += s[i]
# print(rnk)

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# lst = []
# for key, val in emails.items():
#     for i in val:
#         lst.append(i + "@" + key)
# print(*sorted(lst), sep='\n')

# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
#
# my_dict = {key: [i for i in val if i < 21] for key, val in my_dict.items()}
# print(my_dict)
# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

# result = [student_ids[i]: dict(zip(student_names[i], student_grades[i]) for i in range(len(student_grades))]
# result = [dict(zip(student_ids, dict(zip(student_names, student_grades))))]

# res = dict(zip(student_names, student_grades))
# result = dict(zip(student_ids, res))
# result = [{id:{name: grade}} for id, name, grade in zip(student_ids, student_names, student_grades)]

# result = [{student_ids[i]: dict([student_names[i], student_grades[i]])} for i in range(len(student_names))]
# print(result)

# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {tuples[i][0]: (tuples[i][1], tuples[i][2]) for i in range(len(tuples))}

# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {key: val for key, val in students.items() if val[0] > 167 and val[1] < 75}

# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# result = {key: val for key, val in letters.items() if key not in remove_keys}

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {words[i]: [ord(j) for j in words[i]] for i in range(len(words))}
# numbers = [1, 6, 18, 17]
# #result = {}
#
# result = {numbers[i]: [j for j in range(1, numbers[i] + 1) if numbers[i] % j == 0] for i in range(len(numbers))}

# for i in range(len(numbers)):
#     lst = []
#     for j in range(1, numbers[i] + 1):
#         if numbers[i] % j == 0:
#             lst.append(j)
#             result[numbers[i]] = lst
# print(result)
# print(s.split())
# result = {int(i.[0]): i.[1] for i.split(":")  in s.split()}
# result = {int(i.split(":")[0]): i.split(":")[1] for i in s.split()}
# s = s.split()
# print(s)
# for i in range(len(s)):
#     #lst = []
#     lst = s[i].split(":")
#
#     result[lst[0]] = lst[1]
# print(result)

# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
#
# result = {val: key for key, val in months.items()}

# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
#
# result = {}
# result = {key: val for key, val in favorite_numbers.items() if 9 < val < 100}
#
# for key, val in colors.items():
#     if val != None:
#         result[key] = val


# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
#
# result = {i: numbers[i]**2 for i in range(len(numbers))}

# for i in range(len(numbers)):
#     result[i] = numbers[i]**2
