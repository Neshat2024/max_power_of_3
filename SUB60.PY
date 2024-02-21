import time
import sys
sys.set_int_max_str_digits(10000)

def timer(a):
    start = time.perf_counter()
    3**a
    end = time.perf_counter()

    return round( end - start, 6)

def subfinder(a, b):
    t_a = timer(a)
    t_b = timer(b)
    n = 0
    ans = 0
    while not (abs((60-t_b))<0.1):
        if t_b <10:
            x = (b-a)*10+a
                    
        else:
            x = a  - int((a-b)*(t_a - 60)/(t_a - t_b))

        a = b
        t_a = t_b
        b = x
        t_b = timer(b)

        if t_b <61 and t_b>59 :
            if n == 5:
                return num
            else:
                ans += b
                n += 1
                num = b//n
    return b


                

        
        



print(subfinder(2000000, 5000000))