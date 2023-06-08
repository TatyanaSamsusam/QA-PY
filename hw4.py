# Напишите функцию для транспонирования матрицы

from __future__ import annotations

# def transp (matr1: list[int]):
#     trans_matr = [[0 for j in range (len(matr1))] for i in range(len(matr1[0]))]
#     for i in range (len(matr1)):
#         for j in range (len(matr1[0])):
#             trans_matr[j][i] = matr1[i][j]
#     return trans_matr

# print(transp([[1,2,3], [4,5,6], [7,8,9]]))

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, 
# а значение - имя аргумента. Если ключ не хешируем, используйте его строковое представление.

# def fun1 (** kwargs):
#     final_dict = dict(zip(kwargs.values(), kwargs.keys()))
#     return final_dict

# print(fun1(Испания='Мадрид', Великобритания='Лондон', Франция='Париж'))

# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

class Bank:

    _BALANCE = 0
    _MIN = 50
    _COMISSION = 0.015
    _BONUS = 0.03
    _TAX = 0.10
    _OPERATION_COUNT = 0

    def __init__(self):
        self._OPERATION_COUNT = 0

    def _in(self, cash: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0:
            self._BALANCE += cash
            self._OPERATION_COUNT +=1
            return self._BALANCE, self._OPERATION_COUNT
        else: 
            return 'не кратно 50'

    def _out(self, cash: int, comission: int) -> tuple[int, int] | None:
        if cash % self._MIN == 0 and self._BALANCE > 0 and self._BALANCE - (cash + comission) >= 0:
            self._BALANCE -= cash
            self._OPERATION_COUNT +=1
            return self._BALANCE, self._OPERATION_COUNT
        else: 
            return None

    def _check_comission (self, cash: int) -> int:
        sum_comission = cash * self._COMISSION

        _MAX = 600
        _MIN = 30

        if sum_comission > _MAX:
            return _MAX
        elif sum_comission < _MIN:
            return _MIN
        else:
            return sum_comission

    def _check_oper_count(self):
        state = self._OPERATION_COUNT
        if state % 3 == 0:
            return True
        else: 
            return False

    def _exit(self):
        return 'Good bye!'
        
    def start(self, mode: str, cash: int = 0) -> str:

        check_operation = self._check_oper_count()
        if True:
            self._BALANCE += self._BALANCE * self._BONUS 

        if mode == 'in':
            
            data = self._in(cash=cash)
            com_data = self._check_comission(cash=cash)
            return f'средства зачислены. сумма: {cash}, комиссия: {com_data}, баланс: {self._BALANCE}'

        if mode == 'out':
            com_data = self._check_comission(cash=cash)
            data = self._out(cash=cash, comission=com_data)
            if data:
                return (f'Операция успешна. сумма: {cash}, комиссия: {com_data}, баланс: {self._BALANCE}')
            else: 
                return 'Не хватает средств'

        if mode == 'exit':
            return self._exit()

client = Bank()
print(client.start(mode='out', cash=10000))


            
        

