# -*- coding: utf-8 -*-
"""
Programme Snake

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 
from random import randint
from tkinter import font as tkfont

# On crée un environnement Tkinter
tk = Tk()

def right(event):
    # Modification de la variable globale direction
    global direction
    direction = 'right'
    
def left(event):
    # Modification de la variable globale direction
    global direction
    direction = 'left'
    
def down(event):
    # Modification de la variable globale direction
    global direction
    direction = 'down'
    
def up(event):
    # Modification de la variable globale direction
    global direction
    direction = 'up'

# Calcule la nouvelle frame de jeu
def computeNextFrame(numFrame,coordonnee, pomme_verte, pomme_rouge):
    global direction
    # Affiche le numérod de la frame
    #print(numFrame)
    numFrame = numFrame + 1
    
    # Effacer le canevas
    can.delete('all')
    if len(coordonnee) > 0:    
        # Propagation du déplacement des noeuds
        for n in range (len(coordonnee)-1,0,-1):
            coordonnee[n][0] = coordonnee[n-1][0]
            coordonnee[n][1] = coordonnee[n-1][1]
            
        # Mise à jour des coordonnées
        if direction == 'right':
            coordonnee[0][0] += 20
            if coordonnee[0][0] > 480:
                coordonnee[0][0] = 0
        if direction == 'left':
            coordonnee[0][0] += -20
            if coordonnee[0][0] < 0:
                coordonnee[0][0] = 480
        if direction == 'up':
            coordonnee[0][1] += -20
            if coordonnee[0][1] < 0:
                coordonnee[0][1] = 480
        if direction == 'down':
            coordonnee[0][1] += 20
            if coordonnee[0][1] > 480:
                coordonnee[0][1] = 0

        # Dessin de la tête du serpent et de noeuds
        can.create_oval(coordonnee[0][0], coordonnee[0][1], coordonnee[0][0] + 20, 
                             coordonnee[0][1] + 20, outline='yellow', fill='red')
        
        for n in range(1,len(coordonnee)):
            if n%2 == 0: 
                ligne = 'blue'
                couleur = 'green'
            else:
                ligne = 'green'
                couleur = 'blue'
            can.create_oval(coordonnee[n][0], coordonnee[n][1], coordonnee[n][0] + 20, 
                             coordonnee[n][1] + 20, outline= ligne, fill= couleur) 
            
        for p in range(len(pomme_verte)):
            if coordonnee[0][0] == pomme_verte[p][0] and coordonnee[0][1] == pomme_verte[p][1]:
                # Déplacement de la pomme
                pomme_verte[p][0] = randint(1,24)* 20
                pomme_verte[p][1] = randint(1,24)* 20
                # Ajout d'un noeud au serpent (à la même place que le dernier noeud)
                coordonnee.append([-20, -20]) # Caché pour l'instant
                x = randint(1, 24)
                y = randint(1, 24)
                pomme_rouge.append([x*20, y*20, 1])
            
        for p in range(len(pomme_rouge)):
            if coordonnee[0][0] == pomme_rouge[p][0] and coordonnee[0][1] == pomme_rouge[p][1]:
                # Déplacement de la pomme rouge
                pomme_rouge[p][0] = randint(1, 24)* 20
                pomme_rouge[p][1] = randint(1, 24)* 20
                # Enlève un noeud au serpent
                coordonnee.pop()
    # Dessine les objets
    for p in range(len(pomme_verte)):
        can.create_oval(pomme_verte[p][0], pomme_verte[p][1], pomme_verte[p][0] + 20, 
                         pomme_verte[p][1] + 20, outline= 'red', fill= 'green') # Pomme verte
        
    for p in range(len(pomme_rouge)):
        can.create_oval(pomme_rouge[p][0], pomme_rouge[p][1], pomme_rouge[p][0] + 20, 
                         pomme_rouge[p][1] + 20, outline= 'green', fill= 'red') # Pomme rouge
            
    game_over = False
    # On teste la position de la tête par rapport aux noeuds du serpent
    for n in range(1, len(coordonnee)): #L'indice 0 est exclu, c'est la tête
        if coordonnee[0][0] == coordonnee [n][0] and coordonnee [0][1] == coordonnee [n][1]:
            game_over = True # Rest in pepperoni
        
            
            
    if game_over :
        # Fin de partie
        TEXTE = "GAME OVER"
        normal_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        can.create_text(100,200,text = TEXTE, fill='red', font=normal_font)
    else:
        # La partie n'est pas finie
        # Calcule une nouvelle frame dans 100 ms
        tk.after(100, lambda:computeNextFrame(numFrame,coordonnee, pomme_verte, pomme_rouge))


if __name__ == "__main__":
    # On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
    # Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
    # intégré (ici l'environnement Tkinter)
    # Les trois autres paramètres permettent de spécifier la taille et la couleur
    # de fond du canevas
    can = Canvas(tk, width=500, height=500, bg='black')
    
    # On affiche le canevas
    can.pack()
    
    # Direction par défaut
    direction = 'up' 
    
    coordonnee = [ [200, 200], [200, 220], [200, 240], [220, 240] ]
    # Premier objet (la pomme)
    pomme_verte = []
    x = randint(1,24)
    y = randint(1,24)
    pomme_verte.append([x*20, y*20, 0])
    # Deuxième objet (la pomme rouge)
    pomme_rouge = []
    
    
    
    # Construction de la première étape de simulation
    computeNextFrame(0,coordonnee, pomme_verte, pomme_rouge)
    
    # Appuyer sur la touche 'd' appellera la fonction right()
    tk.bind('<d>', right) 
    tk.bind('<q>', left) 
    tk.bind('<s>', down) 
    tk.bind('<z>', up) 
    
    # lancement de la boucle principale qui écoute les évènements (claviers...)
    tk.mainloop() # Cet appel doit être la derniere instruction du programme
