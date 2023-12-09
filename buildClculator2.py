#it's my second calculator 
print("---      ---    /\   ------    -- --")
print("|  \    /  |   /--\    ||      ||-||")
print("|   \__/   |  /----\   ||      || ||")
print("--        -- --    --  ||      -- --")
print("Bonjour\nBienvenu( e ) dans cette simple calculatrice qui calcule deux nombres\nles operateurs (*|+| - |/|^) .\n merci de vous respecter ces normes\n")
from math import *
nmb1 =float(input("veuillez entrer votre premier valeur:"))
operateur =input("veuillez entrer votre operateur:")
nmb2 =float(input("veuillez entrer votre dexieme valeur:"))
def addition(nmb1,nmb2):
    return nmb1+nmb2
resultat1 = addition(nmb1,nmb2)
def soustraction(nmb1,nmb2):
    return nmb1-nmb2
resultat2 = soustraction(nmb1,nmb2)
def multiplication(nmb1,nmb2):
    return nmb1*nmb2
resultat3 = multiplication(nmb1,nmb2)
def division(nmb1,nmb2):
    return nmb1/nmb2
resultat4 = division(nmb1,nmb2)
if operateur == "+":
    print(resultat1)
elif operateur == "-":
    print(resultat2)
elif operateur == "*":
    print(resultat3)
elif operateur == "/":
    print(resultat4)
elif operateur =="^":
    print(pow(nmb1,nmb2))
else:
    print("##                ##")
    print(" \\              //")
    print("   |####   ####|")
    print("   |####   ####|")
    print("      \/\/\/\/   ")
    print(" //              \\")
    print("##                ##")
    print("cette n'existe pas  malheureusement\n### <essayer une autre fois> ###")
