#Ce module gere les images de background (background; victoire; defaite)

import sys
import os

def create (file1,file2,file3,file4): # Defini les fonds d'ecran. file1 : background; file2 : victoire; file3 : defaite; file 4 : menu
	bg=dict()
	myfile = open(file1, "r")
	bg["bg"]=myfile.read()
	myfile.close()

	myfile = open(file2, "r")
	bg["win"]=myfile.read()
	myfile.close()

	myfile = open(file3, "r")
	bg["lose"]=myfile.read()
	myfile.close()

	myfile = open(file4, "r")
        bg["menu"] = myfile.read()
        myfile.close()

        return bg

def show(bg,index):# Affiche un fond d'ecran
	os.system("clear")
	sys.stdout.write("\033[1;1H")

	sys.stdout.write(bg[index])
