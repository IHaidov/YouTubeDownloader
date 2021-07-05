from tkinter import *
from pytube import YouTube



def _window():
    def Download():
        try:
            url = YouTube(str(link.get()))
            video = url.streams.first()
            video.download()
            Label(root, text='Downloaded', fg='green', font='arial 20 bold').place(x=160, y=140)
        except:
            print('',end='')

    root = Tk()
    root.geometry('500x200')
    root.resizable(0, 0)
    root.title('YouTube Downloader v.0.1')

    Label(root, text='YouTube video downloader', font='arial 20 bold').pack()
    link = StringVar()
    Label(root, text='Paste text here: ', font='arial 15 bold').pack()
    link_enter = Entry(root, width=70, textvariable=link).pack()

    Button(root, text='Download', font='arial 15 bold', bg='green', padx=6, command=Download).place(x=180, y=100)
    root.mainloop()


_window()
