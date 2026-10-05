from unitle.language import tr
from unitle.helpers import get_number
from unitle.helpers import is_prime


def help_(com, score):

    print("=" * 40)
    print(tr("🎁 Hint Menu", "🎁 منوی کمک"))
    print(tr("1. Even / Odd                 (-5)", "1.  زوج / فرد              (-5)"))
    print(
        tr(" 2. Divisible by 5             (-5)", "2. بخش‌پذیری بر 5            (-5)")
    )
    print(
        tr(
            "3. Prime?                     (-15)",
            "3. عدد اول؟                     (-15)",
        )
    )
    print(tr("4. Last Digit                 (-20)", "4. رقم آخر                (-20)"))
    print(tr("5.back to game", "5.بازگشت به بازی"))
    print("=" * 40)

    res = get_number(1, 5)
    if res == 1:
        if score < 5:
            print(tr("your score is low", "امتیاز شما کم است"))
            return score, False
        else:
            score -= 5
            if com % 2 == 0:

                print(tr("my number is even", "عدد من زوجه"))

            else:

                print(tr("my numbeuer is odd", "عدد من فرده"))

            return score, True
    elif res == 2:
        if score < 5:
            print(tr("your score is low", "امتیاز شما کم است"))
            return score, False
        else:
            score -= 5
            if com % 5 == 0:

                print(tr("yes", "آره"))

            else:

                print(tr("no", "نه"))

            return score, True
    elif res == 3:
        if score < 15:
            print(tr("your score is low", "امتیاز شما کم است"))
            return score, False
        else:
            score -= 15

            b = is_prime(com)
            if b == True:

                print(tr("yes", "آره"))

            else:

                print(tr("no", "نه"))

            return score, True
    elif res == 4:
        if score < 20:
            print(tr("your score is low", "امتیاز شما کم است"))
            return score, False
        else:

            score -= 20
            d = com % 10
            print(d)
            return score, True
    elif res == 5:

        return score, False
