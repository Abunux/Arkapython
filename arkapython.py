#!/usr/bin/env python
# -*- coding:Utf-8 -*-

###############################################################################
##                                                                            #
##   /\                                                                       #
##  /! \    Nécessite d'installer python-xlib et python-tk                    #
## -----                                                                      #
##                                                                            #
###############################################################################
txt_version='''
###############################################################################
##                                                                            #
##                          -----------------------                           #
##                          | Arkapython v0.3.1.2 |                           #
##                          -----------------------                           #
##                                                                            #
###############################################################################
##                                                                            #
## Créateur : Abu (Frédéric Muller)                                           #
## Miel : abunux de chez la google boite du com                               #
##                                                                            #
## Nom du fichier : arkapython_v0.3.1.2.py                                    #
##                                                                            #
## Suivi du projet : http://forum.ubuntu-fr.org/viewtopic.php?id=217662       #
##                                                                            #
## Date : 23/05/2008                                                          #
## Projet démarré le 08/05/2008                                               #
##                                                                            #
## Description :                                                              #
##       Un petit casse-briques sans prétention en Python                     #
##       (mais qui commence à ressembler à quelque chose...)                  #
##                                                                            #
###############################################################################
##                                                                            #
##  Commandes :                                                               #
##  -----------                                                               #
##      - Boutton gauche : Lance la balle ou met en pause                     #
##      - Boutton droite : Libère la souris et met en pause                   #
##      - Esc : Quitter                                                       #
##      - Ctrl+w : Cheat. Avance d'un niveau et donne 10 vies (pour les tests)#
##                                                                            #
###############################################################################
##                                                                            #
##    Dernière maj v0.3.1.2 :                                                 #
##    ----------------------                                                  #
##      -                                                                     #
##                                                                            #
###############################################################################
##                                                                            #
##    A faire :                                                               #
##   ----------                                                               #
##                                                                            #
##      Au niveau du jeu :                                                    #
##      ------------------                                                    #
##        - Améliorer l'algo de détection (encore trop lourd)                 #
##        - Mettre un chronomètre et améliorer le système de scores           #
##        - Réfléchir à des bonus sur les briques                             #
##        - Revoir le gameplay (vies, réglages vitesse de la balle...)        #
##        - Créer quelques niveaux supplémentaires                            #
##                                                                            #
##      Au niveau du code :                                                   #
##      -------------------                                                   #
##        - Mettre de l'ordre dans la classe Application                      #
##        (créer d'autre classes : Interface, Souris, Tableau, Jeu, Player...)#
##        - Revoir la façon de coder les tableaux (nouvelle classe)           #
##          Et la définire proprement en vue de stockage en fichiers XML      #
##        - En fait repenser presque toutes les classes...                    #
##                                                                            #
##      Au niveau de l'interface :                                            #
##      --------------------------                                            #
##        - Faire un écran d'acceuil avant de lancer la partie                #
##        - Réglage des paramètres (en cours)                                 #
##        - Mettre des sons, voire une musique                                #
##                                                                            #
##      Divers :                                                              #
##      --------                                                              #
##        - Apprendre rapido le XML :-P pour voir les possibilités            #
##        - Réfléchir à un éditeur de niveaux                                 #
##                                                                            #
##      --> Future version v0.4 (doit avoir au minimum) :                     #
##      -------------------------------------------------                     #
##        - Classes remaniées                                                 #
##        - Niveaux stockés dans un fichier                                   #
##        - Menus et scores                                                   #
##                                                                            #
###############################################################################
##                                                                            #
##    Maj v0.3.1.1 :                                                          #
##    --------------                                                          #
##      - Ajout de la fenêtre "Code source"                                   #
##      - Modification de la fenêtre "perdu"                                  #
##      - Correction d'un bug sur la vitesse de la balle                      #
##      - Correction d'un bug sur les fenêtres                                #
##      - Modification du calcul du score (encore pas top)                    #
##      - Préparation de la fenêtre préférences                               #
##        Les préférences sont stockées dans un fichier 'config.ini'          #
##        qui est crée automatiquement s'il n'existe pas                      #
##        Il me reste à les définir et les appliquer au jeu                   #
##      - Ajout des high-scores (à fignoler, notamment pour le nom du joueur) #
##        Les high scores sont stockés dans un fichier 'highscore' en csv     #
##        qui est crée automatiquement s'il n'existe pas                      #
##                                                                            #
##    Maj v0.3.1.0 :                                                          #
##    --------------                                                          #
##      - Création de la classe Fenetre pour l'interface                      #
##        et de la classe Souris (à finir)                                    #
##      - Ajout d'une barre de menu                                           #
##      - Ajout des fenêtres "Aide" et "A propos"                             #
##      - Ajout d'une boite de dialogue quand on a perdu                      #
##      - Refonte rapide de l'interface                                       #
##      - Score minimaliste                                                   #
##                                                                            #
##    Maj v0.3.0.4 :                                                          #
##    --------------                                                          #
##      - Amélioration des collisions avec les coins :                        #
##        Correction d'un bug dans les collisions  :                          #
##           Des fois (rarement) la balle traverse une brique                 #
##           J'espère que ça va maintenant (ça devrait)                       #
##      - Optimisation des tests de collisions : On ne teste que si la balle  #
##        est dans le "rectangle" des briques. Y a moyen d'améliorer.         #
##      - Ajout d'une légère accélération à chaque rebond                     #
##      - Petit changement dans la gestion des lv                             #
##      - Petits changements dans le positionnement des objets                #
##                                                                            #
##    Maj v0.3.0.3 :                                                          #
##   ---------------                                                          #
##      - Tests de collisions de la balle avec les coins des briques          #
##        Marche nikel :)                                                     #
##      - Rebonds de la balle symétriques sur les bords et les briques        #
##        (correction d'un bug)                                               #
##      - Message d'erreur si les bibliothèques ne sont pas chargées          #
##        (merci snapshot)                                                    #
##                                                                            #
##    Maj v0.3.0.2 :                                                          #
##    --------------                                                          #
##      - Changement du comportement de la balle                              #
##        Rebonds symétriques sur els bords et les briques                    #
##        et qui dépend de la position de la balle sur la raquette            #
##      - Correction léger bug sur l'augmentation des vies par lv             #
##                                                                            #
##    Maj v0.3.0.1 :                                                          #
##   ---------------                                                          #
##      - Ajout d'une brique invisible, et d'une indestructible               #
##      - Infos qui s'affichent sur le canevas (pas top encore, mais marche)  #
##      - Changement du comportement de la balle (vitessse, accélération...)  #
##      - Petits changements mineurs dans le code  (nettoyage)                #
##      - Maj de choses à faire et des commentaires                           #
##                                                                            #
##    Maj v0.3 :                                                              #
##   -----------                                                              #
##      - Pointeur de la souris invisible. Là c'est un casse-briques :))      #
##                                                                            #
##    Maj v0.2.5 :                                                            #
##   -------------                                                            #
##      - Amélioration de le gestion de la souris                             #
##        C'est nikel, plus qu'à rendre le curseur invisible                  #
##      - Changement de nom (je pensais que arkapython existait déjà :P)      #
##                                                                            #
##    Maj v0.2.4 :                                                            #
##   -------------                                                            #
##      - Gestion de la souris                                                #
##                                                                            #
##    Maj v0.2 :                                                              #
##    ----------                                                              #
##      - Implantation de la classe Brique-> Gros progrès                     #
##      - Changement de la façon dont sont crées les niveaux                  #
##          Maintenant ils sont personnalisables et créés dans une matrice    #
##      - Graphisme old school à la pong :-P                                  #
##      - Changement du comportement de la balle (un peu de random)           #
##                                                                            #
###############################################################################
##                                                                            #
## Merci à la communauté de ubuntu-fr pour ses encouragements                 #
## Merci également à Gérard Swinnen pour son excellent cours                  #
##      "Apprendre à programmer avec Python"                                  #
##      Dispo librement ici : http://www.ulg.ac.be/cifen/inforef/swi          #
##                                                                            #
##  Vous pouvez bien sûr tout réutiliser absolument comme vous voulez :-)     #
##  Je roule en GPL (le gasoil c'est pas écolo...)                            #
##  Je pense qu'on peut facilement récupérer les classes Raquette et Balle    #
##  pour faire un pong ^_^ (voire un pong en réseau ,  troooop bien !!)       #
##                                                                            #
##  Enjoy ;-)                                                                 #
##                                                                            #
## PS: Python c'est vraiment trop bien :)                                     #
##                                                                            #
###############################################################################
'''

