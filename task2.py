import tkinter as tk
import itertools as it
"""
Task 2
Read the map2.txt file and convert to a map that you can navigate a
rectangle object through. Use images for your map.
You will want to make sure that your rectangle is above the map tiles
Legend:
0 Water
1 Plains
2 Forest
3 Hills
4 Mountains
5 Swamp
6 City
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map2.txt')
read = f.read()
split=read.split("\n")
print(split)
water = tk.PhotoImage(file="assets/map.water.png")
img = c.create_image(200,200,image=water)
rec = c.create_rectangle(25,25,40,40,fill="#800813")
land = []

for k in range(0,11):
    for (i,j) in it.zip_longest(split[k],range(len(split[k]))):
        if i=='0':
            land.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#0000bb'))
        if i=='1':
            land.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#00ff00'))
        if i=='2':
            land.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#013220'))
        if i=='3':
            land.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#90ee90'))
        if i=='4':
            land.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#964b00'))
        if i=='5':
            land.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#005249'))
        if i=='6':
            land.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#808080'))
        else:
            pass




w.mainloop()