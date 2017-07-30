#!/usr/bin/env python
# coding: utf-8
import re
import sys
import math
import collections
#(?<=\=)((.)+) pour ce qui apres egal
# pour les exposants (?<=\^)((\d)+)
# pour le coeff (\d)+(?=\s\*)

def delta_positive(a, b, delta, c):
    x1 = 0
    x2 = 0
    if a != 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
    else:
        x1 = 0
        x2 = 0
    print("delta =", delta)
    print("Le discriminant est strictement positif. Les deux solutions sont :")
    print("x1 ", x1) #.as_integer_ratio()))
    print("x2 ", x2)

def delta_negative(b, delta, a):
    print ("Le discriminant est negative")
    print ("Δ < 0 alors l'équation ne possède pas de solution réelle mais admet 2 solutions complexes x1 et x2")
    # print ("x1 = (−b − i√(-Δ) ) / (2a) et x2 = (−b + i√(-Δ) ) / (2a)")
    print ("x1 = (−", b, "− i√(", -delta,") ) / (", 2 * a,") et x2 = (−", b,"+ i√(", -delta,") ) / (", 2 * a,")")
def delta_zero(a, b):
    print("delta = 0")
    print("Le discriminant est égal à zero. La solution est :")
    x0 = 0
    if a != 0:
        x0 = (-b) / (2 * a)
    else:
        print (("On peut pas diviser par zero"))
    print("x = ", x0)

def calc_first_degrees(zero, one):
    print("Polynomial degree: 1")
    result = (-zero) / one
    print("Il y a une solution:")
    print("x =", result)

def calc_second_degrees(a, b, c):
    delta = abs(b * b) - (4 * a * c)
    print ("Polynomial degree: 2")
    print ("delta =", delta)
    if delta > 0:
        delta_positive(a, b, delta, c)
    elif delta == 0:
        delta_zero(a, b)
    elif delta < 0:
        delta_negative(b, delta, a)

def print_reduced_form(tab, exp):
    sys.stdout.write("Reduced form: ")
    index = 0
    s = ""
    for i in tab:
        if i != 0:
            if index > 0 and index + 1 < len(tab):
                if i > 0:
                    s += " + "
                else:
                    s += " - "
                i = abs(i)
            s += str(i)
            s += " * X ^ "
            s += str(index)
        index += 1
    s += (" = 0\n")
    print (s)

def calc_by_degrees(exp, nb):
    print ("exp", exp)
    tab = [0] * (abs(min(exp)) + max(exp) + 1)
    i = 0
    isInt = 0
    print ("tab calc", tab)
    for exo in exp:
        # if isinstance(exp, int) == False:
        #     isInt = 1
        tab[exo] += nb[i]
        i += 1
    print ("tab calc2", tab)
    if min(nb) != 0 and max(nb) != 0:
        print_reduced_form(tab, exp)
    else:
        print ("Reduced form: 0 = 0")
    if isInt == 1:
        print ("Le programme ne gère pas les exposants non entiers")
    elif max(exp) == 2 and tab[2] != 0:
        calc_second_degrees(tab[2], tab[1], tab[0])
    elif max(exp) == 1 and tab[1] != 0:
        calc_first_degrees(tab[0], tab[1])
    elif max(exp) == 0 and tab[0] == 0:
        print ("Tous les nombres réels sont solution")
    elif max(exp) == 0 and tab[0] != 0:
        print ("Équation impossible à résoudre")
    else:
        print ("L'equation est supérieur à un degrée 2, il est de degree", max(exp))

def print_sup_deg(a):
    print ("L'equation est supérieur à un degrée 2, il est de degree", a)
    sys.exit(0)

def handle_param(befExp, befNb, aftExp, aftNb):
    i = 0
    exp = []
    nb = []
    # gerer les exposants non entiers
    # if all(isinstance(item, int) for item in befExp) and all(isinstance(item, int) for item in befExp):
    for bexp in befExp:
        exp.append(int(bexp.replace(" ", "")))
    for aexp in aftExp:
        exp.append(int(aexp.replace(" ", "")))
    for bnb in befNb:
        nb.append(float(bnb.replace(" ", "")))
    for anb in aftNb:
        nb.append(-float(anb.replace(" ", "")))
    print ("exp", exp)
    print ("nb", nb)
    calc_by_degrees(exp, nb)
    # else:
    #     print("Exposants non entiers")

def main(argv):
    # print ((argv[1]))
    if len(argv) > 1:
        befEqu = re.search('(.)+(?=\=)', argv[1])
        aftEqu = re.search('(?<=\=)((.)+)', argv[1])
        befExp = re.findall('(?<=\^)(\s?[-+]*\d\.?\d*)+', befEqu.group(0))
        aftExp = re.findall('(?<=\^)(\s?[-+]*\d\.?\d*)+', aftEqu.group(0))
        befNb = re.findall('([+-]?\s*\d.?\d?)+(?=\s*\*)', befEqu.group(0))
        aftNb = re.findall('([+-]?\d.?\d?)+(?=\s*\*)', aftEqu.group(0))
        print (befExp, befNb, aftExp, aftNb)
        handle_param(befExp, befNb, aftExp, aftNb)
    else:
        for line in sys.stdin:
            # print(line)
            if len(line) > 0:
                befEqu = re.search('(.)+(?=\=)', line)
                aftEqu = re.search('(?<=\=)((.)+)', line)
                if befEqu and aftEqu:
                    befExp = re.findall('(?<=\^)(\s?[-+]*\d\.?\d*)+', befEqu.group(0))
                    aftExp = re.findall('(?<=\^)(\s?[-+]*\d\.?\d*)+', aftEqu.group(0))
                    befNb = re.findall('([+-]?\s*\d.?\d?)+(?=\s*\*)', befEqu.group(0))
                    aftNb = re.findall('([+-]?\d.?\d?)+(?=\s*\*)', aftEqu.group(0))
                    # if befEqu and aftEqu and befExp and aftExp:
                        # print (befExp, befNb, aftExp, aftNb)
                    print ("be, bn, ae, an",befExp, befNb, aftExp, aftNb)
                    handle_param(befExp, befNb, aftExp, aftNb)
                else:
                    print ("Ceci n'est pas une equation")
            else:
                print ("Ceci n'est pas une equation")


if __name__ == "__main__":
    main(sys.argv)
