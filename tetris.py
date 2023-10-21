import time
import os
import random
abs = 5
ord = 6
def affich(abs,ord):
    obj = """
******
*    *
******
"""
    obj_lignes = obj.strip().split('\n')
    for i in range(len(obj_lignes)):
        if i + ord < 0:
            continue  # Ignore les lignes au-delà du haut de l'écran
        espace = ' ' * abs
        print(espace + obj_lignes[i])

while (abs>=0):
    affich(abs,ord)
    abs-=1
    ord+=10
    if(abs==0):
        os.system('clear')
        abs=6
    time.sleep(0.5)