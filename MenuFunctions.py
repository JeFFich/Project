from tkinter import *
from Parametres import categories
from tkinter import messagebox as mb
from tkinter.filedialog import asksaveasfilename
from InternalFunctions import _add_categ, _del_categ, _categ_info, _analyse


"""Здесь собраны функции верхнего меню"""


# Очистка всех списков
def clear_all(frame1, frame2):
    # Дополнительное подтверждение
    answer = mb.askyesno(title=None, message="Вы точно хотите удалить все события?")
    if answer:
        # Перебор завершенных и незавершённых событий
        for frame in (frame1, frame2):
            index = len(frame.box_data) - 1
            # Удаление событий
            while (index >= 0):
                event = frame.box_data.pop(index)
                categories[event.categ].remove(event)
                frame.box.delete(index)
                index -= 1


# Работа с категориями
def categs(root, frame1, frame2):
    # Создание окна для работы с категориями
    window = Toplevel(root)
    window.title("Категории")
    window.resizable(False, False)
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 165
    h = h - 145
    window.geometry('330x290+{}+{}'.format(w, h))

    box_frame = Frame(window)
    box_frame.pack(side=LEFT)
    but_frame = Frame(window)
    but_frame.pack(side=LEFT, padx=10)
    label = Label(box_frame, text="Список категорий")
    lbox = Listbox(box_frame, height=70, width=30)
    for item in categories:
        lbox.insert(END, item)
    label.pack(anchor=W)
    lbox.pack(side=LEFT)
    scrollbar = Scrollbar(box_frame, command=lbox.yview)
    scrollbar.pack(side=LEFT, fill=Y)

    label = Label(but_frame, text="Новая категория:")
    entry = Entry(but_frame, width=20)
    # Привязка внутренних функций к кнопкам
    button1 = Button(but_frame, text="Добавить", width=20, command=lambda: _add_categ(entry, lbox))
    button2 = Button(but_frame, text="Удалить", width=20, command=lambda: _del_categ(lbox))
    button3 = Button(but_frame, text="Информация", width=20,
                     command=lambda: _categ_info(window, lbox, frame1.box_frame.box_data + frame2.box_frame.box_data))
    button4 = Button(but_frame, text="Анализ", width=20, command=lambda: _analyse(window, frame2))
    label.pack(anchor=W, side=TOP)
    entry.pack(side=TOP)
    button1.pack(side=TOP, anchor=E, pady=5)
    button2.pack(side=TOP, pady=5)
    button3.pack(side=TOP, pady=5)
    button4.pack(side=TOP, pady=5)
    window.grab_set()


# Экспорт завершённых событий
def export_results(frame):
    # Открытие файла для записи
    filename = asksaveasfilename(filetypes=(("TXT files", "*.txt"),))
    if filename:
        f = open(filename, "w")
        # Форматированная запись событий
        for event in list(map(lambda x: x.to_str(), frame.box_frame.box_data)):
            f.write(f"{event[2]}--{event[3]}: {event[0]} ({event[1]})")
            f.write("\n")
        f.close()
