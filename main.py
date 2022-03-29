import sympy as sym
from math import pi, exp as e
from numpy import sin, cos, tan, cosh, tanh, sinh
x = sym.Symbol('x')
# f = sym.Symbol('f')
# f = (8+2*x) # определение функции
# print (type(f))
print(e)
a = input("Верхний предел: ")
b = input("Нижний предел: ")
f = input("Определение функции: ")
print(f)
print(f'функция: {f}')
result = sym.integrate(f, (x, b, a))
print(f'интеграл: {result}')
print(f'значение интеграла: {result.evalf()}')

# sin(x)/(cos(x)**2+1)