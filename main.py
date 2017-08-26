#!/usr/bin/env python
# -*- coding: utf-8 -*-
from colors import *
import re
import sys
import math
import collections
#(?<=\=)((.)+) pour ce qui apres egal
# pour les exposants (?<=\^)((\d)+)
# pour le coeff (\d)+(?=\s\*)

# double square_root(double num)
# {
#   double x1;
#   double x2;
#
#   x1 = (num * 1.0) / 2;
#   x2 = (x1 + (num / x1)) / 2;
#   while (ABS(x1 - x2) >= 0.0000001)
#   {
#     x1 = x2;
#     x2 = (x1 + (num / x1)) / 2;
#   }
#   return (x2);
# }


def sqrt(num):
    x1 = (num * 1.0) / 2
    x2 = (x1 + (num / x1)) / 2
    while (abs(x1 - x2) > 0):
        x1 = x2
        x2 = (x1 + (num / x1)) / 2
    return x2

def delta_positive(a, b, delta, c):
    x1 = 0
    x2 = 0
    if a != 0:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
    else:
        x1 = 0
        x2 = 0
    sys.stdout.write(BLUE)
    print "Le discriminant est strictement positif. Les deux solutions sont :"
    sys.stdout.write(RED)
    print "x1 =", x1 #.as_integer_ratio())))
    print "x2 =", x2
    sys.stdout.write(RESET)

def delta_negative(b, delta, a):
    sys.stdout.write(RED)
    print "Le discriminant est negatif"
    sys.stdout.write(BLUE)
    print "Δ < 0 alors l'équation ne possède pas de solution réelle mais admet 2 solutions complexes x1 et x2"
    sys.stdout.write(RED)
    print "x1 = (−", b, "− i√(", -delta,") ) / (", 2 * a,") et x2 = (−", b,"+ i√(", -delta,") ) / (", 2 * a,")"
    sys.stdout.write(RESET)

def delta_zero(a, b):
    sys.stdout.write(BLUE)
    print "Le discriminant est égal à zero. La solution est :"
    sys.stdout.write(RED)
    x0 = 0
    if a != 0:
        x0 = (-b) / (2 * a)
    else:
        print "On peut pas diviser par zero"
    print "x =", x0
    sys.stdout.write(RESET)

def calc_first_degrees(zero, one):
    sys.stdout.write(RED)
    print "Polynomial degree: 1"
    result = (-zero) / one
    sys.stdout.write(BLUE)
    print "Il y a une solution:"
    sys.stdout.write(RED)
    print "x =", result
    sys.stdout.write(RESET)

def calc_second_degrees(a, b, c):
    delta = abs(b * b) - (4 * a * c)
    sys.stdout.write(RED)
    print "Polynomial degree: 2"
    sys.stdout.write(GREEN)
    print "delta =", delta
    if delta > 0:
        delta_positive(a, b, delta, c)
    elif delta == 0:
        delta_zero(a, b)
    elif delta < 0:
        delta_negative(b, delta, a)
    sys.stdout.write(RESET)

def reduced_form(tab, exp):
    index = 0
    sys.stdout.write(BLUE)
    nb = 0
    s = "Forme Réduite: "
    for i in tab:
        if i != 0:
            if index > 0 and index < len(tab):
                if i > 0:
                    s += " + "
                else:
                    s += " - "
                if i > nb:
                    nb = i
                i = abs(i)
            s += str(i)
            s += " * X ^ "
            s += str(index)
            if index > nb:
                nb = index
        else:
            if max(tab) == 0:
                s += "0"
        index += 1
    s += (" = 0\n")
    print (s)
    sys.stdout.write(RESET)
    return nb

