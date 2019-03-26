#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lykkjur
@author: helgi
"""

# ----------- % for lykkjur % ------------

### Skoðum lista
listi = [1,3,8,9]
for i in listi:
    print(i)    
    
### Vigrar
import numpy as np
for i in np.arange(10):
    print(i)

### range
for i in range(1,9):
    print(i)

### orðabækur
einkunnirIslands = {
 'Hannes' : 7,
 'Birkir' : 7,
 'Kári' : 6,
 'Ragnar' : 6,
 'Ari' : 6,
 'Aron' : 7,
 'Gylfi' : 8,
 'Jóhann' : 7,
 'Alfreð' : 6
}

for lykill in einkunnirIslands:
    print(lykill)
    
for lykill in einkunnirIslands:
    print(einkunnirIslands[lykill])

### strengir
malsgrein = "Airport Associates er einn þeirra kröfuhafa sem hafa samþykkt að breyta skuldabréfum sínum í WOW air í hlutafé. Forstjóri félagsins segir það samdómaálit kröfuhafa að það sé heillavænlegri leið en að WOW fari í þrot. Tölur úr rekstri WOW air sýni algjöra umbreytingu á rekstri félagsins undanfarna mánuði og rekstrarhorfur félagsins séu góðar."
# print(malsgrein)

words = malsgrein.split()
# print(words)

# Hvað eru mörg WOW ?
teljari = 0
for word in words:
    if word == "WOW":
        teljari += 1
        print(word)
        
print("fjoldinn er", teljari)
    
# ---------- % while lykkjur % -----------

### getum látið þær hegða sér eins og for lykkjur
### ítrum í gegnum eftirfarandi lista eins og við myndum gera með for-lykkju
listi = [1,2,7,20]
i = 0
while i < len(listi):
    print(listi[i])
    i += 1

# getum blandað saman input og while til að komast fram hjá rangri notkun notenda

ar = 2019
aldur = int(input("Skraðu inn aldur: "))

while aldur < 18 or aldur > 200:
    aldur = int(input("Ekki leyfilegur aldur \
                      Skraðu inn aldur: "))

print("Þú fæddist árið ", ar-aldur)


# ---------- % break & continue % -----------

### einföld for-lykkja, break

# hættum þegar i verður 10
for i in range(30):
    if i == 10:
        break
    print(i)

### einföld for-lykkja, continue
# förum í næstu ítrun þegar i verður 10 (og sleppum að prenta 10!)
for i in range(30):
    if i == 10:
        continue
    print(i)

