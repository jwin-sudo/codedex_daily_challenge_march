'''
Ye Olde Emoticons 📰
MARCH 30, 2026
·
6
0
On March 30, 1881, Puck Magazine, a satirical American newspaper, published the first use of emoticons in print. Emoticons are text-based expressions created using keyboard characters.

These days, emoticons have mostly been replaced by emojis. But we still love them! <3

image

Given a text string message, complete the function that analyzes the text and reports the overall mood based on the emoticons it contains. :o

🙂 Happy Emoticons

:) → Classic smiley face
:p → Playful / Tongue out
XD → Laughing / Very happy
:3 → Cute / Mischievous (inspiration behind Codédex bot!)
<3 → Heart
\m/ → Rock on
🙁 Sad Emoticons

:( → Frown
:'( → Crying
t(-.-t) → Middle fingers (my personal favorite!)
Each happy emoticon → +1. Each sad emoticon → -1.

Return the final score.

Examples
Example 1:

Input: "i'm going to see a psychic tonite :)"
Output: 1
Example 2:

Input: "dancing with friends at the club! XD come thru <3 <3"
Output: 3
Fun Fact: The first modern emoticon was proposed in 1982 by Scott Fahlman, who suggested using :-) and :-( on a university message board to distinguish jokes from serious posts.
'''
def emoticons_mood(message):
  # Write your code here 💖
  happy_emoticons = [':)', ':p', 'XD', ':3', '<3', '\m/']
  sad_emoticons = [':(', ':\'(', 't(-.-t)']

  score = 0

  for emo in happy_emoticons:
    score = score + message.count(emo)
  
  for emo in sad_emoticons:
    score = score - message.count(emo)
  
  if score >= 0:
    return score
  else:
    return -1

message = "let's freaking go!!! \\m/\\m/\\m/\\m/\\m/\\m/ t(-.-t)"

print(emoticons_mood(message))