def calc_by_degrees(exp, nb):
    tab = [0] * (abs(min(exp)) + max(exp) + 1)
    i = 0
    isInt = 0
    maxExp = 0
    for exo in exp:
        tab[exo] += nb[i]
        i += 1
    if (min(nb) != 0 and max(nb) != 0):
        maxExp = reduced_form(tab, exp)
    else:
        print "Reduced form: 0 = 0"
    sys.stdout.write(GREEN)
    if isInt == 1:
        print "Le programme ne gère pas les exposants non entiers"
    elif maxExp == 0 and tab[0] == 0:
        print "Tous les nombres réels sont solution"
    elif maxExp == 0 and tab[0] != 0:
        print "Équation impossible à résoudre"
    elif min(nb) == 0 and max(nb) == 0:
        print "Tous les nombres réels sont solution"
    elif maxExp == 2 and tab[2] != 0:
        calc_second_degrees(tab[2], tab[1], tab[0])
    elif maxExp == 1 and tab[1] != 0:
        calc_first_degrees(tab[0], tab[1])
    else:
        print "L'equation est supérieur à un degrée 2, il est de degree", max(exp)
    sys.stdout.write(RESET)

def handle_param(befExp, befNb, aftExp, aftNb):
    i = 0
    exp = []
    nb = []
    pb = 0
    expNb = 0
    sys.stdout.write(GREEN)
    if len(befExp) > 0 and len(befNb) > 0 or len(aftExp) > 0 and len(aftNb) > 0:
        for bexp in befExp:
            if bexp.find(".") == -1:
                expNb = int(bexp)
                if expNb > 10000:
                    print "Problème d'exposants1"
                    pb = 1
                else:
                    exp.append(expNb)
            else:
                if pb == 0:
                    print "Problème d'exposants2"
                    pb = 1
        for aexp in aftExp:
            if aexp.find(".") == -1:
                expNb = int(aexp)
                if expNb > 10000:
                    print "Problème d'exposants3"
                    pb = 1
                else:
                    exp.append(expNb)
            else:
                if pb == 0:
                    print "Problème d'exposants4"
                    pb = 1
        if pb == 0:
            print "befNb", befNb
            for bnb in befNb:
                nb.append(float(bnb))
            for anb in aftNb:
                nb.append(-float(anb))
            print "aftNb", aftNb
            if min(exp) >= 0:
                print "exp", exp, "nb", nb
                calc_by_degrees(exp, nb)
            else:
                print "Programme ne gere pas les exposants negatifs"
    else:
        print "Problème pas de nombres"
    sys.stdout.write(RESET)

def main(argv):
    sys.stdout.write(GREEN)
    if len(argv) > 1:
        equation = argv[1].replace(" ", "")
        befEqu = re.search('(.)+(?=\=)', equation)
        aftEqu = re.search('(?<=\=)((.)+)', equation)
        befExp = re.findall('(?<=\^)([+-]?\d\.?\d?)', befEqu.group(0))
        aftExp = re.findall('(?<=\^)([+-]?\d\.?\d?)', aftEqu.group(0))
        befNb = re.findall('([+-]?\d+\.?\d*)(?=\s*\*)', befEqu.group(0))
        aftNb = re.findall('([+-]?\d+\.?\d*)(?=\s*\*)', aftEqu.group(0))
        print "befNb", befNb, "befExp", befExp, "aftNb", aftNb, "aftExp", aftExp
        if len(befExp) == len(befNb) and len(aftExp) == len(aftNb):
            handle_param(befExp, befNb, aftExp, aftNb)
        else:
            print "Problème d'exposants5"
    else:
        line = sys.stdin.readline()
        while line:
            if len(line) > 0:
                befEqu = re.search('(.)+(?=\=)', line)
                aftEqu = re.search('(?<=\=)((.)+)', line)
                if befEqu and aftEqu:
                    befExp = re.findall('(?<=\^)([+-]?\d\.?\d?)', befEqu.group(0))
                    aftExp = re.findall('(?<=\^)([+-]?\d\.?\d?)', aftEqu.group(0))
                    befNb = re.findall('([+-]?\d+\.?\d+)(?=\s*\*)', befEqu.group(0))
                    aftNb = re.findall('([+-]?\d+\.?\d+)(?=\s*\*)', aftEqu.group(0))
                    if len(befExp) == len(befNb) and len(aftExp) == len(aftNb):
                        handle_param(befExp, befNb, aftExp, aftNb)
                    else:
                        print "Problème d'exposants"
                else:
                    print "Ceci n'est pas une equation"
            else:
                print "Ceci n'est pas une equation"
            line = sys.stdin.readline()
    sys.stdout.write(RESET)

if __name__ == "__main__":
    main(sys.argv)
