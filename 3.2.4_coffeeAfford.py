# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:05:57 2019

@author: Scott
"""

cafe = "Octane"
balance = 2.16

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Atlanta is full of great coffee places. Unfortunately, great
#coffee is usually expensive. The variables above will
#contain a balance and a cafe name. Below are the prices of
#a cup of coffee at each of three locations:
#
# - Octane: $6
# - Galloway: $5
# - Starbucks: $4
# - Revelator: $3
# - Dunkin: $2
#
#Add some code above that will print one of the following
#two messages depending on whether the value of balance is
#high enough to buy a cup of coffee at the given cafe.
#
# - If it is sufficient, print "With [balance] dollars, I
#   can buy coffee at [cafe]"
# - If it is not sufficient, print "With [balance] dollars,
#   I cannot buy coffee at [cafe]"

#Add your code here!

afford = True
if cafe == "Octane":
    if balance < 6:
        afford = False
elif cafe == "Galloway":
    if balance < 5:
        afford = False
elif cafe == "Starbucks":
    if balance < 4:
        afford = False
elif cafe == "Revelator":
    if balance < 3:
        afford = False
elif cafe == "Dunkin":
    if balance <2:
        afford = False

if afford:
    print ("With",balance,"dollars, i can buy coffee at",cafe)
else:
    print ("With",balance,"dollars, i cannot buy coffee at",cafe)