from unitle.language import tr


def rank(score):
    if score >= 120:

        print(tr("your rank is \n 💀 BEYOND LEGEND", "رتبه تو \n 💀فرا اسطوره "))
        print(
            tr(
                "YOU BROKE THE LIMIT! 💀🔥 \n 120+ points... that's not supposed to happen. \n The game wasn't ready for you. 😈",
                "تو سقف امتیازو شکستی💀🔥 \n آخه بیشتر از 120 امتیاز چجوری! \n یا خوش‌شانسی یا نابغه😈",
            )
        )

    elif score >= 100:

        print(tr("your rank is \n ⚡ score breaker", "رتبه تو \n ⚡ شکننده‌ی رکوردها"))
        print(
            tr(
                "YOU BROKE THROUGH 100! 🔥\n The normal scoring system wasn't enough for you. \n Keep going... you're getting dangerously good. 😏",
                "🔥از 100 رد شدی! \n امتیاز معمولی برات کافی نبود؟ \n  داری خطرناک پیش میری😏",
            )
        )

    elif score >= 90:

        print(tr("your rank is \n👑 Legend", "رتبه تو  \n👑 اسطوره هست"))
        print(tr("Were you reading my mind?", "نه قبول نیست تو داری ذهن منو می‌خونی"))

    elif score >= 75:

        print(tr("your rank is \n🥇 Master", "رتبه تو \n🥇 استاد هست"))
        print(tr("That was impressive!", "عالی بود! خیلی خوب رفتی"))

    elif score >= 60:

        print(tr("your rank is \n🥈 Pro", "رتبه تو\n🥈 حرفه‌ای"))
        print(tr("Not bad at all!", "بد بازی نکردی!"))

    elif score >= 40:

        print(tr("your rank is \n🥉 Beginner", "رتبه تو \n🥉 تازه‌کار"))
        print(tr("Keep practicing!", "بد نبود \n تمرین آدم رو حرفه‌ای می‌کنه!"))

    else:

        print(tr("your rank is \n🤡 Lucky Potato", "رتبه تو \n🤡سیب‌زمینی خوش‌شانس"))
        print(
            tr(
                "You found it... somehow. 😂",
                "فکر کنم اگه شانس باهات یار نبود ساعت‌ها روش فکر می‌کردی 😂",
            )
        )


def high_score(score):
    try:
        with open("high_score.txt", "r") as f:
            high = int(f.read())
    except FileNotFoundError:
        with open("high_score.txt", "w") as f:
            f.write("0")
        high = 0

    if score > high:
        high = score
        with open("high_score.txt", "w") as f:
            f.write(str(high))

    print(tr(f"high score => {high}", f"بیشترین امتیاز ->{high}"))

    return high
