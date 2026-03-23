animal_lists = [ "パンダ", "ゴリラ", "ペンギン", "ペンギン", "パンダ", "パンダ", "キリン", "パンダ", "ペンギン"]

results = {}
for animal in animal_lists:
    if animal in results:
        results[animal] += 1
    else:
        results[animal] = 1

print('---投票結果---')
for key, value in results.items():
    print(f'{key}:{value}票')
