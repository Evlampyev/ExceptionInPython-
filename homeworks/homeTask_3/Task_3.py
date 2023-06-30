import string

from SaveData import DataRecording


class FullData(Exception):
    pass


class Unit:
    fields = ["Фамилия", "Имя", "Отчество", "Дата рождения", "Телефон", "Пол"]

    def __init__(self, data):
        self.canSave = False
        data = data.split(' ')
        try:
            if checkFullData(data):
                self.canSave = True
        except FullData as e:
            print(e)
            self.canSave = False
        if self.canSave:
            for i in range(3):
                if not (data[i].isalpha()):
                    self.mistake(i)
            if len(data[3].split('.')) != 3:
                self.mistake(3)
            if not(data[4].isdigit()):
                self.mistake(4)
            if data[5] not in {'f', 'm'}:
                self.mistake(5)
        if self.canSave:
            self.data = data
        else:
            raise Exception('Запись не создана')

    def mistake(self, num):
        print(f"Данные поля '{Unit.fields[num]}' не являются корректными")
        self.canSave = False

    def __str__(self):
        result = ""
        for el in self.data:
            result = result + " " + el
        return result[1:]

    def saveUnit(self):
        try:
            DataRecording(self.data)
        except Exception:
            print("Последние данные не сохранены")
        else:
            print("- - Данные сохранены - -")


def checkFullData(data: string) -> bool:
    """
    проверка на ввод всех данных
    :param data: строка данных
    :return: bool
    """
    if len(data) < 6:
        raise FullData("Вы ввели не все данные")
    elif len(data) > 6:
        raise FullData("Количество данных избыточно")
    else:
        return True


def main():
    print("'end' - для окончания ввода")
    print("Введите данные:", end=" ")
    new = input()
    while new != "end":
        try:
            newData = Unit(new)
            newData.saveUnit()
        except Exception:
            print("Какая-то ошибка")
        finally:
            print("Введите данные:", end=" ")
            new = input()



if __name__ == "__main__":
    main()

# Иванов Иван Иванович 01.02.23 1245456 f
