# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no


n = int(input('кол-во столбцов'))
m = int(input('кол-во строк'))
piece = int(input('размер куска'))
if piece %  n == 0 or piece % m == 0:
    print('YES')
else:
    print('NO')