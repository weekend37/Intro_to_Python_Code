#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Orðabækur (e. dictionaries)
@author: helgi
"""

# prófum að geyma upplýsingar um einkunnir íslenska 
# landsliðsins á móti Andorra (frá Vísi.is)
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

### Hvað fékk Birkir?
print(einkunnirIslands['Birkir'])

### prentum nokkra eiginleika orðabókarinnar:
# lyklarnir
print(einkunnirIslands.keys())
# gildin
print(einkunnirIslands.values())
# hlutirniar (lyklar og gildin)
print(einkunnirIslands.items())

# Finnum hlutinn með hæsta gildið (hæstu einkunn)
import operator
hluturMeðHæstaGildi = max(einkunnirIslands.items(),key=operator.itemgetter(1))
print(hluturMeðHæstaGildi)

# Hver fékk það?
print(hluturMeðHæstaGildi[0])

# Hvað fékk hann?
print(hluturMeðHæstaGildi[1])

# gleymdum Birki, bætum honum við (getum það af því að dictionaries eru dynamic)
einkunnirIslands['Birkir'] = 8
print(einkunnirIslands)
