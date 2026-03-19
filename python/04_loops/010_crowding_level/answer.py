for hour in range(6, 24):

    if 7 <= hour <= 9:
        status = "通勤ラッシュ"
    elif 17 <= hour <= 19:
        status = "帰宅ラッシュ"
    else:
        status = "通常運行"

    if hour == 8 or hour == 18:
        status += "★超混雑★"

    print(f"{hour}時: {status}")