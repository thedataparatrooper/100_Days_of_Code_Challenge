fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    """Make pie at the given index"""
    try:
        fruit = fruits[index]

    except IndexError as error_message:
        print(F"The {error_message} error happened.")

    else:
        print(fruit + " pie")


make_pie(2)