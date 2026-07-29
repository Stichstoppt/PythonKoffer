def show_lambdas():
    # note: in general, lambdas are anonymous functions, i.e. no name; use def instead

    a = 2
    f_mul = lambda x, y: a * x * y

    result = (lambda x, y, z=1: x + y + z)(2, 3)
