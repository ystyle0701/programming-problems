hour = int(input('時間を入力してください:'))

if 6 <= hour <= 11:
    greeting = 'おはよう'
elif 12 <= hour <= 17:
    greeting = 'こんにちは'
elif 18 <= hour <= 21:
    greeting = 'こんばんは'
else:
    greeting = 'お疲れ様'

print(f'{hour}時: {greeting}')