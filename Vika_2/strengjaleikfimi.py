#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Strengir
@author: helgi
"""

setning = "Þetta er mjög flott setning. Þetta líka."

# prentum út lengd strengsins
print(len(setning))

# Vísar (substring): vísum í strengi út frá staðsetngu stafana
print(setning[0:10])

## Immutable: eftirfarandi kóði kastar villu:
# setning[10] = "p" # VIRKAR EKKI

# + virki: getum splæst saman strengjum með "+"
nafn="Helgi"
seinna = "Hilmarsson"
print(nafn + " " + seinna)

# Getum tekið strengi í sundur t.d. með split() fallinu
myWords = setning.split(". ")
print(myWords)

# Sækjum málsgrein á netinu 
# (ekkert rosalega sniðug aðgerð til að greina texta)
# en samt cool að skoða!
malsgrein = "Airport Associates er einn þeirra kröfuhafa sem hafa samþykkt að breyta skuldabréfum sínum í WOW air í hlutafé. Forstjóri félagsins segir það samdómaálit kröfuhafa að það sé heillavænlegri leið en að WOW fari í þrot. Tölur úr rekstri WOW air sýni algjöra umbreytingu á rekstri félagsins undanfarna mánuði og rekstrarhorfur félagsins séu góðar."
print(malsgrein)

words = malsgrein.split()
print(words)







