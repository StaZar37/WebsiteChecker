

# from tkinter import *
# def click(event):
#     W['bg'] = 'yellow'
#     btn['bg'] = 'red'
#     btn['text'] = 'Baton'

# W = Tk()
# W.geometry("480x320+200+200")
# btn=Button(text='bat', width = '22', command=click)
# btn.pack(pady=25)
# W.mainloop()


# from tkinter import *
# def click(event):
#     entry['bg'] = 'red'
#     entry['font'] = 'Arial 14'
#     entry['width'] += 6
#     entry['fg'] = 'white'
#     entry.delete(0, END)
#     entry.insert(0, 'Ми')

# root = Tk()
# root.geometry("480x320")


# entry = Entry(width='15', bd='3')
# entry.insert(0,'123')
# entry.pack(pady=30)
# button = Button()
# button.pack(pady=10)
# root.mainloop()


from tkinter import *

def click():
    W.configure(bg='yellow')
    btn.configure(bg='red')
    btn.configure(text='Baton')

W = Tk()
W.geometry("480x320+200+200")
btn = Button(text='bat', width='22', command=click)
btn.pack(pady=25)
W.mainloop()