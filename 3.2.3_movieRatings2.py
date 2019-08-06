# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:25:44 2019

@author: Scott
"""

rating = "PG-13"
age = 13

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#The United States has a movie rating system that rates
#movies with one of five ratings: G, PG, PG-13, R, and NC-17.
#Although some of the ratings are not binding, imagine that
#you are a parent who decides on the following rules:
#
# - Any child can see a G-rated movie.
# - To see a PG-rated movie, your child must be 8 or older.
# - To see a PG-13-rated movie, your child must be 13 or older.
# - To see an R-rated movie, your child must be 17 or older.
# - Your child may never see an NC-17 movie.
#
#The variables above give a rating and a child's age. Use
#these variables to select and print one of these two
#messages based on the criteria above:
#
# - "You may see that movie!"
# - "You may not see that movie!"
#
#However, there's one trick: you may not use the 'and' operator
#anywhere in this code!


#Add your code here!
permission = True
if rating == "NC-17":
    permission = False
elif rating == "R":
    if age < 17:
        permission = False
elif rating == "PG-13":
    if age < 13:
        permission = False
elif rating == "PG":
    if age < 8:
        permission = False

if permission:
    print ("You may see this movie!")
else:
    print ("You may not see this movie!")
