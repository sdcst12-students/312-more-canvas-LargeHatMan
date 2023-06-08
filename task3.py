#!python3

# Find an image to use as a sprite from the Internet.
# Modify the image (flipping horizontally is a quick way to do that) so that you have
# a second, different image. Use the tkObject.after() method to animate it.
# Note: You can find sprite sheets or tile sheets on the internet to help you!

import tkinter as tk


tile=0


w = tk.Tk()
w.geometry("600x400")
w.title("sample")


c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()


img = tk.PhotoImage(file="assets/22904.png")
img2 = tk.PhotoImage(file="assets/229042.png")


rec = c.create_image(50,80,image=img)


def update():
    global tile
    ig = None
    tile +=1
    tile = tile%2
    if tile:
        ig = img2
    else:
        ig = img


    c.itemconfig(rec,image=ig)


def keyPress(e):


    if e.keysym == 'Left':
        if (c.coords(rec))[0] == 5:
            print('')
        else:
            print(e)
            x=-5
            y=0
            c.move(rec,x,y)
            print(c.coords(rec))
        update()
    if e.keysym == 'Right':
        if (c.coords(rec))[0] == 520:
            print('')
        else:
            print(e)
            x=5
            y=0
            c.move(rec,x,y)
            print(c.coords(rec))
        update()
    if e.keysym == 'Up':
        if (c.coords(rec))[1] == 5:
            print('')
        else:
            print(e)
            x=0
            y=-5
            c.move(rec,x,y)
            print(c.coords(rec))
        update()
    if e.keysym == 'Down':
        if (c.coords(rec))[1] == 365:
            print('')
        else:
            print(e)
            x=0
            y=5
            c.move(rec,x,y)
            print(c.coords(rec))
        update()


    print(e)
    print(e.keycode, e.keysym, e.x, e.y)
    
w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)


w.mainloop()