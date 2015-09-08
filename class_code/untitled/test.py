
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
        3: 10,

    }
    return switcher.get(argument, "nothing")


x = numbers_to_strings(3)
