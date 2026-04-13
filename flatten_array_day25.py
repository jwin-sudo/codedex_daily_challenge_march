'''
Flatten Array 🪜
MARCH 26, 2026

It’s the final week of the March Monthly Challenge, so let's do a classic: flattening an array.

This one stuck with me (Sonny) for a reason. Story time:

Back in 2017, I was a 26-year-old classroom teacher going through a brutal 6-hour onsite interview at Codecademy – five back-to-back interviews with a lunch walk with the team in between to see if "I coud hang". This was my dream job, so stakes were high. But I was ready.

I crushed the Curriculum Interview, walking through lesson plans, syllabuses, lecture slides I'd created. I nailed the Pedagogy Interview, breaking down my teaching frameworks. I slayed the Culture Interview, roleplaying a tough convo with an underperforming teammate and teaching something random on the spot. I won over the VP of Eng in the Eng Interview.

Everything was going smoothly… until the Technical Interview.

“Flatten this array.” 😬

flatten an array

And boy, did I bomb it. I still got the job, but this problem has stuck with me ever since.

Here's today's Daily Challenge:

Given a nested list/array (one that can contain numbers or other lists/arrays), sometimes deeply nested, your task is to flatten it into a "single-level" list/array.

Complete the function that returns a new list/array with all values flattened.

Give it a try and see if you can do what I struggled (ask Lumi for help!).

Examples
Example 1

Input: [1, [2, 3], 4, 5]
Output: [1, 2, 3, 4, 5]
The nested [2, 3] is flattened into the main list/array.

Example 2

Input: [1, 2, [3, [4, 5]], 6, 7]
Output: [1, 2, 3, 4, 5, 6, 7]
Multiple levels of nesting. Everything gets flattened.
'''
def flatten(input):
  # Write code below 💖
  output = []
  for item in input:
    if isinstance(item, int):
      output.append(item)
    
    elif isinstance(item, list):
      output.extend(flatten(item))
    
  return output

input = [1, [2, 3], 4, 5]
print(flatten(input))
