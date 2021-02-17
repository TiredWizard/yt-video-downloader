from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import playlistdownload


# metodo che parte quando il pulsante viene premuto
def esegui():
    if audio_only.get() == 0:
        playlistdownload.download(inputlink.get(), inputdir.get())
    else:
        playlistdownload.download_audio_only(inputlink.get(), inputdir.get())
    errorlabel.configure(text='Download completato')


def selezionapath():
    directory = filedialog.askdirectory(initialdir='.')
    inputdir.insert(0, directory)


window = Tk()
window.geometry("400x200")
window.title("Youtube video downloader")

# --------------------Link------------------------
label_frame = LabelFrame(window)
label_frame.pack(expand='yes', fill='both')

# input Link
linklabel = Label(label_frame, text='Link')
linklabel.place(x=0, y=5)
inputlink = Entry(label_frame, width=30)
inputlink.place(x=100, y=5)

# directory path
dirlabel = Label(label_frame, text='Directory')
dirlabel.place(x=0, y=35)
inputdir = Entry(label_frame, width=30)
inputdir.place(x=100, y=35)
Button(label_frame, text='Scegli', command=selezionapath).place(x=300, y=33)
audio_only = IntVar()
c1 = Checkbutton(label_frame, text='Converti in audio', variable=audio_only, onvalue=1, offvalue=0)
c1.place(x=100, y=70)
# log label
errorlabel = Label(window, text='')
errorlabel.pack()

# pulsante di avvio
btn = Button(window, text='Esegui', command=esegui)
btn.pack()

window.mainloop()
