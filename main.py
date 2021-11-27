import sys
sys.tracebacklimit=0
try:
    a = input("Saisir vrai ou faux")
    b = input("Saisir vrai ou faux")
    if (a != "vrai" and a != "faux") or (b != "vrai" and b != "faux"):
        a = 1
        b = 2
        raise Exception("Suivez les consigne !")
except TypeError:

    print("Mauvaise saisie")

if a == "vrai":
    a = True
if a == "faux":
    a = False
if b == "vrai":
    b = True
if b == "faux":
    b = False

if a == b:
    print("Le XOR de a et b vaut faux")
elif a != b:
    print("Le XOR de a et b vaut vrai")