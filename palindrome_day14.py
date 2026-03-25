'''
Palindrome 🏎️
MARCH 13, 2026
Today is March 13th (3/13). And guess what? That's actually a palindrome! 😮

A palindrome is a sequence of values that reads the same forwards and backwards. Think words like "racecar", "taco cat", or "level" and numbers like 2002 or 12321.

palindrome

Given a string, complete the function that checks whether it's a palindrome.

Python: Return True if it is, False if it isn't.
JavaScript: Return true if it is, false if it isn't.
Ignore spaces and capitalization.

Assume the string only contains letters (a-Z) and numbers (0-9). No punctuation.

Examples
Example 1

Input: "racecar"
Output: True
Example 2

Input: "Was it a car or a cat I saw"
Output: True
Example 3

Input: "11 11" (make a wish!)
Output: True
Example 4

Input: "12345"
Output: False
Remember that it's lowercase true/false for JavaScript.
'''
def check_palindrome(sequence):
  # Write code below 💖
  lowercase_sequence = sequence.lower()
  rm_space = ''.join(lowercase_sequence.split(' '))
  
  start = 0
  end = len(rm_space)-1

  while start <= end:
    if rm_space[start] != rm_space[end]:
      return False 
    start += 1
    end -= 1

  return True

print(check_palindrome('Was it a car or a cat I saw'))

  
