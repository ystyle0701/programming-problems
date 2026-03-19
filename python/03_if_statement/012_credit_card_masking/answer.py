card_no = input("クレジットカード番号を入力してください: ")
if len(card_no) != 16:
    print("16桁で入力してください")
else:
    digits = card_no[-4:]
    print("*" * 12 + digits)