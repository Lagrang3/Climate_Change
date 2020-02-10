#!/usr/bin/env python3

# (date,height cm)
events=[
(194,1966),
(187,2019),
(166,1979),
(158,1986),
(156,2008),
(156,2018),
(154,2019),
(151,1951),
(150,2019),
(149,2012),
(148,2018),
(147,1936),
(147,2002),
(145,1960),
(145,2009),
(144,1968),
(144,2000),
(144,2009),
(144,2010),
(144,2019),
(143,2012),
(143,2013),
(143,2019),
(142,1992),
(140,1979)]

events.sort(key=lambda x: x[1])

years = [ y for (h,y) in events  ]
height= [h for (h,y) in events ]

import matplotlib.pyplot as plt

plt.figure()
plt.xlabel('date')
plt.ylabel('height (cm)')
plt.plot(years,height,'o',markersize=3)

plt.savefig('acqua_alta.png')
