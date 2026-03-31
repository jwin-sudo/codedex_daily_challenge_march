'''
My Best Streak 🔥
MARCH 31, 2026

You made it. 30 days of showing up for the Daily Challenges. And this is the final one! 🥲

Take a moment and breather. You should be proud of yourself. ヾ( ˃ᴗ˂ )◞ • *✰

3 characters gif

But let’s be real… it wasn’t perfect.

Some days you showed up and were locked in.
Some days you fell off.

Now the question is: What was your longest streak of consistency?

Given a list representing a user's daily progress:

'✅' = completed the challenge that day
'❌' = missed that day or took 5+ tries
Complete the function and return the length of the longest consecutive streak of '✅'.

Examples
Example 1

Input: ['✅', '✅', '✅', '✅', '✅', '✅', '❌']
Output: 6
Example 2

Input: ['✅', '✅', '❌', '✅', '✅', '✅', '❌', '❌', '✅', '✅']
Output: 3
'''
def longest_streak(progress):
  # Write code below 💖
  max_streak = 0
  current_streak = 0 
  for item in progress:
    
    if item == '✅':
      current_streak += 1
      max_streak = max(max_streak, current_streak)
    
    else:
      current_streak = 0 

  return max_streak

progress = ['✅', '✅', '❌', '✅', '✅', '✅', '❌', '❌', '✅', '✅']
print(longest_streak(progress))