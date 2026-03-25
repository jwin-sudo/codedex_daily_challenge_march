'''
Pi Day 🥧
MARCH 14, 2026
It's March 14... Pi Day! Time to celebrate the math constant π (pi) and eat some yummy pies. 🥧

You and your friends are sharing a delicious pie at a bakery. You know the diameter of the pie and the number of friends. The pie needs to be cut into slices, so everyone gets a piece.

image

We'll keep today's Daily Challenge easy, so there's plenty of time to tackle the bonus task! 👀

Complete the function that calculates how much crust (circumference) each friend gets if the pie slices are shared evenly.

To solve this, you need to:

Google how to use π in Python or JavaScript (the focus here!).
Calculate the circumference of the pie.
Divide the slices evenly among friends.
Return the crust per friend, rounded to 2 decimal places.
The circumference formula is:

C=π×d
C = circumference
d = diameter of the pie
Examples
Example 1

Input:
diameter = 10
friends = 8
Output: 3.93
10 inches × π ÷ 8 friends ≈ 3.93 inches of crust per friend

Example 2

Input:
diameter = 12
friends = 5
Output: 7.54
12 inches × π ÷ 5 friends ≈ 7.54 inches of crust per friend
'''

import math
def cut_pie(diameter, friends):
  c = math.pi * diameter 
  return round(c / friends, 2)
  

