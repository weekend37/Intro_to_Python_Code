#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 13:44:45 2019

@author: helgi
"""
# Hlöðum niður pakkanum math
import math

# Reiknum flatarmál hrings
radius = 5
flatarmal = radius**2*math.pi
print("Flatarmál hrings með radius ", radius, " er ", flatarmal, sep="")

# Reiknum sin(pi/2)
radianar = math.pi/2
gradur = radianar/math.pi*180
print(radianar, " radíanar eru ", gradur, " gradur",sep="")
print("sin af ", gradur, " gráðum er ", math.sin(radianar), sep="")

