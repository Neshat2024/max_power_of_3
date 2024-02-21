import time

st = time.time()


def power_time(number):
    start = time.time()
    print(number)
    n = 3 ** number
    estimated_time = time.time() - start
    print(estimated_time)
    return estimated_time


def guess_number(a, b):
    a_time = power_time(a)
    b_time = power_time(b)
    while not (a - b == 1 and a_time >= 60 and b_time < 60):
        if a_time >= 60 and b_time >= 60:
            a = b
            b = b // 2
            a_time = b_time
            b_time = power_time(b)
        elif a_time < 60 and b_time < 60:
            b = a
            a = a * 2
            b_time = a_time
            a_time = power_time(a)

        if a_time >= 60 and b_time < 60:
            dot = int(a - (((a_time - 60) / (a_time - b_time)) * (a - b)))
            dot_time = power_time(dot)
            if dot_time < 60 and dot_time >= 59:
                b = dot
                b_time = dot_time
                return b
            elif dot_time < 60:
                b = dot
                b_time = dot_time
            elif dot_time > 60:
                a = dot
                a_time = dot_time


print(guess_number(80000000, 10000))
print(f"The duration from beginning to end is: {time.time() - st}")
