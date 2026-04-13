'''
Green Chicago River ☘️
MARCH 17, 2026
Happy St. Patrick's Day! 🥳

Every year, the Chicago River is dyed green to celebrate this festive holiday.

Chicago

The river is colored using approximately 40 pounds of a secret, eco-friendly, vegetable-based powder that appears orange but turns brilliant green upon contact with water!

The dye starts at a few specific points... but the Windy City lives up to its name. 🌬️ Every hour, each green patch drifts one position to the right, spreading the color across the river.

Given the initial state of river and a number of hours, complete the function and return what the river looks like after the dye drifts downstream.

Sláinte! 🍻

Examples
Example 1

Input:
river = ['💧', '☘️', '💧', '💧', '💧', '☘️', '💧', '💧']
hours = 1
Output: ['💧', '☘️', '☘️', '💧', '💧', '☘️', '☘️', '💧']
After 1 hour, each ☘️ drifts one spot to the right.

Example 2

Input:
river = ['☘️', '💧', '💧', '💧', '💧', '☘️', '💧', '💧']
hours = 3
Output: ['☘️', '☘️', '☘️', '☘️', '💧', '☘️', '☘️', '☘️']
After 3 hours, each ☘️ has drifted 3 spots to the right.

💡 Fun fact: The Chicago River's dyed green every year since 1962, except 2020 due to COVID.
'''

def lucky_river(river, hours):
  # Write code below 💖
  i = 0
  while i < len(river):
    j = 0 
    if river[i] == '☘️':
        j = 1
        count = 1
        while count <= hours and (i + j) < len(river):
            river[i+j] = '☘️'
            j += 1
            count += 1
        i = i + j
    else:
        i += 1
        
  return river

river = ['☘️', '💧', '💧', '💧', '💧', '☘️', '💧', '💧']
hours = 3

print(lucky_river(river, hours))

    