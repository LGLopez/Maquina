import random
import  time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

cambio = [1, 2, 5, 10, 20]
conteo = [0, 0, 0, 0, 0]
counter = 0
creditsToPlay = 0

def create_window():
    window = Toplevel(root)

    window.geometry('500x500')

    toPrint = str(creditsToPlay)
    Label(window, text="Creditos " + toPrint).grid(row=2, column=49)

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
            global creditsToPlay
            if creditsToPlay > 6:
                if time.time() - start < 3:
                    label.after(200, count)
                else:
                    creditsToPlay -= 7

                    randNum = random.randint(0, 2)
                    randNum2 = random.randint(0, 2)
                    randNum3 = random.randint(0, 2)

                    label.config(image=photos[randNum])
                    label2.config(image=photos[randNum2])
                    label3.config(image=photos[randNum3])

                    if randNum == randNum2 and randNum == randNum3 and randNum3 == randNum2:
                        messagebox.showinfo("GANASTE!", "Ganaste 100 creditos", parent = window)
                        creditsToPlay+=100
                    else:
                        if randNum == randNum2 or randNum == randNum3 or randNum2 == randNum3:
                            messagebox.showinfo("GANASTE!", "Ganaste 20 creditos", parent = window)
                            creditsToPlay += 20
                        else:
                            messagebox.showinfo("Perdiste :c", "Suerte para la proxima", parent = window)
                    toPrint = str(creditsToPlay)
                    Label(window, text="Creditos " + toPrint).grid(row=2, column=49)
            else:
                messagebox.showinfo("Creditos Insuficientes", "Tus creditos no son suficientes para jugar otra vez", parent = window)
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

def greedy_algorithm():
    global creditsToPlay

    if creditsToPlay == 0:
        messagebox.showwarning("No tienes fondos","Tu saldo es de 0")
    else:
        i = 4
        din20=False
        din10=False
        din5 =False
        din2 =False

        if dinero20.get() == 0:
            din20=True
        if dinero10.get() == 0:
            din10=True
        if dinero5.get() == 0:
            din5=True
        if dinero2.get() == 0:
            din2=True

        while creditsToPlay != 0:
            if din20 == True:
                if i == 4:
                    i = 3
                    din20 = False

            if din10 == True:
                if i == 3:
                    i = 2
                    din10 = False

            if din5 == True:
                if i==2:
                    i = 1
                    din5 = False
            if din2 == True:
                if i==1:
                    i = 0
                    din2 = False

            creditsToPlay -= cambio[i]
            if creditsToPlay < 0:
                creditsToPlay += cambio[i]
                i-=1
            else:
                if i == 4:
                    conteo[i] +=1
                else:
                    if i == 3:
                        conteo[i] +=1
                    else:
                        if i == 2:
                            conteo[i]+=1
                        else:
                            if i==1:
                                conteo[i] +=1
                            else:
                                if i == 0:
                                    conteo[i] +=1
        moneyToShow = ""
        j = 4
        while j >= 0:
            if j==4 and conteo[j] > 0:
                moneyToShow += "Billetes de 20 pesos: "
                moneyToShow += str(conteo[j])
                moneyToShow += "\n"
                conteo[j]=0
            if j==3 and conteo[j] > 0:
                moneyToShow += "Monedas de 10 pesos: "
                moneyToShow += str(conteo[j])
                moneyToShow += "\n"
                conteo[j] = 0
            if j==2 and conteo[j] > 0:
                moneyToShow += "Monedas de 5 pesos: "
                moneyToShow += str(conteo[j])
                moneyToShow += "\n"
                conteo[j] = 0
            if j==1 and conteo[j] > 0:
                moneyToShow += "Monedas de 2 pesos: "
                moneyToShow += str(conteo[j])
                moneyToShow += "\n"
                conteo[j] = 0
            if j==0 and conteo[j] > 0:
                moneyToShow += "Monedas de 1 peso: "
                moneyToShow += str(conteo[j])
                moneyToShow += "\n"
                conteo[j] = 0
            j -= 1

        messagebox._show("Dinero Entregado", moneyToShow)
    creditsToPlay = 0
    toPrint = str(creditsToPlay)
    Label(root, text="Creditos " + toPrint).grid(row=2, column=49)

def confirmation():
    reply = messagebox.askokcancel("¿Seguro?","Perdera todos sus creditos.")
    if reply:
        root.destroy()

#main
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

dinero20 = IntVar()
dinero20.set(True)
dinero10 = IntVar()
dinero10.set(True)
dinero5 = IntVar()
dinero5.set(True)
dinero2 = IntVar()
dinero2.set(True)

Checkbutton(root, variable = dinero20).grid(row = 20, column = 12)
Checkbutton(root, variable = dinero10).grid(row = 20, column = 10)
Checkbutton(root, variable = dinero5).grid(row = 20, column = 8)
Checkbutton(root, variable = dinero2).grid(row = 20, column = 6)

Label(root, text="20").grid(row = 21, column = 12)
Label(root, text="10").grid(row = 21, column = 10)
Label(root, text="5").grid(row = 21, column = 8)
Label(root, text="2").grid(row = 21, column = 6)

Button(root, text="Sacar dinero", command = greedy_algorithm).grid(row = 10, column = 2)

Button(root, text = "Salir", command = confirmation).grid(row =49, column = 48)

root.mainloop()