## Importation des modules

import sys
try:
	from Tkinter import Tk, Canvas, Label, Button, Frame, Menu, Toplevel, Text, END, Entry, StringVar
	from ScrolledText import ScrolledText
##    from Tkinter import *
	import Xlib.display
except ImportError:
	print >>sys.stderr, "Vous devez installer les package python-xlib et python-tk pour utiliser ce jeu : "
	print >>sys.stderr, "sudo apt-get install python-xlib python-tk"
	sys.exit(3)

from random import randrange, uniform
import os
from math import sqrt,hypot
import ConfigParser
import csv
import time

## Création d'un curseur invisible
kNullCursorData="""
  #define t_cur_width 1
  #define t_cur_height 1
  #define t_cur_x_hot 0
  #define t_cur_y_hot 0
  static unsigned char t_cur_bits[] = { 0x00};
  """


## Création des classes

class Raquette:
	""" Classe de définition de la raquette"""
	def __init__(self , canevas , x , y , larg = 50 , haut = 30):
		"""Initialisation de la raquette"""
		self.canevas  =  canevas
		self.xmax = int(canevas.cget('width'))  ## Récupération des dimensions
		self.ymax = int(canevas.cget('height')) ## du canevasas
		## Coordonnées initiales
		self.xdef = x
		self.ydef = y
		## Coordonnées actuelles
		self.x = x
		self.y = y
		## Dimensions
		self.larg = larg
		self.haut = haut
		## Coordonnées absolue du centre (pour placer la souris)
		self.majcoordabs()
		## Dessin
		self.graph = canevas.create_rectangle(self.x-self.larg , self.y , \
			self.x+self.larg , self.y+self.haut , width = 2 , fill = 'white')

	def __del__(self):
		"""Destruction de la raquette : On l'efface"""
		self.canevas.delete(self.graph)

	def redraw(self):
		"""Redessine la raquette à la nouvelle position"""
		self.canevas.coords(self.graph , self.x-self.larg , self.y , \
			self.x+self.larg , self.y+self.haut)

	def deplace(self , delta):
		"""Déplace la raquette de delta.
			Renvoie True si le déplacement est possible"""
		if (self.x-self.larg > -delta) and (self.x+self.larg < self.xmax-delta):
			self.x = self.x+delta
			self.majcoordabs()
			self.redraw()
			return True
		else:
			return False

	def majcoordabs(self):
		"""Calcul les coordonnées absolues du centre de la raquette"""
		self.xabs = self.canevas.winfo_rootx()+self.x
		self.yabs = self.canevas.winfo_rooty()+self.y+self.haut/2



class Balle:
	"""Classe de définition de la balle"""
	def __init__(self , canevas , x , y , rayon =15 , vitesse = 1.2):
		"""Initialisation de la balle"""
		self.canevas = canevas

		## rayon
		self.rayon = rayon

		## Coordonnées initiales
		self.xdef = x
		self.ydef = y
		## Coordonnées actuelles
		self.x = x
		self.y = y
		## Vitesse (nombre de pixels à chaque déplacement) et accélération
		self.vitesse_init = vitesse  ## Vitesse de base
		self.vitesse_lv = vitesse    ## Vitesse de départ dans le lv
		self.vitesse = vitesse       ## Vitesse courante
		self.vitesse_max = 3
		self.acceler_brique = 0.001      ## Accélération quand on touche une brique
		self.acceler_lv = 0.05       ## Accélération quand on change de lv
		## Direction
		self.dirx = 1
		self.diry = -1
		self.normalise()            ## AVoir un vecteur vitesse de norme 1
		## Dessin
		self.graph = canevas.create_oval(self.x-self.rayon , self.y+self.rayon , \
			self.x+self.rayon , self.y-self.rayon , width = 2 , fill = 'white')

	def __del__(self):
		"""Destruction de la balle : On l'efface"""
		self.canevas.delete(self.graph)

	def redraw(self):
		"""Redessine la balle à la nouvelle position"""
		self.canevas.coords(self.graph , self.x-self.rayon , \
			self.y-self.rayon , self.x+self.rayon , self.y+self.rayon)

	def deplace(self):
		""" Déplace la balle de v dans la direction (dirx , diry)"""
		self.x += self.dirx*self.vitesse
		self.y += self.diry*self.vitesse
		self.redraw()


	## Tests de Collisions
	## -------------------
	## Principe :
	##      On regarde pour chaque "point cardinal" de la balle
	##      s'il est dans un rectangle de test et si sa direction
	##      est cohérente avec ce rectangle
	##      Si oui ,  on change la direction de la balle
	##      et éventuellement on l'accélère
	##      On test également si la balle touche un coin

	def normalise(self):
		"""Normalise le vecteur direction """
		hypo=hypot(self.dirx,self.diry)
		if hypo != 0:
			self.dirx=self.dirx/hypo
			self.diry=self.diry/hypo

	def accelere(self) :
		"""Accélération à chaque contact"""
		self.vitesse += self.acceler_brique

	def changedir(self,u,v):
		"""Change la direction de la balle suivant le vecteur (u,v)
		   de norme 1"""
		self.dirx = u
		self.diry = v
		self.normalise()
		self.accelere()

	def test_haut(self , xa , ya , xb , yb):
		""" Test si la balle a un contact au dessus"""
		if ((xa <= self.x <= xb)&(ya <= self.y-self.rayon <= yb)) and self.diry<0:
			self.changedir(self.dirx,abs(self.diry))
			return True
		else:
			return False

	def test_bas(self , xa , ya , xb , yb):
		""" Test si la balle a un contact en dessous"""
		if (xa <= self.x <= xb)&(ya <= self.y+self.rayon <= yb) and self.diry>0 :
			self.changedir(self.dirx,-abs(self.diry))
			return True
		else:
			return False

	def test_gauche(self , xa , ya , xb , yb):
		""" Test si la balle a un contact à sa gauche"""
		if (xa <= self.x-self.rayon <= xb)&(ya <= self.y <= yb) and self.dirx<0 :
			self.changedir(abs(self.dirx),self.diry)
			return True
		else:
			return False

	def test_droite(self , xa , ya , xb , yb):
		""" Test si la balle a un contact à sa droite"""
		if (xa <= self.x+self.rayon <= xb)&(ya <= self.y <= yb)  and self.dirx>0:
			self.changedir(-abs(self.dirx),self.diry)
			return True
		else:
			return False

	def test_coins(self , xa , ya , xb , yb):
		"""Test si la balle touche un coin du rectangle (xa,ya,xb,yb)"""
		## Principe :
		## ----------
		## La balle est découpé en 8 secteurs d'angles pi/4,
		## et on test si les coins de la bique sont dans ces quartiers
		##
		## Récupération des paramètres de la balle pour alléger les notations
		x=self.x        ## (x,y) : Coordonnées du centre de la balle
		y=-self.y       ## Passage dans un repère "normal"
		ya,yb=-ya,-yb   ## ie avec l'axe des ordonnées vers le haut
		r=self.rayon    ## (beaucoup plus pratique pour moi....)
		r2=r*sqrt(2)/2  ## r2=r*cos(pi/4)=r*sin(pi/4)

		## Coins au dessus de la balle
		if        ( ((0 <= xa-x <= r*sqrt(2)/2) and (r*sqrt(2)/2 <= yb-y <= r)) \
				or  ((-r*sqrt(2)/2 <= xb-x <= 0) and (r*sqrt(2)/2 <= yb-y <= r)) \
				or ( (yb-y>=xa-x)    and (0<=yb-y<=r2) and (0<=xa-x<=r2))\
				or ( (yb-y>=-(xb-x)) and (0<=yb-y<=r2) and (0<=xb-x<=r2)) )\
				and self.diry<0 :
			self.changedir(self.dirx, abs(self.diry))
			return True

		## Coins en dessous de la balle
		elif      ( ((0 <= xa-x <= r*sqrt(2)/2) and (-r <= ya-y <= -r*sqrt(2)/2)) \
				or  ((-r*sqrt(2)/2 <= xb-x <= 0) and (-r <= ya-y <= -r*sqrt(2)/2)) \
				or ( (ya-y<=-(xa-x)) and (0>=ya-y>=-r2) and (0<=xa-x<=r2))\
				or ( (ya-y<=xb-x)    and (0>=ya-y>=-r2) and (0>=xb-x>=-r2)) )\
				and self.diry>0 :
			self.changedir(self.dirx, -abs(self.diry))
			return True

		## Coins à gauche de la balle
		elif      ( ((-r <= xb-x <= -r*sqrt(2)/2) and (0 <= yb-y <= r*sqrt(2)/2)) \
				or  ((-r <= xb-x <= -r*sqrt(2)/2) and (-r*sqrt(2)/2) <= ya-y <= 0) \
				or ( (yb-y<=-(xb-x)) and (0<=yb-y<=r2)  and (-r2<=xb-x<=0))\
				or ( (ya-y>=-(xb-x)) and (-r2<=ya-y<=0) and (-r2<=xb-x<=0)) )\
				and self.dirx<0 :
			self.changedir(abs(self.dirx), self.diry)
			return True

		## Coins à droite de la balle
		elif      ( ((r*sqrt(2)/2 <= xa-x <= r) and (0 <= yb-y <= r*sqrt(2)/2)) \
				or ((r*sqrt(2)/2 <= xa-x <= r) and (-r*sqrt(2)/2) <= ya-y <= 0)\
				or ( (yb-y<=xa-x) and (0<=yb-y<=r2) and(0<=xa-x<=r2))\
				or ( (ya-y>=-(xa-x)) and (0>=ya-y>=-r2) and(0<=xa-x<=r2)) )\
				and self.dirx>0 :
			self.changedir(-abs(self.dirx),self.diry)
			return True
		else:
			return False

	def test_raquette_bas(self,xa,ya,xb,yb):
		""" Test si la balle a un contact avec la raquette en dessous
			Idem test_bas + coin bas sauf pas de changement de direction
			qui se fait dans le prog principal
			(besoin des coordonnées de la balle)"""
		if       ( (xa <= self.x <= xb)&(ya <= self.y+self.rayon <= yb) \
				or ( ((0 <= xa-self.x <= self.rayon) and (-self.rayon <= self.y-ya <= 0 )) \
				or  ((-self.rayon <= xb-self.x <= 0) and (-self.rayon <= self.y-ya <= 0 )) ) )\
				and self.diry>0 :
			return True
		else:
			return False

