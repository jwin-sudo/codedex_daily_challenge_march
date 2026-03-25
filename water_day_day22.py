'''
Water Day 💧
MARCH 22, 2026
Happy World Water Day! 🌍 Every year on March 22nd, the United Nations draws attention to the global water crisis – over 2 billion people live without access to clean water at home.

One silent culprit? Leaky pipes. The UN estimates that up to 45% of water is lost to bad infrastructure before it ever reaches a home. Every hour, a small percentage seeps out.

Water

Each hour, a pipe loses a fixed percentage of its current volume using this formula:

new volume=current volume×(1− 
100
leak
​	
 )
But pipes also have a minimum pressure threshold: once the volume drops below this level, the pipe has failed and water stops flowing entirely. 💥

Given:

A starting volume
A leak percentage per hour
A number of hours
A minimum pressure threshold
Complete the function and return the volume of water remaining after all hours have passed, rounded to 2 decimal places.

If the pipe fails before time is up, return -1. The pipe is done. 💧

Examples
Example 1

Input:
volume = 1000
leak = 5
hours = 3
threshold = 100
Output: 857.38
Applying the formula each hour: 1000 → 950 → 902.50 → 857.38. Never hits the threshold!

Example 2

Input:
volume = 200
leak = 30
hours = 6
threshold = 100
Output: -1
A 30% leak compounds fast; the volume crashes below 100 within 6 hours. Pipe failed! 💥
'''
def leaky_pipe(volume, leak, hours, threshold):
  new_volume = 0 
  for _ in range(hours):
    volume = volume * (1-(leak/100))
    new_volume = volume
  
  if new_volume < threshold:
    return -1
  return round(new_volume,2)

print(leaky_pipe(1000, 5, 3, 100))

