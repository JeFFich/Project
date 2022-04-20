from tkinter import *

# Создание основного окна
root = Tk()
root.title("To-do лист")
root.resizable(False, False)

# Верхнее меню для основного окна
mainmenu = Menu(root)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Импорт новых событий")
filemenu.add_command(label="Экспорт завершённых событий")
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_command(label="Категории")
mainmenu.add_command(label="Анализ")
mainmenu.add_command(label="Очистить всё")
root.config(menu=mainmenu)

# Создание правой рамки (работа с активными событиями)
frame1 = Frame(root)
frame1.pack(side=LEFT, padx=10)
# Подрамка для списка активных событий со скроллером
box_frame1 = Frame(frame1)
box_frame1.pack()
label1 = Label(box_frame1, text="Текущие события:")
label1.pack(anchor=W)
lbox1 = Listbox(box_frame1, width=48, height=30)
lbox1.pack(side=LEFT)
scrollbar1 = Scrollbar(box_frame1, command=lbox1.yview)
scrollbar1.pack(side=LEFT, fill=Y)
# Подрамка для верхних кнопок
butt_topframe1 = Frame(frame1)
butt_topframe1.pack(pady=5)
add_butt1 = Button(butt_topframe1, text="Добавить событие", width=20, justify=CENTER)
del_butt1 = Button(butt_topframe1, text="Удалить событие", width=20, justify=CENTER)
add_butt1.pack(side=LEFT)
del_butt1.pack(side=LEFT, padx=5)
# Подрамка для нижних кнопок
butt_botframe1 = Frame(frame1)
butt_botframe1.pack(side=BOTTOM, pady=2)
fin_butt = Button(butt_botframe1, text="Завершить событие", width=20, justify=CENTER)
info_butt1 = Button(butt_botframe1, text="Информация о событии", width=20, justify=CENTER)
fin_butt.pack(side=LEFT)
info_butt1.pack(side=LEFT, padx=5)

# Создание левой рамки (работа с завершенными событиями)
frame2 = Frame(root)
frame2.pack(side=LEFT, padx=10)
# Подрамка для списка завершённых событий со скроллером
box_frame2 = Frame(frame2)
box_frame2.pack()
label2 = Label(box_frame2, text="Завершённые события:")
label2.pack(anchor=W)
lbox2 = Listbox(box_frame2, width=48, height=30)
lbox2.pack(side=LEFT)
scrollbar2 = Scrollbar(box_frame2, command=lbox2.yview)
scrollbar2.pack(side=LEFT, fill=Y)
# Подрамка для верхних кнопок
butt_topframe2 = Frame(frame2)
butt_topframe2.pack(pady=5)
change_butt = Button(butt_topframe2, text="Отменить завершенность", width=20, justify=CENTER)
del_butt2 = Button(butt_topframe2, text="Удалить событие", width=20, justify=CENTER)
change_butt.pack(side=LEFT)
del_butt2.pack(side=LEFT, padx=5)
# Подрамка для нижних кнопок
butt_botframe2 = Frame(frame2)
butt_botframe2.pack(side=BOTTOM, pady=2)
return_butt = Button(butt_botframe2, text="Изменить категорию", width=20, justify=CENTER)
info_butt2 = Button(butt_botframe2, text="Информация о событии", width=20, justify=CENTER)
return_butt.pack(side=LEFT)
info_butt2.pack(side=LEFT, padx=5)

root.mainloop()
