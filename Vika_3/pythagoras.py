#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pýþagoras
Strúktúrum kóðann okkar út frá main falli og sýnum hvernig við
getum búið til "fake" main fall. 
Sá kóði er alltaf keyrður.
@author: helgi
"""

import math

def pythagoras(a,b):
    # hjálparfallið pythagoras
    # tekur inn lengdir tveggja skammhliða rétthyrnds þríhyrnings
    # skilar lengd langhliðarinnar
    c = math.sqrt(a**2 + b**2)
    return c

def pretty_print(langhlid1, langhlid2):
    # hjálparfallið prettyprint
    # tekur inn lengdir tveggja rétthyrnda þríhyrnga og prentar þær út á fallegan hátt
    # fallið skilar svo ekki neinu úttaki
    print("Fyrsta langhliðin er", langhlid1, "metrar")
    print("Sú seinni er svo", langhlid2, "metrar")
    print("Mismunurinn þeirra er því", abs(langhlid1-langhlid2), "metrar")
    return
    
# __main__
# reiknum lengd langhliða á rétthyrndu þríhyrningunum okkar með hjálparfalli
langhlid1 = pythagoras(3,4)
langhlid2 = pythagoras(10,100)

# prentum niðurstöðurnar út á flottan máta með hjálparfallinu pretty_print()
pretty_print(langhlid1, langhlid2)