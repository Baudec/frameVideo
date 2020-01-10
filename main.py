import cv2

# On importe Tkinter
from tkinter import *
from tkinter import filedialog


# On crée une fenêtre, racine de notre interface
fenetre = Tk()
Tk.filename =  filedialog.askopenfilename(initialdir = "/home/conrad/Downloads",title = "Select file",filetypes = (("jpeg files","*.*"),("all files","*.*")))


# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre

break_into_frame(Tk.filename)

