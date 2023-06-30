class DataRecording:

    def __init__(self, data):
        print(data)
        self.data = data
        self.nameFile = data[0] + '.txt'
        self.savedData()

    def __str__(self):
        res = ""
        for el in self.data:
            res = res + " " + el
        return res[1:]

    def savedData(self):
        try:
            f = open(self.nameFile, 'a')
        except OSError:
            print('Не могу открыть файл')
        else:
            f.write(self.__str__()+'\n')
            f.close()
