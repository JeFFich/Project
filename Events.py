from datetime import *


class Events:
    name = ""
    st = None
    finish = None
    length = None
    categ = None

    def __init__(self, string):
        self.name = string
        self.st = datetime.now()

    def fin(self, cat):
        self.finish = datetime.now()
        self.length = (self.finish - self.st).total_seconds()
        self.categ = cat

    def ret(self):
        self.length = None
        self.finish = None
        self.categ = None

    def to_str(self):
        data = [self.name, self.st.strftime("%d.%m.%Y-%H.%M.%S")]
        if self.finish is not None:
            data += [self.finish.strftime("%d.%m.%Y-%H.%M.%S"), self.categ]
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
        return data
