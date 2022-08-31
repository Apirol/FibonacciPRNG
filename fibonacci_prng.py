def set_attributes(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


@set_attributes(buffer=[])
def rand_fibonacci(n, a=55, b=24, X_0=3, a_fib=1291, c_fib=4621, m_fib=21870, base=128):
    a_index = n - a
    b_index = n - b
    if len(rand_fibonacci.buffer) == 0:
        rand_fibonacci.buffer = init_buffer(X_0, a_fib, c_fib, m_fib)
    for i in range(2**128):
        value = (rand_fibonacci.buffer[a_index] + rand_fibonacci.buffer[b_index]) % base
        del rand_fibonacci.buffer[a_index]
        rand_fibonacci.buffer.append(value)
        yield value


def init_buffer(X_0=3, a=1291, c=4621, m=21870):
    return [(a * X_0 + c) % m for i in range(10000)]
