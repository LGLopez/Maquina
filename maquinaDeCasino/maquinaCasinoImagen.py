# import tkinter as tk

# counter = 0


# def counter_label(label):
#    def count():
#        global counter
#        counter += 1
#        label.config(text=str(counter))
#        label.after(1, count)

#    count()


# root = tk.Tk()
# root.title("Counting Seconds")
# label = tk.Label(root, fg="green")

# label.pack()
# counter_label(label)
# button = tk.Button(root, text='Stop', width=25, command=root.destroy)
# button.pack()
# root.mainloop()

import random
import  time
from tkinter import *
from PIL import ImageTk, Image

counter = 0

def counter_label():
    start = time.time()
    img = ImageTk.PhotoImage(Image.open("michi1.png"))
    img2 = ImageTk.PhotoImage(Image.open("michi2.png"))
    img3 = ImageTk.PhotoImage(Image.open("michi3.png"))

    photos = [img, img2, img3]
    photos2 = [img2, img3, img]
    photos3 = [img3, img, img2]

    label = Label(root, image=photos[counter])
    label2 = Label(root, image=photos[counter])
    label3 = Label(root, image=photos[counter])

    label.grid(row=2, column=0)
    label2.grid(row=2, column=2)
    label3.grid(row=2, column=4)

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
            randNum = random.randint(0,2)
            randNum2 = random.randint(0,2)
            randNum3 = random.randint(0,2)

            label.config(image = photos[randNum])
            label2.config(image = photos2[randNum2])
            label3.config(image = photos3[randNum3])

    count()


root = Tk()

button1 = Button(root, text="Jugar", command=counter_label)

button1.grid(row=0, column=2)

root.mainloop()
