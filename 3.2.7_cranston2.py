# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 19:24:38 2019

@author: Scott
"""
story = "A"
text = "D"
role = "A"
director = "B"
cast = "B"
ss = 0
ts = 0
rs = 0
ds = 0
cs = 0
score = 0
if story == "A":
    ss=6
elif story == "B":
    ss=5
elif story == "C":
    ss=4
elif story == "D":
    ss=2
if text == "A":
    ts=5
elif text == "B":
    ts=4
elif text == "C":
    ts=3
elif text == "D":
    ts=1
if role == "A":
    rs=4
elif role == "B":
    rs=3
elif role == "C":
    rs=2
elif role == "D":
    rs=1
if director == "A":
    ds=3
elif director == "B":
    ds=2
elif director == "C":
    ds=1
if cast == "A":
    cs=2
elif cast == "B":
    cs=1
score = ss+ts+rs+ds+cs
if score<12:
    print(score)
    print ("Pass")
elif score <14:
    print(score)
    print ("On the bubble")
elif score <19:
    print(score)
    print ("Seriously consider")
elif score <20:
    print(score)
    print ("Must do")
else:
    print(score)
    print ("Perfect score")


