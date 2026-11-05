import re
from functools import reduce

#
# price = input('Введите сумму: ').strip(' ')
# pattern = r'^\d+\s*ру?б?\s*(?:\d{1,2}\s*ко?п?)?\.?$'
#
# if bool(re.match(pattern, price)):
#     price_list = re.findall(r'\d+', price)
#     if len(price_list) == 2:
#         edited_price = [int(price_list[0]), int(price_list[1])]
#         print(f'{edited_price[0]}.{edited_price[1]:02d} {chr(8381)}')
#     else:
#         edited_price = [int(price_list[0])]
#         print(f'{edited_price[0]} {chr(8381)}')
#


expenses = []

def add_expenses(expenses_list, value):
    pattern = (
        r'^\d+\s*'
        r'(?:рублей|рубля|рубль|руб\.?|р\.?)'
        r'(?:\s+\d{1,2}\s*(?:копеек|копейки|копейка|коп\.?|к\.?))?$'
    )
    if re.match(pattern, value):
        tmp_expenses = re.findall(r'\d+', value)
        if len(tmp_expenses) == 2:
            expenses_list.append(f'{int(tmp_expenses[0])}.{int(tmp_expenses[1]):02d} {chr(8381)}')
        else:
            expenses_list.append(f'{tmp_expenses[0]}.00 {chr(8381)}')


def print_report(expenses_list):
    for index, exp in enumerate(expenses_list):
        print(f'{index + 1}. {exp}')

def get_total_sum(expenses_list):
    tmp_expenses_list = map(create_floats_val, expenses_list)
    total_sum = reduce(lambda x, y: x + y, tmp_expenses_list)
    return total_sum

def create_floats_val(expenses_val):
    return float(expenses_val.split(' ')[0])

def average_expense(expenses_list):
    return get_total_sum(expenses_list) / len(expenses_list)

def del_expense(expenses_list):
    print_report(expenses_list)
    try:
        del_index = int(input('Какой расход удалить? '))
        print(f'Расход на {expenses_list.pop(del_index - 1)} удален')
    except IndexError:
        print('Нет такого элемента в списке')
    except ValueError:
        print('Некорректный ввод! Введите правильное значение')


while True:
    print('''
======================Меню=============================
    add - Добавить расход
    print_report - Показать все расходы
    total - Показать сумму
    avg - средний расход
    del - удалить расход по номеру
    exit - выход
=======================================================
    ''')

    user_choice = input('Введите команду: ').lower().strip(' ')

    match user_choice:
        case 'add':
            print('Добавить расход')
            expense = input('Введите сумму расхода: ').strip(' ').lower()
            add_expenses(expenses, expense)
            # print(f'Добавлен расход на {expenses[-1]}')

        case 'print_report':
            print('Показать все расходы')
            print_report(expenses)
            pass
        case 'total':
            print('Показать сумму')
            if len(expenses) == 0:
                print('Расходы равны 0!')
                continue
            else:
                print(f'Общая сумма расходов: {get_total_sum(expenses):.2f} {chr(8381)}')
        case 'avg':
            print('Показать средний расход')
            if len(expenses) == 0:
                print('Расходы равны 0!')
                continue
            else:
                print(f'Средний расход: {average_expense(expenses):.2f} {chr(8381)}')
        case 'del':
            print('Удалить расход')
            del_expense(expenses)
        case 'exit':
            print('Выход')
            break
        case _:
            print(f'Неизвестная команда. Поробуйте снова')