class Brique:
	"""Classe de définition des briques"""
	def __init__(self , canevas , xa , ya , xb , yb , statut = 1 ):
		"""Initialisation d'une brique"""
		self.canevas = canevas

		## Coordonnées
		self.xa = xa
		self.ya = ya
		self.xb = xb
		self.yb = yb

		## Statut (nombre de coup pour la détruire)
		self.statut = statut

		## Couleur en fonction du statut
		## La dernière est celle de la brique incassable (statut = -1)
		## L'avnt dernière est celle de la brique invisible (noire)
		self.liste_couleurs = ['green' , 'yellow' , 'red' , 'black','grey']
		if self.statut > 0 :
			self.couleur = self.liste_couleurs[(self.statut-1)%len(self.liste_couleurs)]
		elif self.statut == -1:
			self.couleur = self.liste_couleurs[-1]

		## Dessin
		if self.statut != 0 :
			self.graph = self.canevas.create_rectangle(xa , ya , xb , yb , \
				width=2 , fill = self.couleur)
			self.canevas.lower(self.graph)


	def __del__(self):
		"""Destructeur des briques : On l'efface si elle est là"""
		if self.statut > 0 :
			self.canevas.delete(self.graph)

	def redraw(self):
		"""Redessine la brique"""
		self.canevas.coords(self.xa , self.ya , self.xb , self.yb)

	def changestatut(self,statut):
		"""Quand on touche une brique, on change son statut (ici, sa couleur)"""
		self.statut = statut
		self.couleur = \
			self.liste_couleurs[(self.statut-1)%len(self.liste_couleurs)]
		self.canevas.itemconfigure(self.graph,fill = self.couleur)


class Niveau:
	"""Classe de définition des niveaux"""
	def __init__(self , appli , lv = 1 ):
		"""Initialisation du niveau"""
		self.appli=appli
		self.canevas = appli.main.canevas
		self.xmax = int(self.canevas.cget('width'))
		self.ymax = int(self.canevas.cget('height'))

		self.top = 50    ## Hauteur de la 1ère ligne
		self.left = 0    ## Position de la 1ère colonne (marge gauche/droite)

		## Récupération du numéro du lv
		self.lv = lv

		self.definir_level()

	def definir_level(self):
		## Liste des briques du niveau
		self.liste_briques = []

		## serie : Serie de niveaux:
		## serie = 0 : Niveaux codés dans les matrices
		## serie = 1 : Rectangles
		## serie = 2 : Niveaux aléatoires
		self.serie = 0

		## La liste suivante code tous les niveaux de la série 0
		## C'est une liste de matrices
		## dont chaque terme donne le statut de la brique
		listelv = [ \
##					[ [0,1000,0] ],
##				   [ [-1,-1,-1], \
##					 [-1, 1,-1], \
##					 [-1,-1,-1] ], \
##				   [ [ 3, 0, 3, 0, 3, 0, 3],   \
##					 [ 0, 3, 0, 3, 0, 3, 0],   \
##					 [ 3, 0, 3, 0, 3, 0, 3],   \
##					 [ 0, 3, 0, 3, 0, 3, 0],   \
##					 [ 3, 0, 3, 0, 3, 0, 3],   \
##					 [ 0, 3, 0, 3, 0, 3, 0] ], \

				   [ [-1, 2, 3, 2, 3, 2,-1],   \
					 [ 2, 1, 2, 1, 2, 1, 2],   \
					 [ 4, 4, 4, 4, 4, 4, 4],   \
					 [ 2, 1, 2, 1, 2, 1, 2],   \
					 [ 3, 2, 3, 2, 3, 2, 3] ], \

				   [ [1,0,0,0,0,1],   \
					 [0,3,1,1,3,0],   \
					 [0,1,1,1,1,0],   \
					 [1,1,2,2,1,1],
					 [0,1,0,0,1,0],
					 [1,0,0,0,0,1] ], \

##				   [ [ 0, 0,-1,-1,-1, 0, 0],   \
##					 [ 0,-1, 1, 3, 1,-1, 0],   \
##					 [-1, 2, 3, 4, 3, 2,-1],   \
##					 [-1, 3, 1, 3, 1, 3,-1],   \
##					 [ 0,-1, 4, 4, 4,-1, 0],   \
##					 [ 0,-1, 4, 4, 4,-1, 0] ], \

				   [ [1,1,1,1,1,1,1],  \
					 [1,2,2,1,2,2,1],  \
					 [1,2,2,1,2,2,1],  \
					 [1,1,1,1,1,1,1],  \
					 [1,1,1,1,1,1,1],  \
					 [1,3,1,1,1,3,1],  \
					 [1,1,3,3,3,1,1],  \
					 [1,1,1,1,1,1,1]], \

				   [ [0,3,3,0,0,3,3,3,3,0,3,0,0,3],  \
					 [3,0,0,3,0,3,0,0,3,0,3,0,0,3],  \
					 [3,3,3,3,0,3,3,3,0,0,3,0,0,3],  \
					 [3,0,0,3,0,3,0,0,3,0,3,0,0,3],  \
					 [3,0,0,3,0,3,3,3,3,0,3,3,3,3] ] \
				]

		self.nblv = len(listelv) ## Nombre de niveaux codés

		## Série 1 : 3 niveaux classiques rectangulaires
		if self.nblv < self.lv <= self.nblv+4 :
			self.serie = 1
			s = self.lv-self.nblv
			listelv = [[]]
			for i in range(5):
				listelv[0].append([s,s,s,s,s,s])


		## Série 2 : Niveaux aléatoires
		if self.lv > self.nblv+4 :
			self.serie = 2
			listelv = [[]]
			for i in range(5):
				ligne = []
				for j in range(6):
					ligne.append(randrange(5))
				listelv[0].append(ligne)

		## Création du level
		if self.serie == 0 :
			self.creer_level( listelv[ (self.lv-1) ] )
		else:
			self.creer_level( listelv[0] )

	def __del__(self):
		""" Destructeur : On efface toutes les briques restantes"""

		## Astuce pour parcourir les briques restantes :
		## Partir de la fin de la liste, vu qu'on en enlève au fur et à mesure
		i=len(self.liste_briques)-1
		while i >= 0:
			self.liste_briques[i].statut = 1
			self.detruire(i)
			i -= 1

	def creer_level(self,liste):
		"""Créé le tableau à partir d'une liste double,
			codant le satut de chaque brique"""

		## Nombres de briques horizontalement et verticalement
		self.nbx = len(liste[0])
		self.nby = len(liste)

		## Dimension des briques
		self.dimx = (self.xmax-2*self.left)/self.nbx
		self.dimy = 30
		self.left=(self.xmax-self.nbx*self.dimx)/2 ## Pour centrer le lv

		self.nbrique = 0     ## Nombre de briques

		## Construction des lignes
		for j in range(self.nby):
			## Construction des colonnes
			for i in range(self.nbx):
				## Les briques sont construites dans une liste
				if liste[j][i] != 0 :
					self.liste_briques.append( \
						Brique(self.canevas , \
							self.left+self.dimx*i , \
							self.top+self.dimy*j , \
							self.left+self.dimx*(i+1) , \
							self.top+self.dimy*(j+1) , \
							liste[j][i] ) )
					if liste[j][i] > 0 :
						self.nbrique+=1

	##        self.appli.main.ecrireinfo(" NIVEAU "+str(self.lv)+" ")

	def detruire(self , num):
		"""Détruit la brique numéro num"""
		if self.liste_briques[num].statut > 1:
			self.liste_briques[num].\
				changestatut(self.liste_briques[num].statut-1)
			return True

		elif self.liste_briques[num].statut == 1:
			self.liste_briques[num].__del__
			del self.liste_briques[num]
			self.nbrique -= 1
			return True

		elif self.liste_briques[num].statut == -1:
			return False


