#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aldursreikningar sem nota datetime pakkann
@author: helgi
"""


# ------------ flóknari útgáfa -------------
import datetime

# fæðingardagur 8. sept 1995
birthday = datetime.date(1995, 8, 9)

# dagsetningin í dag
today = datetime.date.today()

# Aldurinn er þá áramismunurinn 
age = today.year - birthday.year

# nema! ekki ef manneskjan hefur ekki átt afmæli í ár.. 
# athugum hvort hún hefur átt afmæli

# Hefur manneskjan átt afmæli í ár?
birthMonthHasPassed = today.month > birthday.month 
hasHadBirthdayThisMonth = today.month == birthday.month and today.day > birthday.day
hasHadBirthdayThisYear = birthMonthHasPassed or hasHadBirthdayThisMonth

# drögum frá 1 ár ef manneskjan hefur ekki átt afmæli
if not hasHadBirthdayThisYear:
    age = age - 1
    
print(age) 


# gerum fall úr flóknu útgáfunni:
import datetime

def calculateAge(birthdate):
    
    # dagsetningin í dag
    today = datetime.date.today()
    
    # Aldurinn er þá áramismunurinn 
    age = today.year - birthday.year
    
    # nema ekki ef manneskjan hefur ekki átt afmæli í ár
    
    # Hefur manneskjan átt afmæli í ár?
    birthMonthHasPassed = today.month > birthday.month 
    hasHadBirthdayThisMonth = today.month == birthday.month and today.day > birthday.day
    hasHadBirthdayThisYear = birthMonthHasPassed or hasHadBirthdayThisMonth
    
    # nema mínus 1 ár ef manneskjan hefur ekki átt afmæli
    if not hasHadBirthdayThisYear:
        age = age - 1
        
    return age
        
       
# fæðingardagur
birthday = datetime.date(1995, 4, 10)
age = calculateAge(birthday)
print(age)