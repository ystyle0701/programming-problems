age = int(input('年齢を入力してください：'))

if age >= 18:
    price = 1000
    print(f'大人料金です(1枚 {price}円)')
else:
    price = 500
    print(f'子ども料金です(1枚 {price}円)')

quantity = int(input('チケットの枚数を入力してください：'))
total = price * quantity

print(f'料金は{total}円です')