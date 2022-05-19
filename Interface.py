from tkinter import *
from Parametres import *

"""Здесь собраны классы виджетов для основного окна"""


# Класс для рамки с Listbox
class _box_Frames:
    def __init__(self, label, root):
        self.frame = Frame(root)
        self.frame.pack()
        self.label = Label(self.frame, text=label)
        self.label.pack(anchor=W)
        self.box_data = []
        self.box = Listbox(self.frame, width=box_width, height=box_height, selectmode=EXTENDED)
        self.box.pack(side=LEFT)
        self.scrollbar = Scrollbar(self.frame, command=self.box.yview)
        self.scrollbar.pack(side=LEFT, fill=Y)


# Создание рамки для нижней панели
class _butt_Frames:
    def __init__(self, labels, root):
        self.frame = Frame(root)
        self.frame.pack(pady=frame_pady)
        self.button1 = _buttons(labels[0], self.frame, True)
        self.button2 = _buttons(labels[1], self.frame, False)


# Создание рамки для отдельного уровня кнопок
class _buttons:
    def __init__(self, label, root, flag):
        self.button = Button(root, text=label, width=but_width, justify=CENTER)
        if flag:
            self.button.pack(side=LEFT)
        else:
            self.button.pack(side=LEFT, padx=secbut_padx)


# Создание общей рамки
class gen_Frames:
    def __init__(self, labels, root):
        self.gen_frame = Frame(root)
        self.gen_frame.pack(side=LEFT, padx=frame_padx)
        self.box_frame = _box_Frames(labels[0], self.gen_frame)
        self.top_buttons = _butt_Frames(labels[1:3], self.gen_frame)
        self.bot_buttons = _butt_Frames(labels[3:5], self.gen_frame)

    # Подвязывание функций к кнопкам нижней панели
    def configurate(self, commands):
        self.top_buttons.button1.button["command"] = commands[0]
        self.top_buttons.button2.button["command"] = commands[1]
        self.bot_buttons.button1.button["command"] = commands[2]
        self.bot_buttons.button2.button["command"] = commands[3]


# Создание верхнего меню
class MainMenu:
    def __init__(self, root, main_labels, commands):
        self.mainmenu = Menu(root)
        # Добавление отдельных команд
        for index in range(len(main_labels)):
            self.mainmenu.add_command(label=main_labels[index], command=commands[index])
        root.config(menu=self.mainmenu)
