total = 0

while True:
    num = int(input("数字を入力してください（終了するには0）："))
    if num == 0:
        break
    total += num

print(f"合計は{total}です")