#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fall til að reikna aldur á einfaldan máta
@author: helgi
"""

# Lítið og krúttlegt forrit sem (semi) reiknar aldur fyrir manneskju
birthYear = 1995
year = 2019
age = year-birthYear


# Hvernig gæti það litið út sem fall?
def calculateAgeSimply(birthyear):
    year = 2019
    age = year-birthYear
    return age


print(calculateAgeSimply(1995))
