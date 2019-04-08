#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skoðum hvernig við getum lesið inn .csv skrár með pandas.
Kíkjum á gögn fyrir hlutabréf icelandair síðustu ár.
Prófum svo að teikna smá með pakkanum matplotlib
@author: helgi
"""

import datetime
import pandas as pd
import matplotlib.pyplot as plt

# lesum skránna sótta af keldunni: https://www.keldan.is/market/shares/ICEAIR 
iceair_data = pd.read_csv("iceair.csv")

# skoðum hvernig fyrstu línurnar í gögnunum líta út
print(iceair_data.head())

# Hvað er meira hægt að vita um gagnasafnið okkar?
print(iceair_data.info())

# breytum nöfnunum á dálkunum í eitthvað þægilegra
iceair_data.columns = ['DateTime', 'Verd', 'Magn']

# Breytum datetime breytunni í date:
iceair_data['DateTime'] = pd.to_datetime(iceair_data['DateTime'])

# getum tekið út gildi sem vantar (NaN) með .dropna()
iceair_data = iceair_data.dropna()

# Tékkum núna hvernig gögnin líta út...
print(iceair_data.head())
print(iceair_data.info())
# ...miklu betra!

## Nokkrar leiðir til að nálgast dálka, t.d. fyrir dálkinn DateTime:
# print(iceair_data['DateTime'])
# print(iceair_data.DateTime)
# print(iceair_data.loc[:,'DateTime'])

### Skoðum smá tölfræði

# Hvert er hæsta verðið sem icelandair hefur fengið?
print("Hæsta verð:" , max(iceair_data['Verd']))

# Hvað er meðal magnið yfir allt tímabilið?
print("Meðalmagn:", iceair_data['Magn'].mean())

# Getum filterað gagnasafnið okkar
# skoðum gögnin bara síðan wow fór á hausinn
wow_hrun_date = datetime.datetime(2019, 3, 28)
iceair_since_wow_hrun = iceair_data[iceair_data['DateTime'] > wow_hrun_date]

# -------- Prófum að teikna með matplotlib --------


# Teiknum gengi Iceland Air síðustu 5 ár
iceAirStock = plt.plot(iceair_data['DateTime'],iceair_data['Verd'])
plt.show()

# Teiknum gengi Iceland Air síðan wow varð gjaldþrota
iceAirStockSinceWOW = plt.plot(iceair_since_wow_hrun['DateTime'],
                               iceair_since_wow_hrun['Verd'] )
plt.show()
