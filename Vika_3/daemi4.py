#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HD 4
@author: helgi
"""
import re

def add(x,D):
    # virkni: bætir staki í dictionary og telur fjölda staka
    # inntak: strengur x og Dictionary D
    # úttak: ekkert
    if x in D:
        D[x] += 1 # sama og að segja D[x] = D[x]+1
    else:
        D[x] = 1

def getWordsFromFile(fileName):
    # virkni: les skrá, hreinsar og einangrar orðin
    # inntak: skráarheiti
    # úttak: orðin
    myFile = open(fileName, 'r')
    texti = myFile.read()
    texti = re.sub(r'[-0-9{}&+()"=!.?:/|»©><#«,_+;%\[\]@$*\'\\^`~]', '', texti)
    texti = texti.lower()
    words = np.array(texti.split())
    return words

# __main__    
fileName = 'laxdaela_saga.txt'
words = getWordsFromFile(fileName)
wordCount = {}
for word in words:
    add(word,wordCount)
print(wordCount)
