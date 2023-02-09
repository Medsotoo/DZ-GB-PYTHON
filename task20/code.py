# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12


dict1 = {1 : ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R','А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 2 : ['D', 'G','Д', 'К', 'Л', 'М', 'П', 'У'], 3 : ['Б', 'Г', 'Ё', 'Ь', 'Я','B', 'C', 'M', 'P'], 4 : ['Й', 'Ы','F', 'H', 'V', 'W', 'Y'], 5 : ['Ж', 'З', 'Х', 'Ц', 'Ч','K'], 8 : ['Ш', 'Э', 'Ю' ,'J', 'X'], 10 : ['Ф', 'Щ', 'Ъ','Q','Z']}
t = {('A', 'E', 'I', 'O', 'U', 'L', 'N') : 1 ,('S', 'T', 'R','А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т') : 3}
res = 0
text = input()
for i in text.upper():
    for k,v in dict1.items():
         if i in v:
            res += k
print(res)

