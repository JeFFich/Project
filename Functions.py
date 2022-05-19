from InternalFunctions import _add_item, _fin_transfer, _change_category, _informate
from Events import Events
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox as combo
from Parametres import wid, heig, but_width, categories
from Interface import _butt_Frames

"""Здесь собраны все функции, работающие с кнопками нижней панели"""


# Функция добавления нового события
def adding(root, frame):
    # Создание окна добавления
    window = Toplevel(root)
    window.title("Добавление события")
    window.geometry('200x110+{}+{}'.format(wid-100, heig-55))
    window.resizable(False, False)
    label = Label(window, text="Наименование события")
    label.pack()
    entry = Entry(window, width=30)
    entry.pack()
    label = Label(window, text="Категория события")
    label.pack()
    com = combo(window, values=list(categories.keys()))
    com.current(0)
    com.pack()
    # Привязывание внутренней функции добавления к кнопке
    button = Button(window, text="Добавить", width=but_width, command=lambda: _add_item(window, entry, frame,
                                                                                        list(categories.keys())[com.current()]))
    button.pack()
    window.grab_set()


# Функция завершения события
def ending(frame_from, frame_to):
    selected = list(frame_from.box_frame.box.curselection())
    selected.reverse()
    # Обработка пустого выделения
    if len(selected) == 0:
        mb.showerror(title=None, message="Никаких элементов не было выбрано")
    else:
        # Дополнительное подтверждение
        answer = mb.askyesno(title=None, message="Вы точно хотите завершить выбранные события?")
        if answer:
            _fin_transfer(selected, frame_from, frame_to)  # Вызов внутренней функции завершения


# Функция, удаляющая выбранные события из списка
def deleting(frame):
    selected = list(frame.box_frame.box.curselection())
    # Обработка пустого выделения
    if len(selected) == 0:
        mb.showerror(title=None, message="Никаких элементов не было выбрано")
    else:
        # Дополнительное подтверждение
        answer = mb.askyesno(title=None, message="Вы точно хотите удалить выбранные события?")
        if answer:
            selected.reverse()
            # Итерация выбранных событий
            for index in selected:
                frame.box_frame.box.delete(index)  # Удаление события из Listbox
                # Удаление события из списка для категории
                categories[frame.box_frame.box_data[index].categ].remove(frame.box_frame.box_data[index])
                frame.box_frame.box_data.pop(index)  # Удаление из списка событий


# Функция для получения информации о событиях
def informate(root, frame):
    selected = list(frame.box_frame.box.curselection())
    # Обработка пустого выделения
    if len(selected) == 0:
        mb.showerror(title=None, message="Никаких событий не было выбрано")
    else:
        _informate(root, [frame.box_frame.box_data[index] for index in selected])  # Вызов внутренней функции


# Функция для возврата событий из состояния завершенности
def returning(frame_from, frame_to):
    selected = list(frame_from.box_frame.box.curselection())
    selected.reverse()
    # Обработка пустого выделения
    if len(selected) == 0:
        mb.showerror(title=None, message="Никаких событий не было выбрано")
    else:
        # Дополнительное подтверждение
        answer = mb.askyesno(title=None, message="Вы точно хотите отменить завершённость выбранных событий?")
        if answer:
            # Итерация выделенных событий
            for index in selected:
                frame_from.box_frame.box_data[index].ret()  # Возврат события
                # Добавление его в список незавершённых
                frame_to.box_frame.box_data.append(frame_from.box_frame.box_data[index])
                # Вставка в новый Listbox
                frame_to.box_frame.box.insert(END, frame_from.box_frame.box_data[index].name)
                frame_from.box_frame.box.delete(index)  # Удаление из старого Listbox
                frame_from.box_frame.box_data.pop(index)  # Удаление из списка завершённых


# Функция изменения категории у выбранных событий
def changing(root, frame):
    selected = list(frame.box_frame.box.curselection())
    selected.reverse()
    # Обработка пустого выделения
    if len(selected) == 0:
        mb.showerror(title=None, message="Никаких элементов не было выбрано")
    else:
        # Создание окна удаления
        window = Toplevel(root)
        window.title("Изменение категории")
        window.geometry('300x70+{}+{}'.format(wid - 150, heig - 35))
        window.resizable(False, False)
        label = Label(window, text="Выберите новую категорию")
        label.pack()
        com = combo(window, values=list(categories.keys()))
        com.current(0)
        com.pack()
        but_frame = _butt_Frames(("Изменить", "Отмена"), window)
        # Привязывания внутренней функции к кнопке
        but_frame.button1.button["command"] = lambda: _change_category(list(categories.keys())[com.current()],
                                                                       [frame.box_frame.box_data[index] for index in selected], window)
        but_frame.button2.button["command"] = window.destroy
        window.grab_set()


# Функция восстановления предыдущей незавершённой сессии
def restore(data, frame1, frame2):
    # Итерация по категориям
    for categ in data["categories"].keys():
        categories[categ] = []
        # Итерация по событиям
        for event in data["categories"][categ]:
            # Восстановление событий
            new = Events(None, None).restore(event)
            categories[categ].append(new)
            # Добавление событий в нужные списки и Listbox
            if new.finish:
                frame2.box_data.append(new)
                frame2.box.insert(END, new.name)
            else:
                frame1.box_data.append(new)
                frame1.box.insert(END, new.name)
