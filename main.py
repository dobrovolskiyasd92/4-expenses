price = input("Введите сумму в формате X руб (Y коп): ")

tmp_price = price.lower().replace(' ', '').replace('.', '')


if not 'руб' in tmp_price:
    print('Некорректный формат суммы')
    exit()

tmp_price = tmp_price.rstrip('коп').rstrip('к').split('руб')

if len(tmp_price[1]) > 2:
    print('Некорректный формат суммы')
    exit()

edited_price = [int(tmp_price[0]), int(tmp_price[1])]
print(f'{edited_price[0]}.{edited_price[1]:02d} {chr(8381)}')