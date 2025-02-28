def double(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result * 2
    return wrapper

@double
def get_number(number):
    return number

print(get_number(5))
