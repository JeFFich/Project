from Parametres import labels_list, butlabels_list, mainmenu_list, filemenu_list
from Interface import gen_Frames, MainMenu
from Functions import *

root = Tk()
root.title("To-do лист")
root.resizable(False, False)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 330
h = h - 290
root.geometry('660x580+{}+{}'.format(w, h))

menu = MainMenu(root, mainmenu_list, filemenu_list)
data_frame1 = [labels_list[0]] + butlabels_list[0:4]
data_frame2 = [labels_list[1]] + butlabels_list[4:8]
frame1 = gen_Frames(data_frame1, root)
frame2 = gen_Frames(data_frame2, root)
frame1.configurate((lambda: adding(root, frame1), lambda: deleting(frame1), lambda: ending(root, frame1, frame2),
                    lambda: informate(root, frame1)))
frame2.configurate((lambda: returning(frame2, frame1), lambda: deleting(frame2), lambda: changing(root, frame2),
                    lambda: informate(root, frame2)))
root.mainloop()
