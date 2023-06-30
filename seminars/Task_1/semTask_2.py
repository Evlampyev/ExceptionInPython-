class CloseCounter (Exception):
    pass


class Counter:

    def __init__(self):
        self.possibility = True
        self.count = 0

    def add(self, data):
        if data == 'close':
            self.close()
        else:
            try:
                if counterOpen(self.possibility):
                    self.count += 1
                    print(f"Текущий счетчик равен = {self.count}")
            except CloseCounter as e:
                print("Counter is closed")
            else:
                print("Magnification counter")

    def close(self):
        self.possibility = False


def main():
    A = Counter()
    print("Input data: ", end="")
    new = input()
    while new != "end":
        A.add(new)
        print("Input data: ", end="")
        new = input()


def counterOpen(condition):
    if condition:
        return True
    raise CloseCounter('Counter is closed')


if __name__ == '__main__':
    main()
