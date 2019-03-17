#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 15:11:19 2019

@author: helgi
"""

import numpy as np

# -------------------- Vigrar --------------------  

# búum til vigur af tölum með numpy.array()
talnaVigur = np.array([3,4,54,40,90])

# vísum í stak vigurs alveg eins og í stök lista
print(talnaVigur[3])

# og líka breytt þeim
talnaVigur[3] = 999999
print(talnaVigur)


# -------------------- Fylki --------------------  

# getum búið til fylki líka
talnaFylki = np.matrix([[1,2,3],[4,5,6]])
print(talnaFylki)

# vísum í stak fylkis á tvívíðan máta: [lína,dálkur]
print(talnaFylki[0,1])


# ---------- Leikum okkur með vigra -------------

# búum til vigur af tölum með numpy.array()
talnaVigur = np.array([3,4,54,40,90,2,100,6,30,3])

# summa stakana
print(sum(talnaVigur))

# meðaltal vigursins
print(np.average(talnaVigur))

# staðalfrávik
print(np.std(talnaVigur))


# ----------------- Rökvigrar -------------------

# Eru stökin stærri en 10?
print(talnaVigur>10)

# Hvað eru mörg stök stærri en 10?
print(sum(talnaVigur>10))

# Hvaða stök?
print(np.where(talnaVigur>10))


# --------------- Slembivigrgar -----------------

# Notum numpy pakkann til að gera slembivigur
# gerum vigur af slembiheiltölum á bilinu [0,11) af lengd 5
slembiVigur = np.random.randint(0,11,5)

print(slembiVigur)







