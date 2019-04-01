#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skráarskrif og lesning
@author: helgi
"""

import re
import numpy as np

# ------------- Prófum að skrifa nýja skrá --------------

# opnum skrá í skrifham
newFile = open('newFile.txt', 'w')

# skrifum í hana með fallinu .write()
newFile.write('Halló! Þetta er texti í skrá. \n')
newFile.write('Hér er texti sem fer í næstu línu \n')
newFile.write('(útaf tákninu sem ég nota alltaf aftast) \n')

# lokum skránni með .close()
newFile.close()



# ------------------ Prófum að lesa skrá -------------------

# opnum skrána laxdaela_saga.txt í lesham
myFile = open('laxdaela_saga.txt', 'r')

# lesum hana alla með fallinu .read()
allurTextinn = myFile.read()
print('Byrjunin á textanum í skránni okkar: \n', allurTextinn[0:500])
print('-----------------------------------')

# Getum hreinsað skránna af ýmsum táknum
hreinnTexti = re.sub(r'[-0-9{}&+()"=!.?:/|»©><#«,_+;%\[\]@$*\'\\^`~]', '', allurTextinn)

# Hafa þau öll í lágstöfum
hreinnTexti = hreinnTexti.lower()
                        
# Þá er auðvelt að einangra orðin, geymum sem numpy vigur fyrir þægindi                      
words = np.array(hreinnTexti.split())
print(words[0:100])

# lokum svo skránni
myFile.close()




