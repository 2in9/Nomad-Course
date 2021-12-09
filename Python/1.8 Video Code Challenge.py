def plus(x, y):
    return int(x) + int(y)


def minus(x, y):
    return int(x) - int(y)


def times(x, y):
    return int(x) * int(y)


def division(x, y):
    return int(x) / int(y)


def reminder(x, y):
    return int(x) % int(y)


def negation(x):
    return int(-x)


def power(x, y):
    return int(x) ** int(y)


x = 10
y = "2"

print(plus(x, y))
print(minus(x, y))
print(times(x, y))
print(division(x, y))
print(reminder(x=11, y="3"))
print(negation(x))
print(power(x, y))
