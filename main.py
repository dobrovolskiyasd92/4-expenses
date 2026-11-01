# import re
#
# price = input('Введите сумму: ').strip(' ').lower()
# # pattern = r'^\d+\s*ру?б?/\s*(?:\d{1,2}\s*ко?п?)?\.?$'
# pattern = r'^\d+\s*(?:руб|рубль|рубля|рублей)(?:\s+\d{1,2}\s*(?:коп|копейка|копейки|копеек)\.?)?$'
# if bool(re.match(pattern, price)):
#     price_list = re.findall(r'\d+', price)
#     if len(price_list) == 2:
#         edited_price = [int(price_list[0]), int(price_list[1])]
#         print(f'{edited_price[0]}.{edited_price[1]:02d} {chr(8381)}')
#     else:
#         edited_price = [int(price_list[0])]
#         print(f'{edited_price[0]}.00 {chr(8381)}')
# else:
#     print('Некорректный формат суммы')
#
#

while True:
    user_choice = input('Введите команду: ')

    match user_choice:
        case 'add':
            print('Добавить расход')
            pass
        case 'show_all':
            print('Показать все расходы')
            pass
        case 'show_sum_avg':
            print('Показать сумму и средний расход')
            pass
        case 'del':
            print('Удалить расход')
            pass
        case 'exit':
            print('Выход')
            break
        case _:
            print(f'Неизвестная команда. Поробуйте снова')

