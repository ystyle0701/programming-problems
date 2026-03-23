# 在庫データを辞書で作成
stock = {
    "ボールペン": 100,
    "ノート": 45,
    "消しゴム": 80,
    "ホッチキス": 25
}

# ノートを販売
num = int(input('ノートを何冊購入しますか？'))
if num > stock['ノート']:
    print('在庫がありません')
else:
    stock["ノート"] -= num

# 全ての在庫状況を表示
print("---在庫状況---")
for item, quantity in stock.items():
    print(f"{item}: {quantity}個")