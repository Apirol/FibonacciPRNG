class Generator:
    def __init__(self, a=55, b=24):
        self.buffer = self.__init_buffer__()
        self.a = a
        self.b = b
        self.base = 128

    def next(self):
        value = (self.buffer[self.second_index] + self.buffer[self.first_index]) % self.base
        del self.buffer[self.second_index]
        self.buffer.append(value)
        return value

    def __init_buffer__(self):
        ## конгруэнтный генератор
        X_0 = 3
        a = 1291
        c = 4621
        m = 21870
        return [(a * X_0 + c) % m for i in range(10000)]


if __name__ == '__main__':
    generator = Generator()

    for _ in range(10):
        print(generator.next())