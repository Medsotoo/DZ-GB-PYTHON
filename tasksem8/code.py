# Обязательное ДЗ - доделать телефонный справочник с внешним хранилищем информации, дополнить функционалом добавления информации, удаления и редактирования.



import json


def creat():   
    ''' данная функция создает контакт''' 
    with open(r'C:\Users\sergey\OneDrive\Рабочий стол\DZ.GB.PYTHON\tasksem8\file.json', encoding='utf-8') as f:
        df = json.load(f)
    df.update({input('имя контакта'):{'номер': input('введите номер'), 'место работы': input('введите место работы'),'место жительства': input('введите место жительства')}})
    with open(r'C:\Users\sergey\OneDrive\Рабочий стол\DZ.GB.PYTHON\tasksem8\file.json', 'w',  encoding='utf-8') as f:
        json.dump(df, f, ensure_ascii=False, indent=3)
    return 'контакт успешно создан и записан в в файл'

def add():
    '''изменяет контакт'''
    with open(r'C:\Users\sergey\OneDrive\Рабочий стол\DZ.GB.PYTHON\tasksem8\file.json', encoding='UTF-8') as f:
        df = json.load(f)
    name = input('введите имя контакта, данные которого вы хотите изменить')
    if name in df:
        x = int(input('что хотите изменить: 1 : номер, 2 : место работы, 3 : место жительства'))
        var = {1:'номер', 2:'место работы', 3:'место жительства'}
        df[name][var[x]] = input('введите изменения')
        with open(r'C:\Users\sergey\OneDrive\Рабочий стол\DZ.GB.PYTHON\tasksem8\file.json', 'w',  encoding='UTF-8') as f:
            json.dump(df, f, ensure_ascii=False,  indent=3)
        return 'данные изменены'
    else:
        return 'такого имени нет в вашем списке'

def delit():
    '''удаляет контакт'''
    with open(r'C:\Users\sergey\OneDrive\Рабочий стол\DZ.GB.PYTHON\tasksem8\file.json', encoding='UTF-8') as f:
        df = json.load(f)
    try:
        df.pop(input('введите имя контакта который вы хотите удалить'))
        with open(r'C:\Users\sergey\OneDrive\Рабочий стол\DZ.GB.PYTHON\tasksem8\file.json', 'w',  encoding='UTF-8') as f:
            json.dump(df, f, ensure_ascii=False,  indent=3)
        return 'контакт удален'
    except KeyError:
        return 'Такого имени нет в списке ваших контактов'
    
def com():
    '''вызывает действие'''
    comand = input('1 - для создания контакта / 2 - для удаления контакта  / 3 - для редактирования / любая другая цифра - закрыть прграмму')
    while comand in '123':
        if comand == '1': print(creat())
        elif comand == '2': print(delit())
        elif comand == '3': print(add())
        comand = input('1 - для создания контакта / 2 - для удаления контакта  / 3 - для редактирования / любая другая цифра - закрыть прграмму')
    if comand not in '123': print('программа завершилась')



com()
