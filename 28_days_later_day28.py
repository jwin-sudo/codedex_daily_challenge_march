'''
28 Days Later is a British series about a post-apocalyptic world overrun by a fast-spreading virus. This includes 28 Days Later (2002), 28 Weeks Later (2007), and 28 Years Later (2025).

28 Years Later

A dangerous virus is spreading across a city. So it goes... 🦠

Each day, infected people pass the virus to nearby healthy people. Your goal is to determine how many days it takes to infect everyone... or if it’s impossible.

Given a grid representing a city:

' ' = empty space
'👤' = healthy person
'🧟' = infected person
Each day, any infected person '🧟' infects adjacent healthy folks '👤' (up, down, left, right).

Complete the function and return:

The minimum number of days needed to infect all people.
OR -1 if some people can never be infected.
Examples
Example 1

Input:
[
  ['👤', ' ', '🧟'],
  ['🧟', '👤', ' '],
  [' ', '👤', '👤']
]
Output: 3
In three days, everyone is infected. We're cooked! 🧟 🧟‍♀️ 🧟‍♂️

Example 2

Input:
[
  ['👤', ' ', ' ', '🧟'],
  [' ', '👤', '👤', ' '],
  [' ', '👤', ' ', '👤'],
  ['👤', '👤', '👤', ' ']
]
Output: -1
'''

from collections import deque
def days_to_infect(city):
  # Write code below 💖
  queue = deque()
  rows = len(city)
  columns = len(city[0])
  days = 0 
  healthy_count = 0 

  for r in range(rows):
    for c  in range(columns):
      if city[r][c] == '👤':
        healthy_count += 1
      elif city[r][c] == '🧟':
        queue.append((r,c))

  if healthy_count == 0:
    return 0 
  
  while queue:
    days += 1
    for _ in range(len(queue)):
      r, c = queue.popleft()
      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = dr + r
        nc = dc + c

        if 0 <= nr < rows and 0 <= nc < columns and city[nr][nc] == '👤':
          city[nr][nc] = '🧟'
          healthy_count -= 1
          queue.append((nr, nc))
    
    if healthy_count == 0:
      return days 
  
  return -1

city = [
  ['👤', ' ', ' ', '🧟'],
  [' ', '👤', '👤', ' '],
  [' ', '👤', ' ', '👤'],
  ['👤', '👤', '👤', ' ']
]

print(days_to_infect(city))
  