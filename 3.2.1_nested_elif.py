# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 10:31:43 2019

@author: Scott
"""
# - If you've been dating for at least 4 years, give them a
#   dog ("dog").
# - If you've been dating for at least 1 year but less than
#   4 years, give them a watch ("watch").
# - If you've been dating for at least 6 months but less than
#   1 year, give them concert tickets ("concert tickets").
# - If you've been dating for at least a day but less than 6
#   months, give them candy ("candy").
# - If aren't actually dating, go big or go home: give them
#   a yacht to sail away together ("yacht").
years = 0
months = 5
days = 0
if years>4:
    print("dog")
elif years >=1:
    print("watch")
elif months >= 6:
    print ("concert tickets")
elif months or days >=1:
    print("candy")
else:
    print ("yacht")
