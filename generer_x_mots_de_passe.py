#!/usr/bin/env python
#-*- coding: utf-8 -*-

#~ Importation des bibliothèques nécessaires
import os, sys, getopt
import string
from random import *

demande = sys.argv[1]

############### Définition d'une fonction
def genererMotDePasse():
	
	# lettres min + lettres maj + chiffres
	pop = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*$%&.:?!"
	maju = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	minu = "abcdefghijklmnopqrstuvwxyz"
	chif = "0123456789"
	spec = "+-*$%&.:?!"

	# Boucle pour être sûr de générer un mot de passe correct
	while 1:
		
		# Initialisation des variables
		c = 0
		passwd = ''
		nbmaju = 0
		nbminu = 0
		nbchif = 0
		nbspec = 0
		
		# Longueur variable entre 8 et 16 caractères
		longueur = randrange(8,16)
		
		# Boucle de génération d'un mot de passe
		while c < longueur:
			caractere = pop[randrange(72)]
			if caractere in maju:
				nbmaju += 1
			if caractere in minu:
				nbminu += 1
			if caractere in chif:
				nbchif += 1
			if caractere in spec:
				nbspec += 1
			passwd += caractere
			c += 1
		
		# Condition de validité du mot de passe : il doit contenir au moins 3 des 4 classes de caractères parmis nb*
		# (A|B) & (A|C) & (A|D) & (B|C) & (B|D) & (C|D)
		if (bool(nbmaju) or bool(nbminu)) and (bool(nbmaju) or bool(nbchif)) and (bool(nbmaju) or bool(nbspec)) and (bool(nbminu) or bool(nbchif)) and (bool(nbminu) or bool(nbspec)) and (bool(nbchif) or bool(nbspec)):
			return passwd
###################

print "Vous voulez " + demande + " mots de passe"

nb = 0
while nb < int(demande):
	print genererMotDePasse()
	nb += 1
