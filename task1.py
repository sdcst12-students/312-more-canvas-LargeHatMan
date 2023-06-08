import tkinter as tk
import itertools
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map1.txt')
rec = c.create_rectangle(25,25,40,40,fill="#800813")
fr=f.read()
fs=fr.split('\n')

path = []





for k in range(0,15):
        for (i,j) in itertools.zip_longest(fs[k],range(len(fs[k]))):
                if i =="*":
                        path.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#000000'))
                else:
                        pass







def move(e):
            if e.keysym == 'Left': 
                    x=-5
                    y=0
                    c.move(rec,x,y)
            if e.keysym == 'Up':
                    x=0
                    y=-5
                    c.move(rec,x,y)
            if e.keysym =="Down":
                    x=0
                    y=5
                    c.move(rec,x,y)
            if e.keysym == "Right":
                    x=5
                    y=0
                    c.move(rec,x,y)    
            print(e.keycode, e.keysym, e.x, e.y)
w.bind("<Left>",move)
w.bind("<Right>",move)
w.bind("<Up>",move)
w.bind("<Down>",move)

w.mainloop()