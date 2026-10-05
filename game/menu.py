from unitle.language import tr
from unitle.helpers import get_number
from .core import game


def quit_():

    ans = input(tr("are you sure?(Y/N)?", "مطمئنی?(Y/N)?"))

    if ans.upper() == "Y":

        print(
            tr(
                "😏 Fine... \n You escaped this time. \n But I'll be waiting.",
                "😏خوشحالم از اینکه بازی کردی \n من منتظرت میمونم.",
            )
        )

        return False

    elif ans.upper() == "N":
        return True


def menu():
    while True:

        print(40 * "=")
        print(tr("🎮 menu", "🎮 منو"))
        print(tr("1.play", "1.بازی"))
        print(tr("2.how to play?", "2.راهنما?"))
        print(tr("3.quit", "3.خروج"))
        print(tr("4.new game", "4.بازی جدید"))
        print(40 * "=")

        entekhab = get_number(1, 4)

        if entekhab == 1:
            game()
        elif entekhab == 2:

            print(40 * "=")
            print(
                tr(
                    "Welcome! 🎉 \n Get ready to put your luck and your brain to the test! \n I'm thinking of a secret number, and your mission is to guess it in as few tries as possible.\n Good luck... you need it!😉",
                    "🎉 خوش اومدی! \n آماده‌ای شانس و هوشت رو به چالش بکشی؟ 😈 \n من یه عدد مخفی انتخاب کردم و مأموریت تو اینه که با کمترین تعداد حدس پیداش کنی..\n فکر می‌کنی از پسش برمیای...!😉",
                )
            )
            print(40 * "=")

        elif entekhab == 3:
            if quit_() == False:
                break
        elif entekhab == 4:
            new_game()


def new_game():

    while True:

        resu = input(
            tr(
                "Are you sure? Your current high score will be replaced(Y/N)",
                "آیا از این نظر مطمئنی؟بعد از این تمامی امتیازاتت حذف می‌شود(Y/N)",
            )
        )

        if resu.upper() == "Y":
            with open("high_score.txt", "w") as f:
                f.write("0")
            return ""
        elif resu.upper() == "N":
            return ""
        else:

            print(tr("please enter y or n", "لطفا فقط y و n وارد کن"))
