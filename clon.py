import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

# Кнопка Закрыть
def on_closing():
    if tk.messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        window.destroy()


# Загрузка фото
def imageUploader():
    global path, img1_0, img2_0
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)
    if len(path):
        img = Image.open(path)
        if img.size[0] / img.size[1] > 1.8:
            img1_0 = img.crop((0, 0, img.size[0] / 2, img.size[1]))
            img2_0 = img.crop((img.size[0] / 2, 0, img.size[0], img.size[1]))
        else:
            img1_0 = img
        img = img_resize(img1_0)
        pic = ImageTk.PhotoImage(img)
        label1.config(image=pic)
        label1.image = pic
    else:
        print("No file is Choosen !! Please choose a file.")


# Загрузка папки с клонами
def clone_imageUploader():
    global path_dir, files, img1, img2
    path_dir = tk.filedialog.askdirectory()
    files = os.listdir(path_dir)
    if len(files):
        for i in range(len(files)-1, -1, -1):
            if files[i].endswith(".png") or files[i].endswith(".jpg") or files[i].endswith(".jpeg"):
                pass
            else:
                del files[i]
        img = Image.open(path_dir+'/'+files[0])
        if img.size[0] / img.size[1] > 1.8:
            img1 = img.crop((0, 0, img.size[0] / 2, img.size[1]))
            img2 = img.crop((img.size[0] / 2, 0, img.size[0], img.size[1]))
        img = img_resize(img1)
        pic = ImageTk.PhotoImage(img)
        label2.config(image=pic)
        label2.image = pic
    else:
        print("No file is Choosen !! Please choose a file.")


def img_resize(img):
    if img.size[0] >= img.size[1]:
        wide_size = (box / float(img.size[0]))
        height_size = int((float(img.size[1]) * float(wide_size)))
        img = img.resize((box, height_size))
    else:
        wide_size = (box / float(img.size[1]))
        height_size = int((float(img.size[0]) * float(wide_size)))
        img = img.resize((height_size, box))
    return img


# Кнопка Назад
def prev():
    global count, count_t, img1, img2, path_dir, files
    count_t = 0
    if img1 is None:
        clone_imageUploader()
        return
    if count == 0:
        count = len(files)-1
        img = Image.open(path_dir + '/' + files[count])
        if img.size[0] / img.size[1] > 1.8:
            img1 = img.crop((0, 0, img.size[0] / 2, img.size[1]))
            img2 = img.crop((img.size[0] / 2, 0, img.size[0], img.size[1]))
        img = img_resize(img1)
        pic = ImageTk.PhotoImage(img)
        label2.config(image=pic)
        label2.image = pic
    else:
        count -= 1
        img = Image.open(path_dir + '/' + files[count])
        if img.size[0] / img.size[1] > 1.8:
            img1 = img.crop((0, 0, img.size[0] / 2, img.size[1]))
            img2 = img.crop((img.size[0] / 2, 0, img.size[0], img.size[1]))
        img = img_resize(img1)
        pic = ImageTk.PhotoImage(img)
        label2.config(image=pic)
        label2.image = pic

# Кнопка Вперед
def next():
    global count, count_t, img1, img2, path_dir, files
    count_t = 0
    count += 1
    if img1 is None:
        clone_imageUploader()
        return
    if len(files) > count:
        img = Image.open(path_dir + '/' + files[count])
        if img.size[0] / img.size[1] > 1.8:
            img1 = img.crop((0, 0, img.size[0] / 2, img.size[1]))
            img2 = img.crop((img.size[0] / 2, 0, img.size[0], img.size[1]))
        img = img_resize(img1)
        pic = ImageTk.PhotoImage(img)
        label2.config(image=pic)
        label2.image = pic
    else:
        count = 0
        img = Image.open(path_dir + '/' + files[count])
        if img.size[0] / img.size[1] > 1.8:
            img1 = img.crop((0, 0, img.size[0] / 2, img.size[1]))
            img2 = img.crop((img.size[0] / 2, 0, img.size[0], img.size[1]))
        img = img_resize(img1)
        pic = ImageTk.PhotoImage(img)
        label2.config(image=pic)
        label2.image = pic


def turn0():
    global count_t0
    if img2_0 is None:
        imageUploader()
        return
    if count_t0 == 0:
        img = img_resize(img2_0)
        count_t0 = 1
    else:
        img = img_resize(img1_0)
        count_t0 = 0
    pic = ImageTk.PhotoImage(img)
    label1.config(image=pic)
    label1.image = pic


def turn():
    global count_t
    if img2 is None:
        clone_imageUploader()
        return
    if count_t == 0:
        img = img_resize(img2)
        count_t = 1
    else:
        img = img_resize(img1)
        count_t = 0
    pic = ImageTk.PhotoImage(img)
    label2.config(image=pic)
    label2.image = pic



if __name__ == "__main__":
    box = 750
    count = 0
    count_t = 0
    count_t0 = 0
    img1, img2, img1_0, img2_0 = None, None, None, None

    window = tk.Tk()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.title("Ищем клоны")

    window.resizable(0, 0)
    w = 1600
    h = 800
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.option_add("*tearOff", False)

    label1 = tk.Label(window)
    label1.place(x=30, y=10)
    label2 = tk.Label(window)
    label2.place(x=810, y=10)

    main_menu = tk.Menu()
    main_menu.add_cascade(label="Выбрать фото монеты", command=imageUploader)
    main_menu.add_cascade(label="Выбрать папку с клонами", command=clone_imageUploader)
    main_menu.add_cascade(label="Выход", command=on_closing)

    btn0 = tk.Button(text='Другая сторона монеты', command=turn0)
    btn0.place(x=50, y=770)
    btn1 = tk.Button(text='Предыдущее фото', command=prev)
    btn1.place(x=850, y=770)
    btn2 = tk.Button(text='Следующее фото', command=next)
    btn2.place(x=1050, y=770)
    btn3 = tk.Button(text='Другая сторона монеты', command=turn)
    btn3.place(x=1400, y=770)

    window.config(menu=main_menu)
    window.mainloop()