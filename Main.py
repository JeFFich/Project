import json
from Parametres import labels_list, butlabels_list, mainmenu_list, file_name
from Interface import gen_Frames, MainMenu
from Functions import *
from MenuFunctions import *

# Создание главного окна
root = Tk()
root.title("Task-manager")
root.resizable(False, False)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 330
h = h - 290
root.geometry('660x580+{}+{}'.format(w, h))
# Добавление виджетов
frame1 = gen_Frames([labels_list[0]] + butlabels_list[0:4], root)
frame2 = gen_Frames([labels_list[1]] + butlabels_list[4:8], root)
frame1.configurate((lambda: adding(root, frame1), lambda: deleting(frame1), lambda: ending(frame1, frame2),
                    lambda: informate(root, frame1)))
frame2.configurate((lambda: returning(frame2, frame1), lambda: deleting(frame2), lambda: changing(root, frame2),
                    lambda: informate(root, frame2)))
menu = MainMenu(root, mainmenu_list,
                (lambda: export_results(frame2), lambda: categs(root, frame1, frame2),
                 lambda: clear_all(frame1.box_frame, frame2.box_frame)))
# Восстановление предыдущей сессии
file = open(file_name, "r", encoding='utf-8')
database = json.load(file)
file.close()
restore(database, frame1.box_frame, frame2.box_frame)
root.mainloop()
# Запись состояния сессиии
file = open(file_name, "w")
transformed_categs = {}
for categ in categories.keys():
    transformed_categs[categ] = list(map(lambda x: x.to_str(), categories[categ]))
database = {"unfinished": list(map(lambda x: x.to_str(), frame1.box_frame.box_data)),
            "finished": list(map(lambda x: x.to_str(), frame2.box_frame.box_data)),
            "categories": transformed_categs}
json.dump(database, file)
file.close()
