
def bread(func):
    def wrapper(*args, **kwargs):
        print("</'''''\>")
        func(*args, **kwargs)
        print("<\_____/>")
    return wrapper


def ingredients(func):
    def wrapper(*args, **kwargs):
        print("#tomatoes#")
        func(*args, **kwargs)
        print("~salad~")
    return wrapper


@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)


if __name__ == '__main__':
    #sandwich()
    sandwich(food="cheese")
