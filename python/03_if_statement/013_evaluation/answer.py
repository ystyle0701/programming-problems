score = int(input('点数を入力してください(0-100): '))
attendance = int(input('出席日数を入力してください(0-20): '))
if score >= 80 and attendance >= 18:
    result = '優秀'
elif score >= 60 and attendance >= 15:
    result = '合格'
elif score >= 60 and attendance < 15:
    result = '出席不足で不合格'
elif score < 60 and attendance >= 15:
    result = '点数不足で不合格'
else:
    result = '両方不足で不合格'

print(f'点数: {score}点, 出席日数: {attendance}日')
print(f'判定: {result}')
