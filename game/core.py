from time import monotonic
import random
from unitle.language import tr
from .scoring import rank, high_score
from .difficulty import difficulty
from .helping import help_
import math


def welcome():

    print("=" * 40)
    print(tr("🎯 Welcome to Guess My Number!", "🎯 خوش اومدی به بازی حدس عدد!"))
    print(tr("😈 Ready to lose?", "اماده ای تا ببیازی😈"))
    print(tr("I've picked a secret number.", "من عدد مخفی رو انتخاب کردم"))
    print(tr("Think you can beat my high score?", "به نظرت میتونی رکورد بزنی؟"))
    print(tr("Let's find out!", "برو و پیداش کن!"))
    print("=" * 40)


def answer(computer, user_number):
    if computer > user_number:
        res = random_joke("bigger")
    elif computer < user_number:
        res = random_joke("smaller")
    else:
        res = ""

    return res


def random_joke(direction):

    bigger = tr(
        [
            "⬆️ Aim higher, you re still too low!",
            "🚀Go up! My number is out of your reach",
            "📈 Keep climbing, you re not there yet.",
        ],
        [
            "⬆️ بالا تر برو عدد من بزرگتره!",
            "🚀 خجالت نکش بالا تر برو",
            "📈 هنوز بهم نزدیک هم نشدی برو بالا.",
        ],
    )
    smaller = tr(
        [
            "⬇️ Easy there! Try a smaller number.",
            "📉 Lower... before you reach the moon",
        ],
        [
            "⬇️ یه عدد پایین تر رو انتخاب کن.",
            "📉 اروم تر...پایین بیا تا به ماه نرسیدی",
        ],
    )

    if direction == "bigger":
        return random.choice(bigger)
    if direction == "smaller":
        return random.choice(smaller)


def get_guess(start, end):

    while True:
        try:

            guess = input(tr("whats your guess?", "حدست چیه?"))

            if guess == "menu":
                return "menu"
            if guess == "help":
                return "help"
            else:
                ans = int(guess)
            if start <= ans <= end:
                return ans
            else:

                print(
                    tr(
                        f"please enter number between {start} and {end} or enter (menu) and (help)",
                        f"لطفا فقط از بین اعداد {start} و {end} یا(menu) و (help) استفاده کنید",
                    )
                )

        except ValueError:

            print(tr("please sey just number", "لطفا فقط عدد وارد کن"))


def win(user_number, computer_number):
    return user_number == computer_number


def finished(final_score, time, bunos_time, score, guess, hint_count, computer_number):

    print(40 * "=")
    print(tr("🎉congratilations", "🎉 بهت تبریک میگم"))
    print(tr(f"My number was {computer_number}.", f"عدد من {computer_number} بود."))
    print(
        tr(
            f"🏆 finally Score: {score + bunos_time} \n ⭐ score: {score} \n🎯 Guesses: {guess} \n 🎁 hint count: {hint_count} \n ⏲ time: {int(time)} \n ⏱ time score : {bunos_time}",
            f"🏆 امتیاز نهایی: {score + bunos_time} \n⭐ امتیاز: {score} \n 🎯 تعداد حدس: {guess} \n 🎁تعداد کمک: {hint_count} \n ⏲ مدت زمان:{int(time)} \n ⏱ امتیاز زمان:{bunos_time}",
        )
    )
    rank(final_score)

    while True:

        answer = input(
            tr(
                "😏 Think you can beat your record? (Y/N) ",
                "😏 به نظرت میتونی دوباره رکورد بزنی? (Y/N) ",
            )
        )

        if answer.upper() == "Y":
            return True
        elif answer.upper() == "N":
            return False
        else:
            print(tr("please enter just (y) and (n)", "لطفا فقط (y) یا (n) وارد کن"))


def game():
    welcome()
    print("")
    resalt = difficulty()
    if resalt == "menu":
        return "menu"
    else:
        start, end = resalt

    print(tr("help -> enter (help)", "کمک -> بنویس (help)"))
    print(tr("menu -> enter(menu)", "منو -> بنویس(menu)"))

    continue_playing = True
    while continue_playing:
        computer_number = random.randint(start, end)
        score = 100
        gusse = 0
        count = 0
        hint_count = 0
        start_time = monotonic()
        while not win(gusse, computer_number):

            gusse = get_guess(start, end)
            if gusse == "menu":
                return
            if gusse == "help":

                if hint_count > 2:
                    print(40 * "=")
                    print(
                        tr(
                            "🚫 Hint limit reached! You can only use 3 hints.",
                            "🚫 به حد مجاز کمک رسیدید! فقط می‌توانید از ۳ کمک استفاده کنید.",
                        )
                    )
                    print(40 * "=")
                    continue
                else:
                    score, analyses_hint = help_(computer_number, score)
                if analyses_hint:
                    hint_count += 1
                continue

            if win(gusse, computer_number):
                count += 1
                break
            else:

                count += 1
                score -= 3
                print(answer(computer_number, gusse))
            if score < 0:
                print(40 * "=")
                print(
                    tr(
                        "you lose \n your scor is -...!!",
                        "تو باختی \n امتیازت منفی شد!!",
                    )
                )
                print(40 * "=")
                return

        end_time = monotonic()
        time_difrens = end_time - start_time

        range_number = end - start + 1
        time_score = round(
            max(0, 20 + 30 * math.log10(range_number / 20) - time_difrens)
        )

        finally_score = score + time_score
        high_score(finally_score)
        continue_playing = finished(
            finally_score,
            time_difrens,
            time_score,
            score,
            count,
            hint_count,
            computer_number,
        )

    print("=" * 40)
    print(tr("😤 You win... this time.", "😤 تو فقط این بارو بردی..."))
    print(tr("Don't get too confident.", "مغرور نشو."))
    print(tr("😈 I'll be waiting for our rematch.", "😈 تا بازی بعد منتظرت میمونم."))
    print("=" * 40)
