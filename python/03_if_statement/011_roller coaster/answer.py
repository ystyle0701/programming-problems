print('ジェットコースターご利用前の確認')
wheelchair = input('車椅子をご利用ですか？【y:はい/n:いいえ】')
if wheelchair == 'y':
    print('車椅子ご利用の方は、ご利用いただけません')
else:

    height = int(input('身長を入力してください: '))
    if height < 120:
        print('120cm未満の方は、ご利用いただけません')
    elif height >= 190:
        print('190cm以上の方は、ご利用いただけません')
    else:
        print('楽しんでください！')