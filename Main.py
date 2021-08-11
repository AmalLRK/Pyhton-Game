from File import *
from tkinter import *
from pin import *
import hashlib
from tkinter import messagebox
G_age = ''
G_lieu = ''
G_arme = ''
G_mobile = ''


def convertsha256(hash):
    encoded = hash.encode()
    result = hashlib.sha256(encoded)
    return result.hexdigest()

import tkinter as tk
level = 0
def checkAnswer(var):
    global level
    if level == 0:
        monAge(var)
    else :
        if level == 1:
            lieuDeCrime(var)
        else :
            if level == 2:
                armeDeCrime(var)
            else:
                if level == 3:
                    mobileDeCrime(var)
def initFormul():
    global window, entry
    # mettre à jour le niveau du jeu
    window.title("Jeu d'Assassin - Etape " + str(level + 1))
    #vider le texte et le label de reponse
    entry.delete(0, tk.END)
    entry.insert(0, "")
    label_reponse.configure(text="", font=("Arial,40"), bg='#FACEA1', fg='#ADD8E6')
    label_compteur.configure(text="", font=("Arial,40"), bg='#FACEA1', fg='#ADD8E6')

def Start():
    initFormul()
    window.configure(background='#FACEA1')
    canvas.itemconfig(canvas.create_image(0,0, anchor=NW, image=img), image=img2)
    label_title.config(text="\nSaisire un code PIN ",font=("Arial,50"), bg='#FACEA1', fg='black')
    # pour sauter la ligne
    label = Label(window, text='', bg='#FACEA1', fg='Black')
    label.pack()
    # code texte
    entry.pack()
    button.configure(text="Entrer", font=("Arial,40"), bg='white', fg='Black', command=lambda: checkAnswer(entry.get()))
    #button.place(x=310, y=380)
    button.place(relx=0.5, rely=0.9, anchor=CENTER)
    # pour sauter la ligne
    label = Label(window, text='', bg='#FACEA1', fg='#ADD8E6')
    label.pack()
    label_reponse.pack()
    label_compteur.pack()

###Fonction Age
def monAge(pin):
    result = checkPin(pin)
    initFormul()
    if(len(result)>2) :
        compteur = 10 - result[2]
        label_reponse.config(text="\n"+str(pin)+" : pas tout à fait correct. Mais tu as eu " +str(result[0]) +" chiffre(s) correct(s)!"
                                "\nPas tout à fait le nombre. Mais tu as eu "+str(result[1]) + " existe mais dans une autre position !"                            
                                , font=("Arial,40"), bg='#FACEA1', fg='red')
        label_compteur.config(text="Attention il vous reste " + str(compteur) + " tentative(s) !",
                              font=("Arial,40"),
                              bg='#FACEA1', fg='red')
    else :
        compteur = 10 - result[1]
        if (result[0] == 200) :
            label_title.config(text="\nGénial! Vous avez deviné le nombre ! Vous pouvez commencer le jeux")
            CreatMP3()
            global level
            level = 1

        else :
            if (result[0] == 100) :
                label_reponse.config(text="\n" + str(pin) + " : n'est pas un PIN à 4 chiffres !", font=("Arial,40"),
                                     bg='#FACEA1', fg='red')

            else :
                if (result[0] == 300) :
                   label_reponse.config(text="\n"+str(pin)+" : aucun des nombres de votre saisie ne correspond" ,font=("Arial,40"), bg='#FACEA1', fg='red')

            label_compteur.config(text="Attention il vous reste " + str(compteur) + " tentative(s) !",
                                         font=("Arial,40"),
                                         bg='#FACEA1', fg='red')

    if(compteur == 0) :
         messagebox.showinfo("Compteur remis à zéro","Vous n'avez pas réussi à déterminer le code pin\n un nouveau code pin sera régénéré")
         initFormul()