class Application:
	"""Programme principal"""
	def __init__(self , dimx = 400 , dimy = 600):
		"""Constructeur de l'interface"""
		## Récupération des préférences
		self.recup_option()
		
		## Création des high-scores
		self.highscore=Highscore()

		## Variables de jeu
		self.maxtiming = 2
		self.timing = self.maxtiming      ## Vitesse de la balle
		self.maxvie = 3
		self.vie = self.maxvie            ## Nombre de vies
		self.lv = 1                       ## Numéro du niveau
		self.score = 0                     ## Score


		## Variables globales de contôle
		self.fen = 0 			## 0: aucune fenetre n'est ouverte
		self.lance = 0          ## 0: La balle est arêtée ,  1: Elle est lancée
		self.pause = 0               ## 0: Le jeu n'est pas en pause ,  1:Pause
		self.pos_init = 1          ## 1: Le jeu est en position initiale
		self.mousex , self.mousey = -1 , -1   ## Coordonnées de la souris
		self.mouseauto = 0      ## 0: La souris est bougée par le joueur,
								## 1: Le curseur est placé automatiquement
								## 2: Le curseur est libéré

		## Création de l'objet souris
		self.souris=Souris(self)

		## Création de la fenêtre de jeu et récupération des sous-objets
		self.dimx,self.dimy=dimx,dimy
		self.main=Fenetre(self,dimx , dimy )
		

		## Création (instanciation) des objets du jeu
		self.creer_raquette()
		self.creer_balle()
		self.creer_niveau()

		## Partir sur de bonnes bases
		self.main.root.update()
		self.newgame()

		## Affiche des paramètres de test si besoin
		## Par ex des valeurs de variables
	##        self.test()

	def creer_raquette(self):
		"""Construit la raquette"""
		x,y=self.dimx/2 , self.dimy-100
		self.raquette = Raquette(self.main.canevas , x,y)

	def creer_balle(self):
		"""Construit la balle"""
		rayon = 15 ## Rayon de la balle
		x,y=self.dimx/2,self.dimy-100-rayon
		self.balle = Balle(self.main.canevas , x,y , rayon)

	def creer_niveau(self):
		"""Construit le niveau lv"""
		self.niveau = Niveau(self , lv=self.lv)

	def recup_option(self):		
		"""Construit un dictionnaire avec la liste des options de la forme :
			self.option[section][option] à partir de 'config.ini"""
		config=ConfigParser.ConfigParser()
		if not os.path.exists('config.ini')\
			or not os.path.exists('config_defaut.ini'): 
			self.creer_opt()
		config.read('config.ini')
		self.option={}
		for section in config.sections():
			for option in config.options(section):
				self.option[option]=config.get(section,option)
		
	def getopt(self,section,option,defaut=0):
		"""Renvoie l'option section,option 
			ou defaut si elle n'existe pas dans le config.ini"""
		config=ConfigParser.ConfigParser()	
		if not os.path.exists('config.ini'):
			self.creer_opt()
		config.read('config.ini')
		try:
			return config.get(section,option)
		except:
			return defaut

	def creer_opt(self):
		"""Creer le fichier config.ini"""
		if not os.path.exists('config_defaut.ini'):		
			conf_file=open('config_defaut.ini','w')
			conf_file.write(\
'''[test]
a = 1
b = 2
c = 3

[Graphisme]
Largeur = 400
Hauteur = 600

[Jeu]
Vitesse initiale = 1.2
''')
			conf_file.close()
		if not os.path.exists('config.ini'):
			import shutil
			shutil.copy('config_defaut.ini','config.ini')		
		
	def test(self):
		"""Fonction de test qui affiche des paramètres, à virer à terme"""
	##        self.txt_test.configure(text="Test : %s"%(self.mouseauto))
		pass

	def newgame(self):
		""" Lance une nouvelle partie"""
		self.setvie(self.maxvie)
		self.setlv(1)
		self.setscore(0)
		self.reinit()

	def reinit(self):
		"""Redessine un niveau complet"""
		## Destruction et recréation du niveau
		self.niveau.__del__()
		self.creer_niveau()
		## Position de départ pour la raquette et la balle
		self.stop()

	def start(self , event):
		"""Lance la balle ou met en pause/dépause"""
		if self.fen==1 :
			return
		self.pos_init = 0
		## Si la balle est à l'arret (pause ou début du tableau)
		if self.lance == 0 :
			## On informe qu'elle est lancée
			self.lance = 1
			## On informe que le jeu n'est pas en pause
			self.pause = 0
			## On recentre la souris et on efface le curseur
			self.souris.centresouris()
			self.main.canevas.configure(cursor='@invisiblecursor white')
			## On efface la fenêtre d'infos
			self.main.effaceinfo()
			## On lance la balle
			self.avance_balle()
		## Sinon, si elle est lancée, on met le jeu en pause
		elif self.lance == 1 :
			self.lance = 0
			self.pause = 1

	def stop(self):
		"""Stop la balle et remet raquette+balle à leur position d'origine"""
		## La balle est arrêtée,
		## le jeu n'est pas en pause et on est en position initiale
		self.lance = 0
		self.pause = 0
		self.pos_init = 1
		## Raquette au point de départ
		self.raquette.x = self.raquette.xdef
		self.raquette.y = self.raquette.ydef
		self.raquette.redraw()
		## Souris centrée sur la raquette
		self.main.canevas.configure(cursor='@invisiblecursor white')
		self.souris.centresouris()
		## La balle suit la raquette
		self.balle.x = self.raquette.x
		self.balle.y = self.raquette.y-self.balle.rayon
		self.balle.redraw()
		## Reinitialisation de la direction de la balle
		self.balle.dirx = uniform(-1,1)   ## Direction horizontale aléatoire
		self.balle.diry = -1.0            ## fait partie des choses à revoir
		self.balle.normalise()
		self.balle.vitesse = self.balle.vitesse_lv

	def triche(self,event):
		"""Juste pour passer d'un niveau, pour les tester bien sûr ^_^ """
		self.main.effaceinfo()
		self.gagne()
		self.setvie(10)

	def gagne(self):
		"""Si on gagne on passe d'un lv"""
		self.setlv(self.lv+1)
		self.reinit()

	def perdu(self):
		"""Si plus de vie"""
		self.main.fenetreperdu()

	def setvie(self , vie):
		""" Met à jour le nombre de vies"""
		self.vie = vie
		self.main.txt_vie.configure(text = ' VIES : '+str(self.vie)+" ")
		if self.vie == 0 :
			self.main.txt_vie.configure(fg = 'red')
		else:
			self.main.txt_vie.configure(fg = 'white')
	def setscore(self, score):
		self.score=score
		self.main.txt_score.configure(text = 'SCORE : '+str(int(self.score)))


	def settiming(self , n):
		"""Change la vitesse de jeu"""
		if n >= 1:
			self.timing = n

	def setlv(self , lv):
		""" Met à jour le niveau"""
		## Nombre de points gagnés
		points=self.score+100*self.vie
		self.setscore(points)
		self.lv = lv
		self.main.txt_level.configure(text = ' NIVEAU : '+str(self.lv)+" ")
		if lv>1 :
			self.main.ecrireinfo(' NIVEAU '+str(self.lv)+" ")
		else:
			self.main.ecrireinfo('Clique droit pour\nlibérer la souris',couleur='red',taille=30)
		## A chaque niveau ça va un peu plus vite
		self.balle.vitesse_lv = \
			min(self.balle.vitesse_init + self.balle.acceler_lv*(self.lv-1),\
			self.balle.vitesse_max)
		## Tous les 2 niveaux jusqu'au 5 on gagne une vie, pour un max de 5
		if 1 <lv <= 5 and self.vie < 5:
			self.setvie(self.vie+self.lv%2)

	def bouge_raquette(self , event):
		"""Gestion de la raquette à la souris, réponse à l'event <Move>"""

		## Si on veut vraiment avoir le curseur
		if self.mouseauto == 2 :
			return

		## Si le curseur a été positionné automatiquement, on sort
		elif self.mouseauto == 1 :
			self.mouseauto = 0
			return

		## Si le joueur à réellement bougé la souris
		elif self.mouseauto == 0 :

			## Initialisation de la position de la souris
			if self.mousex == -1:
				self.mousex = int(event.x)
			else:
				## Calcul de la variation de position
				delta = int(event.x)-self.mousex
				## Mise à jour des nouvelles coordonnées
				self.mousex = int(event.x)
				## Test si le jeu n'est pas en pause
				if self.pause == 0:
					## On essaie de déplacer la raquette
					if self.raquette.deplace(delta):
						## Si position de départ on bouge aussi la balle
						if self.lance == 0:
							self.balle.x = self.raquette.x
							self.balle.y = self.raquette.y-self.balle.rayon
							self.balle.redraw()
					## Si on peut pas c'est qu'on est sur un bord
					## et on replace le curseur au centre de la raquette
					else:
						self.souris.centresouris()

	def test_bords(self):
		"""Test si la balle touche un bord de l'écran ou la raquette"""
		## Test si la balle touche les bords du jeu
		tol=self.balle.vitesse+1
		self.balle.test_haut(0 , 0 , self.dimx , tol)
		self.balle.test_droite(self.dimx-tol , 0 , self.dimx , self.dimy)
		self.balle.test_gauche(0 , 0 , tol , self.dimy)
		self.test_raquette()

	def test_raquette(self):
		"""Test si la balle rebodit surla raquette"""
		if self.balle.test_raquette_bas(self.raquette.x-self.raquette.larg , \
				self.raquette.y , \
				self.raquette.x+self.raquette.larg , \
				self.raquette.y+10):
			## Dans ca cas, la direction de la balle dépend de la distance
			## de son point de contact avec le milieu de la raquette
			## Milieu : rebond vertical, Extrémités : 45°
			self.balle.changedir(\
				(self.balle.x-self.raquette.x)/self.raquette.larg,-1.0)

	def zone_test_briques(self):
		"""Définie la zone dans laquelle on doit tester les contacts
		   avec les briques"""
		x=self.balle.x
		y=self.balle.y
		r=self.balle.rayon
		if (self.niveau.left - r <= x <= self.niveau.left+self.niveau.dimx*self.niveau.nbx+r)\
			and (self.niveau.top - r <= y <= self.niveau.top+self.niveau.dimy*self.niveau.nby+r) :
			return True
		else:
			return False


	def test_briques(self):
		"""Test si une brique est touchée et la supprime si c'est le cas"""
		## Nombre de points par brique touchée
		points=10*self.balle.vitesse+5*self.lv
		score=self.score+points
		## Tolérance de la zone de test : La vitesse de la balle
		tol=int(self.balle.vitesse)+1
		## Si la balle est dans la zone des briques
		if self.zone_test_briques() :
		## S'il reste des briques en jeu
			if self.niveau.nbrique > 0:
				## Numéro de la brique testée
				num = 0
				## Parcours de la liste des briques
				for brique in self.niveau.liste_briques:
					exist = brique.statut
					x1 = brique.xa
					y1 = brique.ya
					x2 = brique.xb
					y2 = brique.yb
					if exist != 0:
						## Principe :
						##  Si la brique est encore en jeu ,
						##  On test si la balle la touche dans chaque direction
						##  Si c'est le cas ,  on la détruit avec sa méthode
						##  (en fait on met à jour son statut)
						##  Si la brique est détruite, on màj le score
						##  Enfin on sort de la boucle
						if self.balle.test_coins(x1,y1,x2,y2):
							if self.niveau.detruire(num):
								self.setscore(score)
							return True
						elif self.balle.test_haut(x1 , y2-tol , x2 , y2):
							if self.niveau.detruire(num):
								self.setscore(score)
							return True
						elif self.balle.test_bas(x1 , y1 , x2 , y1+tol):
							if self.niveau.detruire(num):
								self.setscore(score)
							return True
						elif self.balle.test_droite(x1 , y1 , x1+tol , y2):
							if self.niveau.detruire(num):
								self.setscore(score)
							return True
						elif self.balle.test_gauche(x2-tol , y1 , x2 , y2):
							if self.niveau.detruire(num):
								self.setscore(score)
							return True
					num+=1
		if self.niveau.nbrique == 0:
			## Si plus de brique on a fini le lv
			self.gagne()

	def test_mort(self):
		"""Test si la balle passe sous la raquette"""
	##        if self.balle.y >= self.raquette.y+self.raquette.haut:
		if self.balle.y-self.balle.rayon >= self.dimy:
			if self.vie > 0:
				self.setvie(self.vie-1)
			elif self.vie == 0:
				self.perdu()
			self.stop()

	def avance_balle(self):
		"""Boucle de déplacement de la balle"""
		if self.lance == 1:
			## On déplace la balle
			self.balle.deplace()
			## On test alors les collisions avec les objets
			self.test_bords()
			self.test_briques()
			self.test_mort()
			## On boucle (récusrsion)
			self.main.root.after(self.timing , self.avance_balle)


