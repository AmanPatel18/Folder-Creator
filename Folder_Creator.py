import sys
import os
from tkinter import *
from Tkinter.custom_module import window_at_centre
win = Tk()
win.title('Folder Creator')
win.config(bg='black')
window_at_centre(win, 600, 430)
win.wm_attributes('-alpha', 0.8)


def create():
    path = path_entry.get()
    name = name_entry.get()
    num_of_folder = int(folder_num_entry.get())
    name = '//'+name
    path = path+name
    i = 1
    while i <= num_of_folder:
        os.mkdir(path+str(i))
        i = i+1


def delete():
    path = path_entry.get()
    name = name_entry.get()
    num_of_folder = int(folder_num_entry.get())
    name = '//'+name
    path = path+name
    i = 1
    while i <= num_of_folder:
        os.rmdir(path+str(i))
        i = i+1
def reset():
    path_entry.delete(0, END)
    name_entry.delete(0, END)
    folder_num_entry.delete(0, END)

def hover1(e):
    create_button.config(relief='raised', bg='gold')


def hover1_revert(e):
    create_button.config(relief='solid', bg='orange')


def hover2(e):
    delete_button.config(relief='raised', bg='gold')


def hover2_revert(e):
    delete_button.config(relief='solid', bg='orange')

def hover3(e):
    reset_button.config(relief='raised', bg='gold')

def hover3_revert(e):
    reset_button.config(relief='solid', bg='orange')


header = Label(win, text='Folder Creator', font=(
    'Times 30 bold'), fg='orange', bg='black')
header.place(x=170, y=20)

path_label = Label(win, text='Path', font=(
    'Helvetica 20 bold'), fg='orange', bg='black')
path_label.place(x=20, y=100)

path_entry = Entry(win, font=('Helvetica 20 bold'), bg='indigo', fg='white')
path_entry.place(x=280, y=100)

name_label = Label(win, text='Name', font=(
    'Helvetica 20 bold'), fg='orange', bg='black')
name_label.place(x=20, y=180)

name_entry = Entry(win, font=('Helvetica 20 bold'), bg='indigo', fg='white')
name_entry.place(x=280, y=180)

folder_num_label = Label(win, text='Number of Folders', font=(
    'Helvetica 20 bold'), fg='orange', bg='black')
folder_num_label.place(x=20, y=260)

folder_num_entry = Entry(win, font=(
    'Helvetica 20 bold'), bg='indigo', fg='white')
folder_num_entry.place(x=280, y=260)

create_button = Button(win, text='Create', font=(
    'Times 20 bold'), bg='orange', fg='indigo', width=8, command=create, relief='solid')
create_button.place(x=60, y=340)

delete_button = Button(win, text='Delete', font=('Times 20 bold'),
                       bg='orange', fg='indigo', width=8, command=delete, relief='solid')
delete_button.place(x=230, y=340)

reset_button = Button(win, text='Reset', font=('Times 20 bold'),
                      bg='orange', fg='indigo', width=8, command=reset, relief='solid')
reset_button.place(x=400, y=340)


# Binding buttons with events
create_button.bind('<Enter>', hover1)
create_button.bind('<Leave>', hover1_revert)
delete_button.bind('<Enter>', hover2)
delete_button.bind('<Leave>', hover2_revert)
reset_button.bind('<Enter>',hover3)
reset_button.bind('<Leave>', hover3_revert)


win.mainloop()
