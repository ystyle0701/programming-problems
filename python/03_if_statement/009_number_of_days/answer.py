month = int(input('調べたい月を入力してください(1～12)：'))
if month == 1 or month == 3 or month == 5 or month == 7 or \
        month == 8 or month == 10 or month == 12:
    print('31日まであります')
elif month == 4 or month == 6 or month == 9 or month == 11:
    print('30日まであります')
elif month == 2:
    print('28日まであります')
else:
    print('分かりません')