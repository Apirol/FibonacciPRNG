from fibonacci_prng import rand_fibonacci

if __name__ == '__main__':
    for i in range(100):
        print(next(rand_fibonacci(55)))
