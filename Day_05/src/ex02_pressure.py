import random
import time


def emit_gel(step):
    while True:
        num = random.randrange(0, 100, step)
        i = yield num
        if i is not None:
            step = i


def valve():
    step = 3
    E = emit_gel(step)
    for eg in E:
        while (eg > 80) or (eg < 20):
            if eg > 90 or eg < 10:
                E.close()
            r = random.randint(1, 99)
            eg = E.send(r)

        yield eg


def test():
    for v in valve():
        print(v)
        time.sleep(1)


if __name__ == "__main__":
    test()
