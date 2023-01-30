
# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = input('введите трехзначное число')
f = True
while f:
    if len(num) == 3:
        res = 0
        f = False
        for i in num:
            res += int(i)
        print(res)
    else:
        num = input('число не трехзначное, попробуйте еще')
