from fibonacci_prng import rand_fibonacci
from test import visual_test

if __name__ == '__main__':
    test_sequence = [next(rand_fibonacci(55)) for i in range(1000)]
    visual_test(test_sequence)
