text = "banana and apple"

count = 0

for i in range(len(text)):
    if text[i] == "a" or text[i] == "i" or text[i] == "u" or text[i] == "e" or text[i] == "o":
        count += 1

print(f"母音の数は{count}個です")