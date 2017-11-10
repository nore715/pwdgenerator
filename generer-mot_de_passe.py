#!/usr/bin/env python
#-*- coding: utf-8 -*-

import getopt, sys
import argparse
import os, sys, getopt
import string
from random import *

HardCodedLimit = 8
NbOfPwd = 1
LowerSizeLimit = 8
UpperSizeLimit = 12

############### Définition de la fonction de génération de mot de passe
def genererMotDePasse(lower,upper):
	
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
		
		# Longueur variable
		longueur = randrange(lower,upper)
		
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

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number",
                    type=int,
                    default=1,
                    help="number of random strings to generate")
parser.add_argument("-l", "--lower",
                    type=int,
                    default=HardCodedLimit,
                    help="minimum number of characters in random string")
parser.add_argument("-u", "--upper",
                    type=int,
                    default=HardCodedLimit,
                    help="maximum number of characters in random string")
args = parser.parse_args()

if args.number < 1:
    print "The number of required random strings cannot be null or negative"
elif args.lower < HardCodedLimit:
    print "The minimum number of characters cannot be lower than ",HardCodedLimit
elif args.upper < args.lower:
    print "The max nb of char in random string cannot be lower than the min nb of chars"
else:
    nb = 0
    print "Vous voulez",args.number,"mots de passe entre",args.lower,"et",args.upper,"caracteres"
    while nb < args.number:
        print genererMotDePasse(args.lower,args.upper+1)
        nb += 1






