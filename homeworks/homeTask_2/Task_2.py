class StringIsNone(Exception):
    pass


class FloatNumber:

    def __init__(self, data):
        self.data = float(data)


def notIsString(data):
    if data != '':
        return True
    else:
        raise StringIsNone('Ввод не должен быть пустым')


def main():
    print("Для окончания ввода наберите 'end' или 'выход' ")
    print('Введите дробное число: ', end="")
    new = input()
    lst = []
    while new != 'end' and new != "выход":
        try:
            if notIsString(new):
                a = FloatNumber(new)
                lst.append(a.data)
        except StringIsNone:
            print('Вы ввели пустое значение')
        except Exception:
            print("Нельзя преобразовать строку в дробь ")
        else:
            print(f"Ваше число - {a.data}")
        finally:
            print('Введите дробное число: ', end="")
            new = input()

    print("Итоговый список: ")
    for el in lst:
        print(el, end=" ;  ")


if __name__ == "__main__":
    main()
