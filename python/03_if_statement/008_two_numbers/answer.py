num1 = int(input('1つめの数字を入力してください：'))
num2 = int(input('2つめの数字を入力してください：'))
if num1 > num2:
    print('1つめの数字の方が大きい')
elif num1 < num2:
    print('2つめの数字の方が大きい')
else:
    print('同じ値です')