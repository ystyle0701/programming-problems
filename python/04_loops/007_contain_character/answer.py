
text = "banana"

flag = False

for i in range(len(text)):
    if text[i] == "a":
        flag = True
        break

if flag:
    print("aは含まれています")
else:
    print("aは含まれていません")


# 便利な書き方
text = "banana"

if "a" in text:
    print("aは含まれています")
else:
    print("aは含まれていません")