## generators
def count_up_to(n):
    i = 1
    while i <=n:
        yield i
        i += 1
for num in count_up_to(10):
    print(num)

## decorators
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@debug
def say_hi(name):
    print(f"Hi {name}")

say_hi("Ayo")

## context managers
