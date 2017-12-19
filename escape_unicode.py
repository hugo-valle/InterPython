
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap


@escape_unicode
def mexico_city():
    # Alt+130 for é
    return "México"


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before {}'.format(
            original_function.__name__ ))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print("Display function ran")


@decorator_function
def display_info(name, age):
    print("Display_info ran with parameters ({}{})".format(
        name, age ))

if __name__ == '__main__':
    # without decorator notation
    #decorated_display = decorator_function(display)
    #decorated_display()

    # Using decorator
    display()
    display_info("John", 25)
