from tkinter import *
from tkinter import messagebox as mb
from Events import *
from Parametres import categories, information_list
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

"""Здесь собраны все внутренние функции,
осуществляющие различные преоразования"""


# Добавление нового события в список
def _add_item(window, entry, frame, categ):
    s = entry.get()  # Получение имени нового события
    if not s.split():  # Проверка на пустую строку
        entry.delete(0, END)
        mb.showerror(title=None, message="Имя должно содержать хотя бы один не пробельный символ")
    else:
        # Проверка на наличие схожего незавершённого события
        for item in frame.box_frame.box_data:
            if (s == item.name) & (categ == item.categ):
                entry.delete(0, END)
                mb.showerror(title=None, message="Событие с таким названием уже есть в списке!")
                return
        frame.box_frame.box.insert(END, s)  # Вставка нового элемента в Listbox
        event = Events(s, categ)  # Создание нового события
        categories[categ].append(event)  # Добавление его в список для выбранной категории
        frame.box_frame.box_data.append(event)  # Добавление его в список текущих незавершённых событий
        entry.delete(0, END)  # Очистка поля ввода
        window.destroy()


# Окончание событий
def _fin_transfer(selected, frame_from, frame_to):
    # Итерация всех выделенных для окончания событий
    for index in selected:
        event = frame_from.box_frame.box_data.pop(index)  # Удаление элемента из списка незавршённых
        event.fin()  # Заврешение события
        frame_to.box_frame.box.insert(END, event.name)  # Вставка его в Listbox завершённых
        frame_to.box_frame.box_data.append(event)  # Добавление в список завершённых
        frame_from.box_frame.box.delete(index)  # Удаление из Listboxa незавершённых


# Изменение категорий у выбранных завершённых событий
def _change_category(category, events, window):
    # Итерация всех выделенных событий
    for event in events:
        categories[event.categ].remove(event)  # Удаление выделенного события из списка старой категории
        event.categ = category  # Изменение категории события
        categories[category].append(event)  # Добавление в список новой категории
    window.destroy()


# Построение окна с информацией
def _informate(root, events):
    window = Toplevel(root)
    window.title("Информация о событиях")
    window.resizable(False, False)
    frame_gen = Frame(window)
    frame_gen.pack(side=LEFT)
    ind = 0
    # Итерация выделенных событий
    for event in events:
        ind += 1
        item = event.to_str()  # Перевод события в список строк
        frame = LabelFrame(frame_gen, text="Событие №" + str(ind))  # Создание нумерованной рамки
        frame.pack()
        # Добавление надписей
        for i in range(5):
            label = Label(frame, text=information_list[i] + item[i], justify=RIGHT)
            label.pack()
        # Создание новой рамки для адекватного отображения большого числа событий
        if ind % 6 == 0:
            frame_gen = Frame(window)
            frame_gen.pack(side=LEFT)
    window.update()
    window.grab_set()


# Добавление новой категории
def _add_categ(entry, box):
    new = entry.get()
    entry.delete(0, END)
    # Обработка пустой строки
    if not new.split():
        mb.showerror(title=None, message="Имя должно содержать хотя бы один не пробельный символ")
    else:
        # Обработка наличия такой же категории
        if (new in categories.keys()):
            mb.showerror(title=None, message="Такая категория уже есть в списке!")
        else:
            # Создание новой категории
            categories[new] = []
            box.insert(END, new)


# Удаление категории
def _del_categ(box):
    selected = list(box.curselection())
    # Обработка пустого выделения
    if not selected:
        mb.showerror(title=None, message="Категория не выбрана!")
    # Обработка случая наличия последней категории
    elif len(categories.keys()) == 1:
        mb.showerror(title=None, message="Должна оставаться хотя бы одна категория!")
    else:
        categ = list(categories.keys())[selected[0]]
        # Обработка случая наличия привязанных к данной категории событий
        if categories[categ]:
            mb.showerror(title=None, message="В данный момент удаление категории невозможно")
        else:
            # Дополнительное подтверждение
            answer = mb.askyesno(title=None, message="Вы точно хотите удалить выбранные категории?")
            if answer:
                #  Удаление категорий
                box.delete(selected[0])
                del categories[categ]


# Вывод информации о событиях категории
def _categ_info(root, box, data):
    selected = list(box.curselection())
    # Обработка пустого выбора
    if not selected:
        mb.showerror(title=None, message="Категория не выбрана!")
    else:
        categ = list(categories.keys())[selected[0]]
        # Взятие всех нужных событий
        new_data = [item for item in data if (item.categ == categ)]
        # Обработка случая пустой категории
        if not new_data:
            mb.showinfo(title=None, message="Данная категория пуста")
        else:
            _informate(root, new_data)  # Вызов внутренней функции


# Анализ списка категорий на численность
def _analyse(root, frame):
    # Обработка случая отсутствия завершённых событий
    if not(frame.box_frame.box_data):
        mb.showerror(title=None, message="Анализ невозможен, так как отсутствуют завершённые события")
    else:
        # Создание окна анализа
        window = Toplevel(root)
        window.title("Анализ")
        window.resizable(False, False)
        w = window.winfo_screenwidth()
        h = window.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - 225
        h = h - 145
        window.geometry('450x290+{}+{}'.format(w, h))
        # Подсчёт числа событий по категориям
        data = {}
        total_count = 0
        for event in frame.box_frame.box_data:
            if event.categ in data.keys():
                data[event.categ] += 1
                total_count += 1
            else:
                data[event.categ] = 1
                total_count += 1
        counts = []
        for categ in data.keys():
            counts.append(data[categ]/total_count)
        # Создание именной рамки
        frame1 = LabelFrame(window, text="Анализ количества")
        lab1 = Label(frame1, text=f"Общее число завершённых событий: {total_count}")
        lab1.pack(anchor=W)
        # Создание круговой диаграммы
        fig1 = Figure()
        ax1 = fig1.add_subplot()
        ax1.pie(counts, radius=1, labels=data.keys(), autopct='%0.2f%%')
        chart1 = FigureCanvasTkAgg(fig1, frame1)
        chart1.get_tk_widget().pack()
        frame1.pack()

        window.grab_set()
