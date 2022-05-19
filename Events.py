from datetime import *

"""Класс, реализующий отдельные события в списке
состоит из 5 полей: название, категория, время начала, время окончания и общая продолжительнотсь
имеются также 5 методов работы: создание нового объекта, придание ему статуса завершённого,
возврат события в состояния актива, перевод события в строковое представление и восстановление события
из строкового представления;
Вся работа с показателями времени осуществляется при помощи модуля datetime"""


class Events:
    name = ""  # Имя события
    st = None  # Время начала
    finish = None  # Время окончания
    length = None  # Общая продолжительность
    categ = None  # Категория события

    # Создание нового активного события
    def __init__(self, string, cat):
        self.name = string
        self.st = datetime.now()  # Фиксация времени начала
        self.categ = cat

    # Окончание события
    def fin(self):
        self.finish = datetime.now()  # Фиксация времени окончания
        self.length = (self.finish - self.st).total_seconds()  # Вычисление общей продолжительности

    # Возвращение события из состояния завершённости
    def ret(self):
        self.length = None
        self.finish = None

    # Перевод события в строковое представление (в виде списка строк)
    def to_str(self):
        data = [self.name, self.categ, self.st.strftime("%d.%m.%Y-%H.%M.%S")]
        if self.finish:
            data.append(self.finish.strftime("%d.%m.%Y-%H.%M.%S"))
            # Случай когда событие было новым
            if (type(self.length) != str):
                # Формализованная запись события (часы - минуты - секунды)
                if self.length // 3600 > 0:
                    hours = round(self.length // 3600)
                    minutes = round((self.length % 3600) // 60)
                    seconds = round((self.length % 3600) % 60)
                    data.append(f"{hours} ч. {minutes} мин. {seconds} сек.")
                elif self.length // 60 > 0:
                    minutes = round(self.length // 60)
                    seconds = round(self.length % 60)
                    data.append(f"{minutes} мин. {seconds} сек.")
                else:
                    data.append(f"{round(self.length)} сек.")
            else:
                data.append(self.length)
        else:
            data += ["----- ", "----- "]  # Добивание длины списка для незавршённых событий
        return data

    # Восстановление ранних событий из этой сессии
    def restore(self, data):
        self.name = data[0]
        self.categ = data[1]
        self.st = datetime.strptime(data[2], "%d.%m.%Y-%H.%M.%S")
        self.finish = None if (data[3] == "----- ") else datetime.strptime(data[3], "%d.%m.%Y-%H.%M.%S")
        self.length = None if (data[4] == "----- ") else data[4]
        return self
