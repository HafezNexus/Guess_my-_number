from unitle.language import tr


def difficulty():

    print(40 * "=")
    print(20 * "=")
    print(tr("🎮 Choose your difficulty:", "🎮 سطح بازی رو انتخاب کن:"))
    print(
        tr(
            " 🟢 Easy \n Numbers: 1 - 20 \n 😊 Just warming up... even your grandma could win. ",
            " 🟢 راحت \n اعداد : 1 - 20 \n 😊 این فقط برای شروعه... حتی مادربزرگت هم می‌تونه پیداش کنه ",
        )
    )
    print(
        tr(
            "🟡 Medium \n Numbers: 1 - 100 \n 😏 Now we're talking. Don't celebrate too early!",
            "🟡 متوسط \n اعداد: 1 - 100 \n 😏 حالا باید ببینیم چند مرده حلاجی",
        )
    )
    print(
        tr(
            "🔴 Impossible \n Numbers: 1 - 1000 \n 💀 Good luck... you'll probably need it.",
            "🔴 غیر ممکن \n اعداد: 1 - 1000 \n 💀 برات آرزوی موفقیت میکنم... باید خیلی خوش شانس باشی.",
        )
    )
    print(
        tr(
            "⚙️ Custom \n Choose your own range. \n 🤔 Make the game as easy... or as impossible as you want!",
            "⚙️ دلخواه \n خودت محدوده رو بساز. \n 🤔 بازی خودتو بساز... از راحت تا غیر ممکن \n کدومو ترجیح میدی",
        )
    )

    print(40 * "=")
    print(20 * "=")

    while True:
        try:

            res = int(
                input(
                    tr(
                        "😈 Pick your challenge! \n Type a number from 1 to 4: \n 1️⃣ Easy \n 2️⃣ Medium 😎 \n 3️⃣ Impossible 💀 \n 4️⃣ Custom ⚙️ \n 5.back to main menu \n :",
                        "😈 حالا وقتشه خودتو امتحان کنی! \n از 1 تا 4 عدد مورد نظرت رو وارد کن: \n 1️⃣ راحت \n 2️⃣ متوسط 😎 \n 3️⃣ غیر ممکن 💀 \n 4️⃣ دلخواه ⚙️ \n 5.برگشت به منو\n :",
                    )
                )
            )

            if res == 1:
                return 1, 20

            elif res == 2:
                return 1, 100

            elif res == 3:
                return 1, 1000
            elif res == 4:
                while True:

                    try:
                        print(40 * "=")
                        print(15 * "=")
                        print(tr("🎯 Build your own challenge!", "🎯 چالش خودتو بساز!"))
                        start = int(input(tr("start: ", "آغاز از: ")))
                        end = int(input(tr("end: ", "پایان: ")))

                        if start >= end:
                            print(tr("start < end", "شروع < پایان"))
                            continue
                        print(
                            tr(
                                "🤖 I've hidden my number...Good luck finding it!",
                                "🤖 من عددم رو قایم کردم...در پیدا کردنش خوش شانس باشی!",
                            )
                        )
                    except ValueError:
                        print(tr("please enter just number!", "لطفا فقط عدد وارد کن"))
                        continue
                    return start, end

            elif res == 5:
                return "menu"
            else:

                print(
                    tr(
                        "please say number between 1 and 5",
                        "لطفا فقط اعدادی از 1 تا 5 بگو",
                    )
                )

        except ValueError:

            print(tr("please enter just number!", "لطفا فقط عدد وارد کنید!"))

        print(40 * "=")
        print(20 * "=")
