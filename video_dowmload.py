import os
from tkinter import *
root = Tk()
root.geometry('370x150')
def runit():
    os.startfile('link.bat')
def downloadytv():
    with open('link.bat', 'w') as down_load:
        down_load.write(f'youtube-dl {link.get()}')
        down_load.close()
    runit()
f = Frame(root)
f.grid()
Label(f,text='====Youtube Video Downloader====', font=15,padx=6).pack()

f1 = Frame(root)
f1.grid()
Label(f1,text='Enter link Here', font=5).grid(row=1)

link = StringVar()

Entry(f1,font=5,textvariable=link).grid(row=1,column=1,pady=5,padx=10)

work = Button(root, text='Download', width=15, height=2,font=10,borderwidth=5,
command=downloadytv).place(x=120, y=60)
# download = Button(f1,text='Download',padx=50,relief=RAISED,font=10,borderwidth=5,command=downloadytv).place(x=40, y=50)
#.place(x=20,y=50)



# Button.grid(column=1,pady=5)

root.mainloop()