class Souris:
	def __init__(self,appli):
		## Classe Application qui invoque la souris
		self.appli=appli

		## Initialisation de X11 pour la gestion de la souris
		self.display = Xlib.display.Display()
		self.screen = self.display.screen()
		self.roots = self.screen.root

		## Création du fichier du curseur invisible
		## (seulement s'il n'existe pas déjà)
		if not (os.path.exists('invisiblecursor')):
			os.umask(0177) # octal
			f=open("invisiblecursor","w")
			f.write(kNullCursorData)
			f.close()

	def centresouris(self):
		"""Centre la souris sur la raquette"""
		## On met à jour les coordonnées de la raquette
		self.appli.raquette.majcoordabs()
		## On place la souris grace à xlib
		self.roots.warp_pointer(\
			self.appli.raquette.xabs,self.appli.raquette.yabs)
		self.display.sync()
		## Maj des coordonnées relatives de la souris
		self.appli.mousex = \
			self.appli.raquette.xabs-self.appli.main.canevas.winfo_rootx()
		## L'event généré ne doit pas déplacer la raquette
		self.appli.mouseauto = 1

	def rentresouris(self,event):
		"""Rentre la souris dans le canevas"""
		if self.appli.fen==1 :
			return
		if self.appli.pause == 0 and self.appli.mouseauto != 2:
			self.appli.main.canevas.configure(cursor='@invisiblecursor white')
			self.centresouris()

	def liberesouris(self,event):
		"""Libère la souris"""
		if self.appli.fen==1:
			return
		## Si la souris n'est pas libre
		if self.appli.mouseauto != 2:
			## On la libère et on met en pause
			self.appli.mouseauto = 2
			self.appli.main.canevas.configure(cursor='arrow')
			self.appli.pause=1

		else:
			## Sinon on la rerentre dans le jeu et on repart
			self.appli.main.canevas.configure(cursor='@invisiblecursor white')
			self.centresouris()
			self.appli.pause =0

		## Switch pause/dépause seulement si on n'est pas en pos initiale
		if self.appli.pos_init == 0 :
			self.appli.start(None)


