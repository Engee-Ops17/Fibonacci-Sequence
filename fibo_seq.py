def fib(x, a, b=None):
    """This function calculates the fibonacci sequence over any specified range:
        Equation: fib(arg1, arg2, kwarg1)
            arg1 = range
            arg2 = initial value (Acts as equation scale if Kwarg is not included)* 
            kwarg = second value (Optional - Defines step between first value and second value)
        """
    if b == None:
        b = a
    if b < a and a > 0:
        raise ValueError('Value of "b" should not be less than the value of "a" while (a>0)')
    if b > a and a < 0:
        raise ValueError('Value of "a" should not be less than the value of "b" while (a<0)')
    fib_seq = []
    for i in range(x-1):
        if i == 0 and b == a and a != 0:
            fib_seq.append(0)
            fib_seq.append(a)
            continue
        if b != a and i == 0:
            fib_seq.append(a)
            fib_seq.append(b)
            a = fib_seq[i]+fib_seq[i+1]
            continue
        if a == 0:
            fib_seq.append(a)
            a = 1
            fib_seq.append(a)
            continue
        fib_seq.append(a)
        a = fib_seq[i]+fib_seq[i+1]
    return fib_seq

if __name__ == "__main__":
    print("Test code")
    print(fib(20, 1, b=4))


       