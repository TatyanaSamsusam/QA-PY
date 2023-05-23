# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

# from random import randint
# num = randint(500, 1000)
# print(f'вот полученное число: {num}')

# base = 16

# check = hex(num)
# print (f'Вот оно в шестнадцатеричной системе через hex: {check}')

# result: str = ''
# digits = '0123456789abcdef'

# while num > 0:
#     result = digits[num % base] + result
#     num = num // base

# print(f'Вот оно в шестнадцатеричной системе через цикл: {result}')

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions
import decimal
import math

init1 = input('введите дробь через / : ')
init2 = input('введите еще одну дробь через / : ')

drob1_kak_spisok = init1.split("/")

chisl_1 = int(drob1_kak_spisok[0])
znam_1 = int(drob1_kak_spisok[1])

drob2_kak_spisok = init2.split("/")

chisl_2 = int(drob2_kak_spisok[0])

znam_2 = int(drob2_kak_spisok[1])

proizv_chisl = int(chisl_1 * chisl_2/math.gcd(chisl_1 * chisl_2,znam_1 * znam_2))
proizv_znam1 = int(znam_1 * znam_2/math.gcd(chisl_1 * chisl_2,znam_1 * znam_2))

sum_chisl = int((chisl_1 * znam_2 + chisl_2 * znam_1)/math.gcd(chisl_1 * znam_2 + chisl_2 * znam_1, znam_1 * znam_2))
proizv_znam2 = int(znam_1 * znam_2/math.gcd(chisl_1 * znam_2 + chisl_2 * znam_1, znam_1 * znam_2))

print(f"результат произведения дробей: {proizv_chisl}/{proizv_znam1}")
print(f"результат сложения дробей: {sum_chisl}/{proizv_znam2}")


f1 = fractions.Fraction(3,4)
f2 = fractions.Fraction(5,6)

sum = f1 + f2
print(f'это сумма введенных дробей: {sum}')

mult = f1 * f2
print(f'это произведение введенных дробей: {mult}')