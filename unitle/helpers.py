from .language import tr


def get_number(start, end):
    while True:
        try:
            number = int(input(":"))
            if start <= number <= end:
                return number
            else:

                print(
                    tr(
                        f"please enter only number between {start} and {end}",
                        f" لطفا فقط از اعدادی بین {start} و {end}استفاده کنید",
                    )
                )

        except ValueError:
            print(tr("please enter just number", "لطفا فقط عدد بگو"))


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number**0.5 + 1)):

        if number % i == 0:
            return False
    return True
