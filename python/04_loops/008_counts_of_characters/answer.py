text = "banana"

count = 0

for i in range(len(text)):
    if text[i] == "a":
        count += 1

print(f"aの数は{count}個です")


# 便利な書き方
counts = text.count("a")
print(f"aの数は{counts}個です")
