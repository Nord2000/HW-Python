"""
Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)2
100 -> 1 (1 + 0 + 0) |
"""

q = 100
summa = 0 
while q > 0:
    x = q % 10
    summa = summa + x
    q = q // 10
print (summa) 