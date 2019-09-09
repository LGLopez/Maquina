import random
import  time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


counter = 0
creditsToPlay = 0

def create_window():
    window = Toplevel(root)

    window.geometry('500x500')

    rows = 0

    while rows < 50:
        window.rowconfigure(rows, weight=1)
        window.columnconfigure(rows, weight=1)
        rows += 1

    def counter_label():
        start = time.time()
        img = ImageTk.PhotoImage(Image.open("michi1.png"))
        img2 = ImageTk.PhotoImage(Image.open("michi2.png"))
        img3 = ImageTk.PhotoImage(Image.open("michi3.png"))

        photos = [img, img2, img3]
        photos2 = [img2, img3, img]
        photos3 = [img3, img, img2]

        label = Label(window, image=photos[counter])
        label2 = Label(window, image=photos[counter])
        label3 = Label(window, image=photos[counter])

        label.grid(row=5, column=0)
        label2.grid(row=5, column=2)
        label3.grid(row=5, column=4)

        def count():
            global counter
            counter += 1

            if counter == 3:
                counter = 0

            label.config(image=photos[counter])
            label2.config(image=photos2[counter])
            label3.config(image=photos3[counter])

            if time.time() - start < 3:
                label.after(200, count)
            else:
                global creditsToPlay
                creditsToPlay -= 7

                randNum = random.randint(0, 2)
                randNum2 = random.randint(0, 2)
                randNum3 = random.randint(0, 2)

                label.config(image=photos[randNum])
                label2.config(image=photos[randNum2])
                label3.config(image=photos[randNum3])

                if randNum == randNum2 and randNum == randNum3 and randNum3 == randNum2:
                    messagebox.showinfo("GANASTE!", "Ganaste 100 creditos")
                    creditsToPlay+=100
                else:
                    if randNum == randNum2 or randNum == randNum3 or randNum2 == randNum3:
                        messagebox.showinfo("GANASTE!", "Ganaste 20 creditos")
                        creditsToPlay += 20
                    else:
                        messagebox.showinfo("Perdiste :c", "Suerte para la proxima")

                toPrint = str(creditsToPlay)
                Label(root, text="Creditos " + toPrint).grid(row=2, column=49)



        count()

    Button(window, text="Jugar", command=counter_label).grid(row = 2, column = 10)
    Button(window, text="salir", command=window.destroy).grid(row=40, column=49)

def check_credits():
    global  creditsToPlay
    if creditsToPlay > 6:
        create_window()
    else:
        messagebox.showinfo("No puedes Jugar", "No tienes suficientes creditos")

def add_credits_1():
    global creditsToPlay
    creditsToPlay += 1
    toPrint = str(creditsToPlay)
    Label(root, text="Creditos " + toPrint).grid(row=2, column=49)

def add_credits_2():
    global creditsToPlay
    creditsToPlay += 2
    toPrint = str(creditsToPlay)
    Label(root, text="Creditos " + toPrint).grid(row=2, column=49)

def add_credits_5():
    global creditsToPlay
    creditsToPlay += 5
    toPrint = str(creditsToPlay)
    Label(root, text="Creditos " + toPrint).grid(row=2, column=49)

def add_credits_10():
    global creditsToPlay
    creditsToPlay += 10
    toPrint = str(creditsToPlay)
    Label(root, text="Creditos " + toPrint).grid(row=2, column=49)

def add_credits_20():
    global creditsToPlay
    creditsToPlay += 20
    toPrint = str(creditsToPlay)
    Label(root, text="Creditos " + toPrint).grid(row=2, column=49)


root = Tk()

root.title("Maquina de casino")
root.geometry("500x500")

rows = 0

while rows < 50:
    root.rowconfigure(rows, weight=1)
    root.columnconfigure(rows, weight=1)
    rows += 1

toPrint = str(creditsToPlay)
Label(root, text="Creditos " + toPrint).grid(row=2, column=49)

Button(root, text="Juego", command=check_credits).grid(row=0, column=2)
Button(root, text="1", command=add_credits_1).grid(row=3, column = 4)
Button(root, text="2", command=add_credits_2).grid(row=3, column = 6)
Button(root, text="5", command=add_credits_5).grid(row=3, column = 8)
Button(root, text="10", command=add_credits_10).grid(row=3, column = 10)
Button(root, text="20", command=add_credits_20).grid(row=3, column = 12)

Button(root, text="Sacar dinero").grid(row = 10, column = 2)

Button(root, text = "Salir", command = root.destroy).grid(row =49, column = 48)

root.mainloop()
