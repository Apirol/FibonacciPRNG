from fibonacci_prng import rand_fibonacci
import matplotlib.pyplot as plt


def visual_test(sequence:list):
    plt.plot(sequence, 'o')
    plt.xlabel('Index number')
    plt.ylabel('Value')
    plt.show()
