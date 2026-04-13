'''
Hitchhiker's Guide 🪐
MARCH 11, 2026
·
Douglas Adams, author of the beloved sci-fi series The Hitchhiker's Guide to the Galaxy, was born on March 11th, 1952! The series follows the misadventures of the last surviving human.

It famously asks: what's the "Ultimate Answer to Life, The Universe, and Everything"?

Well... turns out it's the number 42. 🫠

marvin the robot

Your task: Find the minimum number of components whose sum is exactly 42.

If it’s impossible to reach exactly 42, return -1.

Choose wisely. The wrong combination might tear a hole in the space-time continuum!

Examples
Example 1

Input: [10, 20, 5, 15, 7]
Output: 3
One combination is 20 + 15 + 7 = 42. The minimum number of components needed is 3.

Example 2

Input: [1, 2, 3, 4, 5, 6]
Output: -1
No combination sums to exactly 42.

Example 3

Input: [42, 1, 1, 1]
Output: 1
The component 42 alone powers the drive.
'''

def minimum_components(components):
  # Write code below 💖
  output = []

  def backtrack(path, start):
    if sum(path) == 42:
      output.append(path[:])
      return 

    for i in range(start, len(components)):
      path.append(components[i])
      backtrack(path, i+1)
      path.pop()    
  
  backtrack([], 0)

  min_length = float('inf')

  if output == []:
    return -1

  for arr in output:
    if len(arr) < min_length:
      min_length = len(arr)
  return min_length

components = [1, 2, 3, 4, 5, 6]
print(minimum_components(components))