class Fenetre :
	def __init__(self , appli, dimx = 400 , dimy = 600):
		"""Constructeur de l'interface"""
		## Classe Application qui invoque la fenêtre
		self.appli=appli

		## Fenêtre de jeu
		self.main = Tk()
		self.main.title("Arkapython")

		self.root=Frame(self.main,bg='black')
		self.root.pack()

		## Paramètres d'affichage des widgets
		self.param_menu_titres={'font':'Courrier 18 bold',\
			'bg':'black','fg':'white',\
			'activebackground':'red','activeforeground':'black',\
			'selectcolor':'white','borderwidth':0,'activeborderwidth':1}
		self.param_menu={'tearoff':0, 'font':'Courrier 12 bold',\
			'bg':'black','fg':'white',\
			'activebackground':'red','activeforeground':'black',\
			'selectcolor':'white','borderwidth':1,'activeborderwidth':1}

		self.param_bouton={'font':"Courrier 18 bold" , \
			'bg':'black' , 'fg':'white', 'relief':'flat' , \
			'activebackground':'red' , 'activeforeground': 'black'}

		self.param_label={'font':"Courrier 25 bold" ,\
			'bg':'black' , 'fg':'white'}

		self.param_txt={'font':'Courrier 12','bg':'black','fg':'white'}

		self.param_toplevel={'bg':'black'}
		
		self.param_frame={'bg':'black','bd':0,'relief':'flat'}

		## Barre de menu
		self.menubar=Menu(self.main,self.param_menu_titres)
			## Sous-menu High-scores
		self.highscoremenu=Menu(self.menubar, self.param_menu)
		self.highscoremenu.add_command(label='Voir les high-scores',command=self.fenetre_highscore)
		self.highscoremenu.add_command(label='Effacer les high-scores',command=appli.highscore.creer)
			## Menu Fichier
		self.filemenu = Menu(self.menubar,self.param_menu)
		self.filemenu.add_command(label="Nouvelle partie", command=self.appli.newgame)
		self.filemenu.add_command(label="Quitter", command=self.main.quit)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="High-scores",command=self.fenetre_highscore)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Préférences", command=self.fenetre_preferences)
		self.menubar.add_cascade(label="MENU", menu=self.filemenu)
			## Menu A propos
		self.aboutmenu = Menu(self.menubar,self.param_menu)
		self.aboutmenu.add_command(label="Aide", command=self.fenetre_aide)
		self.aboutmenu.add_command(label="Code source", command=self.fenetre_source)
		self.aboutmenu.add_separator()
		self.aboutmenu.add_command(label="A propos", command=self.fenetre_apropos)
		self.menubar.add_cascade(label="AIDE", menu=self.aboutmenu)

		self.main.config(menu=self.menubar)

		## Textes NIVEAU, SCORE et VIES
		self.txt_level = Label(self.root , self.param_label)
		self.txt_level.grid(row = 3 , column = 1 , pady=5 , sticky ='W')

		self.txt_vie = Label(self.root ,self.param_label)
		self.txt_vie.grid(row = 1 , column = 2, pady=5 , sticky ='E')

		self.txt_score = Label(self.root ,self.param_label)
		self.txt_score.grid(row = 1 , column = 1, pady=5 , sticky ='W')

		## Canevas
		self.dimx , self.dimy = dimx , dimy   ## Dimensions du canevas
		self.canevas = Canvas(self.root , bg = 'black' , cursor='@invisiblecursor white' , \
			width = self.dimx , height = self.dimy)
		self.canevas.grid(row = 2 , column = 1 , columnspan = 2 , \
			padx = 5 , pady = 5)

		## Bouttons		
		Button(self.root , self.param_bouton, text = "Quitter" , \
			command = self.root.quit).\
			grid(row = 3 , column = 2  , padx = 5 , pady = 5 , sticky ='E')

		## Pour les tests. A virer
		## -----------------------
	##        self.txt_test = Label(self.root , text = ' Test : ' , \
	##            font = "Courrier 12 bold" , bg = 'black' , fg = 'white')
	##        self.txt_test.grid(row = 0, column = 1 , columnspan = 2 , sticky='W')
	##        self.bouton_test=Button(self.root , text = "Test" , \
	##            bg='black' , fg='white', relief='flat' , \
	##            font = "Arial 16 bold" , \
	##            activebackground = 'red' , activeforeground = 'black' ,
	##            command = self.test)
	##        self.bouton_test.grid(row = 4 , column = 2  , padx = 5 , pady = 5 , sticky ='E')

		## Gestion des événements
		self.canevas.bind('<Button-1>' , self.appli.start)
		self.canevas.bind_all('<Motion>' , self.appli.bouge_raquette)
		self.canevas.bind_all('<Control-w>',self.appli.triche)
		self.canevas.bind_all('<Escape>',self.quitter)
		self.canevas.bind(('<Enter>','<Leave>'),self.appli.souris.rentresouris)
		self.canevas.bind_all(('<Enter>','<Leave>'),self.appli.souris.rentresouris)
		self.canevas.bind_all('<Button-3>',self.appli.souris.liberesouris)

	def quitter(self,event):
		"""Fermer l'appli"""
		self.root.quit()

	def ecrireinfo(self , chaine='', couleur='white',taille=50,temps=0):
		"""Ecrit des infos sur le canevas"""
		## On écrit le texte au dessus de la raquette dans la couleur donnée	
		x=self.dimx/2
		y=self.appli.raquette.y-150
		self.txt_info = self.canevas.create_text(x , y , \
			anchor='center',justify='center',\
			font="Courrier "+`taille`+" bold", fill=couleur,text=chaine)
		bound=self.canevas.bbox(self.txt_info)
		self.fond_info=self.canevas.create_rectangle(bound,fill='black')
		self.canevas.lift(self.txt_info)
		## Si un temps (en secondes) est précisé on efface au bout de ce temps
		if temps != 0:
			self.root.after(temps*1000,self.effaceinfo)

	def effaceinfo(self):
		"""Efface les infos sur le canevas"""	
		self.canevas.delete(self.txt_info)
		self.canevas.delete(self.fond_info)
	
	## Fenêtres secondaires
	## --------------------
	## A chaque fois qu'on ouvre une fenêtre, 
	## on met le paramètre self.appli.fen à 1 pour éviter les conflit de souris
	## avec la fenêtre principale
	## Quand on ferme la fenêtre, on le remet à 0
	##
	
	def fenetre_highscore(self):
		"""Fenetre 'High score'"""
		self.appli.fen=1
		self.fen_highscore=Toplevel(self.main,self.param_toplevel)
		self.fen_highscore.title("High scores")
		self.fen_highscore.transient(self.main)
		self.fen_highscore.geometry(\
			'+'+str(self.main.winfo_rootx())+'+'+str(self.main.winfo_rooty()))
			
		self.fen_highscore.protocol('WM_DELETE_WINDOW', self.fenetre_highscore_quitter)
		self.param_hs_label={'font':'Courrier 18 bold', 'bg':'black','fg':'white'}		
		
		## Récupération des highscores
		hs=self.appli.highscore
		hs.lire()
		## S'il n'y en a pas, on l'indique
		if not(hs.high):
			Label(self.fen_highscore,self.param_hs_label, text='Pas de high score').\
				grid(row=0, column=1, columnspan=2)
		
		## Remplissage de la fenêtre	
		ligne=1
		for s in hs.high:
			Label(self.fen_highscore,self.param_hs_label, text=str(s[0])).\
				grid(row=ligne, column=1, sticky='W')
			Label(self.fen_highscore,self.param_hs_label, text=str(s[2])).\
				grid(row=ligne, column=2, sticky='W')
			ligne+=1
		Button(self.fen_highscore , self.param_bouton, text = "Effacer" , \
			command = hs.creer).\
			grid(row = 100 , column = 1 , padx = 5 , pady = 5 , sticky ='E')
		Button(self.fen_highscore , self.param_bouton, text = "Fermer" , \
			command = self.fenetre_highscore_quitter).\
			grid(row = 100 , column =2 , padx = 5 , pady = 5 , sticky ='W')
			
		self.fen_highscore.focus_set( )
		self.fen_highscore.grab_set( )
		self.fen_highscore.wait_window()
		
	def fenetre_highscore_quitter(self):
		self.appli.fen=0
		self.fen_highscore.destroy()
		

	def fenetreperdu(self):
		"""Fenêtre quand on a perdu"""
		self.appli.souris.liberesouris(None)
		self.appli.fen=1
		self.fen_perdu=Toplevel(self.main,self.param_toplevel)
		self.fen_perdu.title("Perdu")
		self.fen_perdu.overrideredirect(1)
		self.fen_perdu.transient(self.main)
		self.fen_perdu.geometry(str(self.main.winfo_width()-20)+'x'\
			+str(int(self.main.winfo_height()/4+50))\
			+'+'+str(self.main.winfo_rootx()+10)\
			+'+'+str(self.main.winfo_rooty()+int(self.main.winfo_height()/4)))


		Label(self.fen_perdu, font='Courrier 20 bold', bg='black',fg='red',\
			text="Vous avez perdu :'(")\
			.grid (row=1, column=1, columnspan=2, padx=10, pady=10)
		
		score=int(self.appli.score)	

		Label(self.fen_perdu, font='Courrier 20 bold', bg='black',fg='white',\
			text="Votre score est : "+str(int(self.appli.score))).\
			grid (row=2, column=1, columnspan=2, padx=10, pady=10)
		
		## Vérification si le score est dans les highscores	
		hs=self.appli.highscore
		if hs.is_hs(score):
			Label(self.fen_perdu, font='Courrier 20 bold', bg='black',fg='white',\
				text="Vous êtes dans le top "+str(hs.NBHIGH)).\
				grid (row=3, column=1, columnspan=2, padx=10, pady=10)
			hs.ajouter(score,'Player')

		Button(self.fen_perdu , self.param_bouton, text = "Rejouer" , \
			command = self.fenetreperdu_rejouer).\
			grid(row = 100 , column = 1 , padx = 5 , pady = 5 , sticky ='E')

		Button(self.fen_perdu , self.param_bouton, text = "Quitter" , \
			command = self.fenetreperdu_quitter).\
			grid(row = 100 , column = 2  , padx = 5 , pady = 5 , sticky ='W')
		self.fen_perdu.protocol('WM_DELETE_WINDOW', self.fenetreperdu_quitter)

		self.fen_perdu.focus_set( )
		self.fen_perdu.grab_set( )
		self.fen_perdu.wait_window()

	def fenetreperdu_rejouer(self):
		self.appli.fen=0
		self.fen_perdu.destroy()
		self.appli.newgame()

	def fenetreperdu_quitter(self):
		self.appli.fen=0
		self.fen_perdu.destroy()
		self.main.quit()

	def fenetre_aide(self):
		"""Fenetre 'Aide'"""
		self.appli.fen=1
		self.fen_aide=Toplevel(self.main,self.param_toplevel)
		self.fen_aide.title("Aide")
		self.fen_aide.transient(self.main)
		self.fen_aide.geometry(\
			'+'+str(self.main.winfo_rootx())+'+'+str(self.main.winfo_rooty()))
		txt="""
Commandes :
-----------
- Boutton gauche : Lance la balle ou met en pause
- Boutton droite : Libère la souris et met en pause
- Esc : Quitter
- Ctrl+w : Cheat. Avance d'un niveau et donne 10 vies (pour les tests)"""
		txt_aide=Text(self.fen_aide,self.param_txt)
		txt_aide.pack(padx=10,pady=10)
		txt_aide.insert(END, txt)
		txt_aide.configure(state='disabled')
		Button(self.fen_aide, self.param_bouton,text="Fermer",\
			command=self.fenetre_aide_ferme).pack(pady=5)
		self.fen_aide.protocol('WM_DELETE_WINDOW', self.fenetre_aide_ferme)
		self.fen_aide.focus_set( )
		self.fen_aide.grab_set( )
		self.fen_aide.wait_window()

	def fenetre_aide_ferme(self):
		self.appli.fen=0
		self.fen_aide.destroy()
	##        self.appli.souris.liberesouris(None)


	def fenetre_apropos(self):
		"""Fenetre 'A propos'"""
		self.appli.fen=1
		self.fen_apropos=Toplevel(self.main,self.param_toplevel)
		self.fen_apropos.title("A propos")
		self.fen_apropos.transient(self.main)
		self.fen_apropos.geometry(\
			'+'+str(self.main.winfo_rootx())+'+'+str(self.main.winfo_rooty()))
		txt_apropos=ScrolledText(self.fen_apropos,self.param_txt)
		txt_apropos.pack(padx=10,pady=10)
		txt_apropos.insert(END, txt_version.replace(chr(9),'    '))
		txt_apropos.configure(state='disabled')
		Button(self.fen_apropos, self.param_bouton,text="Fermer",\
			command=self.fenetre_apropos_ferme).pack(pady=5)
		self.fen_apropos.protocol('WM_DELETE_WINDOW', self.fenetre_apropos_ferme)
		## Astuce pour mettre la fenêtre en modal (à retenir...)
		self.fen_apropos.focus_set( )
		self.fen_apropos.grab_set( )
		self.fen_apropos.wait_window()

	def fenetre_apropos_ferme(self):
		self.appli.fen=0
		self.fen_apropos.destroy()
	##        self.appli.souris.liberesouris(None)

	def fenetre_source(self):
		"""Fenetre 'Code source'"""
		self.appli.fen=1
		self.fen_source = Toplevel(self.main,self.param_toplevel )
		self.fen_source.title("Code source")
		self.fen_source.transient(self.main)
		self.fen_source.geometry(\
			'+'+str(self.main.winfo_rootx())+'+'+str(self.main.winfo_rooty()))

		txt_source = ScrolledText(self.fen_source,self.param_txt,width=120)
		txt_source.pack(padx=10,pady=10)
		txt_source.insert('0.0', open(sys.argv[0]).read( ).replace(chr(9),'    '))
		txt_source.configure(state='disabled')
		Button(self.fen_source, self.param_bouton,text="Fermer",\
			command=self.fenetre_source_ferme).pack(pady=5)
		self.fen_source.protocol('WM_DELETE_WINDOW', self.fenetre_source_ferme)
		self.fen_source.focus_set( )
		self.fen_source.grab_set( )
		self.fen_source.wait_window()

	def fenetre_source_ferme(self):
		self.appli.fen=0
		self.fen_source.destroy()
	##        self.appli.souris.liberesouris(None)
	
	def fenetre_preferences(self):
		"""Fenetre 'Préférences'"""
		self.appli.fen=1
		self.fen_preferences = Toplevel(self.main,self.param_toplevel )
		self.fen_preferences.title("Préférences (PAS TERMINE)")
		self.fen_preferences.transient(self.main)
		self.fen_preferences.geometry(\
			'+'+str(self.main.winfo_rootx())+'+'+str(self.main.winfo_rooty()))
		
		## Layout de la fenêtre préférences et bouttons
		self.frm_bt=Frame(self.fen_preferences,self.param_frame)
		self.frm_bt.pack(padx=5, pady=5, side='bottom')
		self.frm_opt=Frame(self.fen_preferences,self.param_frame)
		self.frm_opt.pack(padx=5, pady=5, side='top')
		Button(self.frm_bt , self.param_bouton, text = "Annuler" , \
			command = self.fenetre_preferences_cancel).\
			pack(padx=5, pady=5, side='right')
			##grid(row = 100 , column = 100 , padx = 5 , pady = 5 , sticky ='E')
		Button(self.frm_bt , self.param_bouton, text = "Défaut" , \
			command = self.fenetre_preferences_defaut).\
			pack(padx=5, pady=5, side='right')
			##grid(row = 100 , column = 100  , padx = 5 , pady = 5 , sticky ='E')
		Button(self.frm_bt , self.param_bouton, text = "Sauver" , \
			command = self.fenetre_preferences_save).\
			pack(padx=5, pady=5, side='right')
			##grid(row = 100 , column = 100  , padx = 5 , pady = 5 , sticky ='E')
		
		Label(self.frm_opt, font='Courrier 20 bold', bg='black',fg='red',\
			text="Pas encore fonctionnel\n Les changements n'ont aucun effet")\
			.grid (row=100, column=1,columnspan=2, padx=10, pady=10)		
			
