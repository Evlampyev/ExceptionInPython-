class calc:
    def __init__(self, data):
        self.data = data
        self.a, self.b = map(int, data.split('/'))

    def result(self):
        if self.b == 0:
            raise RuntimeError("На ноль делить нельзя")
        else:
            print(self.a / self.b)


def main():
    A = calc(input())
    A.result()


if __name__ == "__main__":
    main()
