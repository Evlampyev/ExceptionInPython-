# Реализуйте 3 метода, чтобы в каждом из них получить разные исключения
# Посмотрите на код, и подумайте сколько разных типов исключений вы тут сможете получить?

import string


class ExceptionNotTitle(Exception):
    pass


class RepeatWords(Exception):
    pass


class Base:
    def __init__(self):
        self.base = []

    def __add__(self, other):
        self.base.append(other)

    def printBase(self):
        for el in self.base:
            print(el)

    def __len__(self):
        return len(self)


class Unit:

    def __init__(self, data: string):
        self.capability = False
        try:
            if firstIsBig(data):  # если ФИО с заглавной буквы
                data = data.split()
                if (data[0] != data[1]) and (data[0] != data[2]) and (
                        data[1] != data[2]):  # Если нет повторояющихся слов
                    self.lastName = data[0]
                    self.firstName = data[1]
                    self.patronymic = data[2]
                    self.capability = True
                else:
                    raise RepeatWords("Repeat words")

        except ExceptionNotTitle as e:
            print(e)

    def __str__(self):
        return self.lastName + " " + self.firstName + " " + self.patronymic


def firstIsBig(fullName: string):
    if fullName.istitle():
        return True
    raise ExceptionNotTitle("Invalid input. Each word must be capitalized")


def main():
    base = Base()
    print("New unit: ", end="")
    new = input()
    while new != "exit" or new != "выход":

        try:
            newData = Unit(new)  # если был создан пользователь
            if newData.capability:
                base.__add__(newData)  # тогда его добавить в базу
        except:
            print("Unit not create")
        else:
            pass

        print("New unit: ", end="")
        new = input()
    print(f'Размер базы: {base.base.__len__()}')
    base.printBase()


if __name__ == "__main__":
    main()
