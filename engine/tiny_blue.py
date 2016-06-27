from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
image_path = "C:/Users/Ian/Desktop/tiny_blue/assets/test_box.bmp"
button_image = ImageTk.PhotoImage(Image.open(image_path))

def callback(arg="HI"):
    print (arg + str(random.random()))

# create a toolbar
toolbar = Frame(root)
'''
b = Button(toolbar, image=button_image, width=16, height=16, command=callback)
b.pack()

b = Button(toolbar, image=button_image, width=16, height=16, command=callback)
b.pack()
'''

Button(toolbar, image=button_image, width=16, height=16, command=lambda: callback("Moon")).grid(row=0, sticky=W)
Label(toolbar, text="Second").grid(row=1, sticky=W)

e1 = Entry(toolbar)
e2 = Entry(toolbar)

e1.grid(row=0, column=2)
e2.grid(row=1, column=1)
#button1.grid(row=2, column=2)


toolbar.pack(side=TOP, fill=X)

mainloop()



'''
class App:

    def __init__(self, master):

        frame = Frame(master, width=100, height=100)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", bg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print ("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()
#root.destroy() # optional; see description below
'''