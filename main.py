price = input("Введите сумму в формате X руб (Y коп): ")

tmp_price = price.lower().replace(' ', '').replace('.', '')

if not 'руб' in tmp_price:
    print('Некорректный ввод')
    exit()

tmp_price = tmp_price.rstrip('коп').rstrip('к').split('руб')

if len(tmp_price[1]) > 2:
    print('Некорректный ввод')
    exit()

edited_price = float('.'.join(tmp_price))
print(f'{edited_price:.2f} {chr(8381)}')