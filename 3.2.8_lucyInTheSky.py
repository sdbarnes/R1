# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
cut = "Princess"
clarity = "I"
color = "N"
carat = 4.2
budget = 92
preferred_cuts = ["Oval", "Princess", "Marquise", "Heart", "Pear"]


cost = 100
colorfactor = 0
clarityfactor = 0

# Color Rating: "D" (the best) to "Z" (the worst)
colorfactor = 1-((ord(color) - ord("D")) * .02)
print("Color:",ord(color))
print ("Color D:",ord("D"))
print ("Color Factor:",colorfactor)

# Clarity Rating: F (the best), IF, VVS, VS, SI, or I (the worst)
if clarity == "I":
    clarityfactor = 1
elif clarity == "SI":
    clarityfactor = 2
elif clarity == "VS":
    clarityfactor = 4
elif clarity == "VVS":
    clarityfactor = 8
elif clarity == "IF":
    clarityfactor = 16
elif clarity == "F":
    clarityfactor = 32
print ("Clarity Factor:",clarityfactor)

# Price Calculation
pricefactor = cost * colorfactor * clarityfactor
print ("Price Factor:",pricefactor)
price = pricefactor * carat
print ("Price:", price)

# Affordability Calculation
if (price <= budget) and (cut in preferred_cuts):
    print ("I'll take it!")
else:
    print ("No thanks")