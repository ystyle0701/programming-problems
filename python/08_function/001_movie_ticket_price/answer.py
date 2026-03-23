def ticketPrice(age, isMonday):
    if 0 <= age <= 12:
        return 500

    elif 13 <= age <= 60:
        if isMonday:
            return 1800
        else:
            return 2000

    elif 61 <= age <= 100:
        return 1500

    return -1

age = int(input('年齢を入力してください: '))
isMonday = False
monday = input('今日は月曜日ですか？(y:はい n:いいえ): ').lower()
if monday == 'y':
    isMonday = True

price = ticketPrice(age, isMonday)
if price == -1:
    print('入力値が不正です')
else:
    print(f'{price}円です')