##		Label(self.frm_opt, font='Courrier 20 bold', bg='black',fg='red',\
##			text="Les changements prendront effet\n au prochain redémarrage")\
##			.grid (row=100, column=1,columnspan=2, padx=10, pady=10)
		
		if not os.path.exists('config.ini'):
			self.fenetre_preferences_defaut()
			return

		self.config=ConfigParser.ConfigParser()
		self.config.read('config.ini')
		
		self.fenetre_preferences_maj()
		
		self.fen_preferences.protocol('WM_DELETE_WINDOW', self.fenetre_preferences_cancel)
		self.fen_preferences.focus_set( )
		self.fen_preferences.grab_set( )
		self.fen_preferences.wait_window()
	
	def addopt(self,section,option='',genre='Entry'):
		"""Ajoute une ligne à la fenêtre préférences"""
		## Si on ajoute juste le titre d'une section
		if option=='':
			Label(self.frm_opt,self.param_opt_titre,text=section).grid (row=self.ligne, column=1,columnspan=2, sticky ='W')
			self.ligne+=1
			self.sections.append(section)
			self.options[section]=[]
			self.opt_val[section]={}
			self.opt_entry[section]={}
		## Si on a une option à régler
		else:
			self.opt_val[section][option]=StringVar()
			self.opt_val[section][option].set(self.config.get(section,option))
			Label(self.frm_opt,self.param_opt_enonce,text=option).grid (row=self.ligne, column=1, sticky ='W')
			self.opt_entry[section][option]=Entry(self.frm_opt,self.param_opt_entry,textvariable=self.opt_val[section][option])
			self.opt_entry[section][option].grid (row=self.ligne, column=2, sticky ='W')
			self.options[section].append(option)
			self.ligne+=1	
	
	def fenetre_preferences_maj(self):
		"""Rempli la fenêtre préférences avec les options"""
		self.param_opt_titre={'font':'Courrier 18 bold', 'bg':'black','fg':'white'}
		
		self.param_opt_enonce={'font':'Courrier 12 bold', 'bg':'black','fg':'white'}
		
		self.param_opt_entry={'font':'Courrier 12 bold','fg':'black','bg':'white',\
			'bd':1,'width':4}

		self.opt_entry={}
		self.opt_val={}
		self.sections=[]
		self.options={}
		self.ligne=1
