def select_language():

    while True:

        an = input("select your language(english/persian)")

        if an == "english":

            return True

        elif an == "persian":

            return False

        else:

            print("please enter language persian or english")


its_english = select_language()


def tr(en, fa):

    if its_english:

        return en

    return fa
