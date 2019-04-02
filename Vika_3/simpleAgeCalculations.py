#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fall til að reikna aldur á einfaldan máta
@author: helgi
"""

## Lítið og krúttlegt forrit sem (semi) reiknar aldur fyrir manneskju
#birthYear = 1995
#year = 2019
#age = year-birthYear

# Hvernig gæti það litið út sem fall?
def calculateAgeSimply(birthyear):
    year = 2019
    age = year-birthyear
    return age


print("aldurinn hans helga:", calculateAgeSimply(1995))

# Getum líka sótt aldurinn frá notenda:
print("minn aldur (næstum því): ", 
      calculateAgeSimply(int(input("fæðingarárið minn: "))))