##		sections=self.config.sections()
##		sections.sort()
##		for section in sections:
##			Label(self.frm_opt,self.param_opt_titre,text=section).grid (row=self.ligne, column=1,columnspan=2, sticky ='W')
##			self.ligne+=1
##			self.opt_val[section]={}
##			self.opt_entry[section]={}
##			options=self.config.options(section)
##			options.sort()
##			for option in options:
##				self.opt_val[section][option]=StringVar()
##				self.opt_val[section][option].set(self.config.get(section,option))
##				Label(self.frm_opt,self.param_opt_enonce,text=option).grid (row=self.ligne, column=1, sticky ='W')
##				self.opt_entry[section][option]=Entry(self.frm_opt,self.param_opt_entry,textvariable=self.opt_val[section][option])
##				self.opt_entry[section][option].grid (row=self.ligne, column=2, sticky ='W')
##				self.ligne+=1	
		self.addopt('Graphisme')
		self.addopt('Graphisme','Largeur')
		self.addopt('Graphisme','Hauteur')
		
		self.addopt('Jeu')
		self.addopt('Jeu','Vitesse initiale')
					
	def fenetre_preferences_save(self):
		"""Sauve les préférences"""
##		for section in self.config.sections():			
##			for option in self.config.options(section):				
##				self.config.set(section,option,self.opt_val[section][option].get())
		for section in self.sections:			
			for option in self.options[section]:				
				self.config.set(section,option,self.opt_val[section][option].get())		
		conf_file=open('config.ini','w')
		self.config.write(conf_file)
		conf_file.close()
		self.appli.fen=0
		self.fen_preferences.destroy()
		
		
	def fenetre_preferences_defaut(self):
		"""Préférences par défaut"""	
		self.config=ConfigParser.ConfigParser()
		if not os.path.exists('config.ini')\
			or not os.path.exists('config_defaut.ini'): 
			self.appli.creer_opt()
		self.config.read('config_defaut.ini')
		self.fenetre_preferences_maj()
	
	def fenetre_preferences_cancel(self):
		"""Annule les changements"""
		self.appli.fen=0
		self.fen_preferences.destroy()
		


class Highscore:
	NBHIGH=10  ## Nombre maxi de scores à stocker
	
	def __init__(self):
		if not os.path.exists('highscore'):
			self.creer()
		
		
	def creer(self):
		"""Crée ou efface le fichier 'highscore'"""
		hs=open('highscore','w')		
		hs.close()
		
	def lire(self):
		"""Récupère les données du fichier 'highscore'
			et les stock dans le tableau self.high"""
		hs=open('highscore','rb')
		hscsv=csv.reader(hs)

		self.high=[]
		for score,date,nom in hscsv:		
			self.high.append([int(score),date,nom])
		self.high.sort()
		self.high.reverse()		
		hs.close()
		

	def ajouter(self,score,nom):
		"""Ajoute un score"""
		t=time.localtime(time.time())
		date='%s/%s/%s %sh%s'%(t[2],t[1],t[0],t[3],t[4])
		self.lire()
		self.high.append([int(score),date,nom])
		self.high.sort()
		self.high.reverse()
		if len(self.high)>self.NBHIGH:
			self.high.pop()
		hs=open('highscore','w')
		hscsv=csv.writer(hs)
		for i in range(len(self.high)):	
			hscsv.writerow(self.high[i])
		hs.close()
		
	
	def is_hs(self,score):
		"""Test si le score est dans le top"""
		self.lire()
		if len(self.high)<self.NBHIGH or min(self.high)[0]<score:
			return True
		else:
			return False


## Lancement du prog principal
app = Application()
app.main.root.mainloop()
