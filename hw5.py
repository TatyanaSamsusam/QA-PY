from __future__ import annotations
from typing import Dict, List

# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

text = 'C:/Users/S&T/Documents/cat.jpg'
*way, name, format = text.split('/')

print(f'{way=}, {name=}, {format=}')


# # Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# # имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# # В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# # Сумма рассчитывается как ставка умноженная на процент премии

def my_gen (names:List[str], salary: List[int], bonus: List [str]) -> dict[str:int]:
    return {names[i]: salary[i] + salary[i] * (float(bonus[i].replace('%', '')) / 100) for i in range (len(names))}

print(my_gen(['Ivanov', 'Petrov', 'Sidorov'], [12000, 11000, 11500], ['10.5%', '10.25%', '10.75%']))    

# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def gener_fibo(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(gener_fibo(12)))  