'''
Ring Ring ☎️
MARCH 10, 2026

Alexander Graham Bell, inventor of the first practical telephone, once wrote in a letter to his father: "The day is coming when telegraph wires will be laid on to houses just like water or gas – and friends converse with each other without leaving home". 🤯

He was feeling inspired because 150 years ago on this day March 10th, 1876, he had just said the first words ever transmitted through a telephone to his assistant Thomas Watson:

"Mr. Watson, come here, I want to see you."

Alexander Graham Bell

In today's Daily Challenge, we are looking at phone transcripts.

Complete the function that counts the number of unique words in a phone call.

Words are separated by spaces, and punctuation should be ignored. Treat words as the same regardless of capitalization.

Examples
Example 1

Input: "Mr. Watson, come here, I want to see you."
Output: 9
There are 9 unique words in the phone call transcript.

Example 2

Input: "Hello Neil and Buzz, I am talking to you by telephone from the Oval Room at the White House, and this certainly has to be the most historic telephone call ever made."
Output: 27
There are 27 unique words because "the", "and", "to", "telephone" are repeated.
'''
import re 
def find_unique_words(transcript):
  if transcript == "":
    return 0
  # Write code beleow 💖
  cleaned = re.sub(r"[^\w\s']", '', transcript)
  cleaned = cleaned.lower()
  total = 0 
  words = cleaned.split(' ')
  words = list(set(words))
  

  for word in words:
    total += words.count(word)

  return total 
transcript = "Mr. Watson, come here, I want to see you."
find_unique_words(transcript)
  