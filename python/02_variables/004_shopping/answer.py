name = 'たろう'
money = 1000
print(name, 'さんの所持金', money, '円')

price = 100
item = 'チョコレート'
print(name, 'さんは', item, 'を買いました(金額',price,'円)')

money = money - price
print(name, 'さんの所持金', money, '円')

print('残金で',item, 'を', money // price, '個買えます')