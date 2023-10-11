#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

try:
    r = Rectangle()
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r = Rectangle(1)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r = Rectangle(1, [12, 52])
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r = Rectangle(4, 5)
    print(r.width)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r = Rectangle(4, 5)
    print(r.height)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
