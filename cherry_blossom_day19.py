'''
Cherry Blossoms 🌸
MARCH 20, 2026

Every spring, crowds flock to Japan to witness the breathtaking sakura season ⛩️, but timing is everything! Cherry blossoms are notoriously fleeting, and predicting peak bloom is a science.

Cherry Blossoms

Inspired by the real Japanese forecasting method, 積算温度, which tracks heat buildup after winter dormancy, blossoms open on the first day the 5-day rolling average temperature crosses 15°C. That means for each day, you look at it and the previous 4 days, compute their average, and check whether it surpasses 15.

Your task: Given a list of daily temperatures, complete the function so that it returns the day number (1-indexed) when the blossoms first bloom, or -1 if they never do.

🌸🍃🌸✨🌸🍃🌸✨🌸🍃🌸✨

Examples
Example 1

Input: temps = [10, 11, 13, 14, 16, 17, 18]
Output: 7
The temperatures steadily climb – by day 7, the 5-day rolling average finally crosses 15°C.

Example 2

Input: temps = [12, 14, 15, 16, 17, 11, 13]
Output: -1
The 5-day average never quite clears 15°C; the blossoms stay closed this year. 🥀
'''
def cherry_blossoms(temps):
  # Write code below 💖

  for i in range(0, len(temps), 1):
    window_temp = temps[i:i+5]
    avg = sum(window_temp) / 5 
    if avg > 15:
      return i+5
  
  return -1

temps =  [10, 11, 13, 14, 16, 17, 18]
print(cherry_blossoms(temps))