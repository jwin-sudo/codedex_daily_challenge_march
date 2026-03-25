'''
Cuddly Kittens 🐈
MARCH 23, 2026
Happy Monday! It’s National Cuddly Kitten Day! 😻

We are back with a Daily Challenge and... a Bonus Task! Let's gooo.

kitties!

You're helping kittens line up in a cozy play area. They only stay calm if their energy levels are similar. Otherwise, the purring stops, and chaos ensues.

You're given:

A list/array kittens, where kittens[i] represents the energy level of the i-th kitten
A number limit, the biggest difference between any two kittens in a calm group
A group of kittens is calm and can purr together if:

max energy−min energy≤limit
Return the length of the longest group of consecutive kittens that can stay calm. 🐾🐾🐾

Bonus Task: Snap a pic of your cat with Codédex for a chance to win a Codédex Crewneck! 📸

Examples
Example 1

Input:
kittens = [1, 3, 6, 7, 9]
limit = 3
Output: 3
The longest valid group is [6, 7, 9] because max - min = 9 - 6 = 3.

Example 2

Input:
kittens = [2, 3, 4, 5]
limit = 10
Output: 4
All kittens can stay together since max - min = 5 - 2 = 3 ≤ 10.
'''
def cuddly_kittens(kittens, limit):  
  left = 0 
  right = 0
  window_size = []
  max_size = float('-inf')

  while right < len(kittens):
    window_size.append(kittens[right])

    while max(window_size) - min(window_size) > limit:
      window_size.pop(0)
      left += 1
    
    max_size = max(max_size, right - left + 1)

    right += 1
  
  return max_size

kittens = [2, 3, 4, 5]
limit = 10

print(cuddly_kittens(kittens, limit))

