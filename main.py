import re

price = input('Введите сумму: ').strip(' ')
pattern = r'^\d+\s*ру?б?\s*(?:\d+\s*ко?п?)?\.?$'

if bool(re.match(pattern, price)):
    price_list = re.findall(r'\d+', price)
    if len(price_list) == 2:
        edited_price = [int(price_list[0]), int(price_list[1])]
        print(f'{edited_price[0]}.{edited_price[1]:02d} {chr(8381)}')
    else:
        edited_price = [int(price_list[0])]
        print(f'{edited_price[0]} {chr(8381)}')
else:
    print('Некорректный ввод суммы')


