member = input('アプリ会員ですか？(y:はい/n:いいえ)')
if member == 'n':
    print('割引はありません')
elif member == 'y':
    age = int(input('年齢を入力してください: '))
    if age < 0 or age > 120:
        print('正しい年齢を入力してください')
    elif age >= 60:
        print('5%割引です')
    else:
        print('3%割引です')
else:
    print('入力に誤りがあります')