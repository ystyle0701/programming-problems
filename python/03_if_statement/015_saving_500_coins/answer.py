target = int(input('目標金額を入力してください: '))
if target < 0:
    print('正の金額を入力してください')
elif target == 0:
    print('0円なので硬貨は必要ありません')
elif target % 500 == 0:
    num = target // 500
    print(f'500円硬貨は{num}枚必要です')
else:
    print('500円硬貨以外が必要です')