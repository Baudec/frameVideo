import cv2

# On importe Tkinter
from tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Salut les Zér0s !")

# On affiche le label dans la fenêtre
champ_label.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()

def break_into_frame(path):
    vidcap = cv2.VideoCapture('Compton.mp4')
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
        count += 1

