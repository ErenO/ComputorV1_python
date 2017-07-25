import re
import sys
import math
#(?<=\=)((.)+) pour ce qui apres egal
# pour les exposants (?<=\^)((\d)+)
# pour le coeff (\d)+(?=\s\*)

def delta_positive(a, b, delta, c):
    print("positive")
    x1 = 0
    x2 = 0
    if a != 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
    else:
        x1 = 0
        x2 = 0
    print("delta =", delta)
    print("Reduced form:", a, "* X^2 +", b, "* X^1 +", c, "* X^0 = 0")
    print("Il y a deux solutions :")
    print("x1 ", x1)#.as_integer_ratio())
    print("x2 ", x2)

def delta_negative():
    print ("negative")
    print("Δ < 0 alors l'équation ne possède pas de solution réelle mais admet 2 solutions complexes x1 et x2")
    print("x1 = (−b − i√(-Δ) ) / (2a) et x2 = (−b + i√(-Δ) ) / (2a)")

def delta_zero(a, b):
    print("zerolf")
    print(a, b, "a et b")
    x0 = 0
    if a != 0:
        x0 = (-b) / (2 * a)
    else:
        print ("On peut pas diviser par zero")
    print("delta =", delta)
    print("Reduced form:", a, "* X^2 +", b, "* X^1 +", c, "* X^0 = 0")
    print(x0)

def calc_first_degrees(zero, one):
    print("Polynomial degree: 1")
    print("Reduced form :", one, "* X^1 +", zero, "* X^0 = 0")
    result = (-zero) / one
    print("Il y a une solution:")
    print("x =", result)

def calc_second_degrees(a, b, c):
    print ("a b et c", a, b, c)
    delta = abs(b * b) - (4 * a * c)
    print("Polynomial degree: 2")
    print("delta =", delta)
    print("Reduced form:", a, "* X^2 +", b, "* X^1 +", c, "* X^0 = 0")
    if delta > 0:
        delta_positive(a, b, delta, c)
    elif delta == 0:
        delta_zero(a, b)
    elif delta < 0:
        delta_negative()

def print_reduced_form(tab, exp):
    sys.stdout.write("Reduced form: ")
    index = 0
    for i in tab:
        if i != 0:
            print(i)
            sys.stdout.write("* X^")
            print(index)
        index += 1
    sys.stdout.write("= 0\n")
def calc_by_degrees(exp, nb):
    tab = [0] * (max(exp) + 1)
    i = 0
    for exo in exp:
        tab[exo] += nb[i]
        i += 1
    print_reduced_form(tab, exp)
    if tab[2] != 0 and max(exp) == 2:
        calc_second_degrees(tab[2], tab[1], tab[0])
    elif tab[1] != 0 and max(exp) == 1:
        calc_first_degrees(tab[0], tab[1])
    elif tab[0] != 0 and max(exp) == 0:
        print("Tous les nombres réels sont solution")
    else:
        print("l'equation est supérieur à un degrée 2, il est de degree", max(exp))
def print_sup_deg(a):
    print("l'equation est supérieur à un degrée 2, il est de degree", a)
    sys.exit(0)

def handle_param(befExp, befNb, aftExp, aftNb):
    i = 0
    exp = []
    nb = []
    for bexp in befExp:
        exp.append(int(bexp.replace(" ", "")))
    for aexp in aftExp:
        exp.append(int(aexp.replace(" ", "")))
    for bnb in befNb:
        nb.append(float(bnb.replace(" ", "")))
    for anb in aftNb:
        nb.append(-float(anb.replace(" ", "")))
    print("nb ", nb)
    print("exp ", exp)
    calc_by_degrees(exp, nb)

def main(argv):
    if len(argv) > 1:
        befEqu = re.search('(.)+(?=\=)', argv[1])
        aftEqu = re.search('(?<=\=)((.)+)', argv[1])
        befExp = re.findall('(?<=\^)(\d)+', befEqu[0])
        aftExp = re.findall('(?<=\^)(\d)+', aftEqu[0])
        befNb = re.findall('([+-]?\s*\d.?\d?)+(?=\s*\*)', befEqu[0])
        aftNb = re.findall('([+-]?\d.?\d?)+(?=\s*\*)', aftEqu[0])
        handle_param(befExp, befNb, aftExp, aftNb)
    else:
        for line in sys.stdin:
            print(line)

if __name__ == "__main__":
    main(sys.argv)
