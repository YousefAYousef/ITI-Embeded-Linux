import os
from time import sleep

n = 6
space = '  '
star = '* '
speed = 0.5

def up():
    for i in range(n * 2):
        print(space * (n * 2), end="")
        print(space * (n * 3 - 1) + star)
    for i in range(n):
        print(space * (n * 4), end="")
        print(space * (n - (i + 1)), end="")
        print(star * (i + 1), end="")
        print(star * i, end="")
        print(space * (n - i))
    for i in range(n * 2):
        print(space * (n * 2), end="")
        print(space * (n * 3 - 1) + star)

def left():
    for i in range(n * 4):
        print("")
    for i in range(n):
        print(space * (n * 2), end="")
        print(space * (n - (i + 0)), end="")
        print(star * (i + 0))
    print(star * (n * 5))
    for i in range(n):
        print(space * (n * 2), end="")
        print(space * (i + 1), end="")
        print(star * (n - (i + 1)))

def right():
    for i in range(n * 4):
        print("")
    for i in range(n):
        print(space * (n * 5), end="")  # left arrow space
        print(space * (n * 2), end="")
        print(star * (i + 0), end="")
        print(space * (n - (i + 0)))
    print(space * (n * 5), end="")
    print(star * (n * 4))
    for i in range(n):
        print(space * (n * 5), end="")  # left arrow space
        print(space * (n * 2), end="")
        print(star * (n - (i + 1)), end="")
        print(space * (i + 1))

def down():
    for i in range((n * 5) + 1):
        print("")
    for i in range(n * 2):
        print(space * (n * 2), end="")
        print(space * (n * 3 - 1) + star)
    for i in range(n):
        print(space * (n * 4), end="")
        print(space * (i + 0), end="")
        print(star * (n - (i + 0)), end="")
        print(star * (n - (i + 1)), end="")
        print(space * (i + 1))
    for i in range(n * 2):
        print(space * (n * 2), end="")
        print(space * (n * 3 - 1) + star)

while True:
    left()
    sleep(speed)
    os.system('cls')

    up()
    sleep(speed)
    os.system('cls')

    right()
    sleep(speed)
    os.system('cls')

    down()
    sleep(speed)
    os.system('cls')