###Lieu De Crime
def lieuDeCrime(lieu):
    global G_age, G_lieu, G_arme, G_mobile
    print(G_age)
    G_lieu = lieu
    LieuSHA = convertsha256(lieu)
    if LieuSHA == 'b0dfed06855585ab08056ee1723bf653ca0bf783c47a762bbb922fb4bea3b736':
        label_title.config(text="\nBravo, Félicitation, vous avez trouvez LE 1er indice (Lieu De crime) !"
                                "\nMaintenant il faut trouvez le 2eme indice, et pour cela je vous genere un fichier pour vous aidez à trouvez l'arme de crime."
                                "\nBon courage et n'oublie pas de rester concentrer sur l'indice"
                                "\n")
        CreatExe()
        global level
        level = 2
        initFormul()
    else:
        label_reponse.configure(text="!!!! Erreur, il faut réessayer !!!!", font=("Arial,40"), bg='red', fg='white')

###Fonction Arme de Crime
def armeDeCrime(arme):
    global G_age, G_lieu, G_arme, G_mobile
    G_arme = arme
    ArmeSHA = convertsha256(arme)
    if ArmeSHA == '48ac267ffe8fa17db58a6d0e146416b60bbe6989631f497d93d1182aa8c867e6':
        label_title.config(text="\n\Bravo, Félicitation, vous avez trouvez LE 2 eme indice (Arme De Crime) !"
                                "\nMaintenant il faut trouvez le 3eme indice, et pour cela je vous genere un autre fichier pour vous aidez à trouvez le Mobile."
                                "\nBon courage et n'oublie pas de rester concentrer sur l'indice"
                                "\n")
        CreatPDF()
        global level
        level = 3
        initFormul()
    else:
        label_reponse.configure(text="!!!! Erreur, il faut réessayer !!!!", font=("Arial,40"), bg='red', fg='white')

###Fonction Mobile
def mobileDeCrime(mobile):
    global G_age, G_lieu, G_arme, G_mobile
    G_mobile = mobile
    MobileSHA = convertsha256(mobile)
    if MobileSHA == 'ea3d6cd6ba20db9099ec8015bc6960c5306573c54bfda756001f4d3768bef972':
        label_title.config(text="\n\Bravo, Félicitation, vous avez trouvez LE 3 eme indice (Mobile De Crime) !"
                                "\nle FLAG est :  >>>>>>>>>>>>>>>> \n")
        Flag = G_age + " " + G_lieu
        label_reponse.configure(text=Flag, font=("Arial,70"), bg='red', fg='white')

    else:
        label_reponse.configure(text="!!!! Erreur, il faut réessayer !!!!", font=("Arial,40"), bg='red', fg='white')

def centerWindow(windowName):
    # modifier la longueur et largeur de la fenetre principale
    MyLeftPos = (windowName.winfo_screenwidth() - 800) / 2
    myTopPos = (windowName.winfo_screenheight() - 500) / 2
    windowName.geometry("%dx%d+%d+%d" % (800, 500, MyLeftPos, myTopPos))


#pour l'affichage
window = Tk()
window.title("Jeu d'Assassin")
centerWindow(window)
window.config(background='white')

#image in tkinter

canvas = Canvas(window, width = 390, height = 195)
canvas.pack()
img2 = PhotoImage(file="Bag.png")
img = PhotoImage(file="Gang.png")
canvas.create_image(0,0, anchor=NW, image=img)

#pour l'icon
window.iconbitmap('PINKY.ico')

label_title = Label(window, text="\nBienvenue sur l'application"
                                 "\nRegle de jeux......"
                                 "\nBLABLA BLABLA BKA"
                                 "\nBLABLABLABLABLA"
                                 , font=("Arial,50"), bg='white', fg='black')
label_title.pack()

# code texte
entry = Entry(window, font=("Arial,40"), bg='white', fg='Black')

#code button enter
button=Button(window, text="START" , font=("Arial,40"), bg='white', fg='Black', command=lambda : Start())
button.pack()
button.place(relx=0.5, rely=0.9, anchor=CENTER)

# code label de reponse
label_reponse = Label(window, text="", font=("Arial,40"), bg='#FACEA1', fg='black')

# code label de compteur
label_compteur = Label(window, text="", font=("Arial,40"), bg='#FACEA1', fg='black')

#window.bind('<Return>', checkAnswer(entry.get()))
window.mainloop()