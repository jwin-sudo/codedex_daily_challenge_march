'''
The Infinite Monkey Theorem is one of math's most beloved thought experiments!

Picture this: If a monkey sits at a typewriter and randomly hits keys forever, it will eventually type the complete works of Shakespeare!

Obviously we can't wait forever 🤨, so we're going to measure just how close our monkey is getting. But here's the twist, our monkey types a string of text much longer than the target. Shakespeare might be hiding somewhere in the middle without the monkey even knowing it!

For each valid starting position in the attempt, we check a window of characters the same length as the target and calculate a similarity score — the percentage of characters that match the target in the exact same position.

For an example with target = "hamlet":

attempt = "xxhamxet"
           |||
           ||└─── window at index 2: "hamxet" → 83.33% ✅ Best!
           |└─── window at index 1: "xhamxe" → 0% ❌ Closer, but matches are off by one
           └─── window at index 0: "xxhamx" → 0% ❌ Too early, so nothing lines up
Slide the window across every valid position and find the highest similarity score. From that score, estimate how many attempts it would take the monkey to stumble onto that window at 100%:

attempts= 
( 
100
similarity
​	
 ) 
length
 
1
​	
 
Given a target string and a longer attempt string, return a dictionary/object with:

best_index : the starting index of the most similar window.
similarity : the highest similarity percentage rounded to 2 decimal places, if needed.
attempts : theoretical attempts to hit 100% at that rate, rounded to the nearest whole number. If the best similarity is 0%, set attempts to null. 🐒
*Round similarity to 2 decimal places for the final output only. Use the unrounded similarity value when calculating attempts.

If two windows have the same similarity, return the first one.
'''

def infinite_monkey(target, attempt):
    # Write code below 💖
    left = 0 
    right = left + len(target) - 1
    output = {}
    max_similarity = float('-inf')
    while right < len(attempt):
        matched = 0 
        for char_a, char_b in zip(target, attempt[left:right+1]):
            if char_a == char_b:
                matched += 1
        current_similarity = matched / (right - left + 1) * 100
        

        if current_similarity > max_similarity:
            max_similarity = current_similarity
            output['best_index'] = left
            output['similarity'] = round(max_similarity, 2)

            if max_similarity == 0:
                output['attempts'] = None
            else:
                output['attempts'] = round(1 / (max_similarity / 100) ** (right - left + 1))
        



        left += 1
        right += 1

    return output

target = 'hamlet'
attempt = 'xxhamxetxxxx'
print(infinite_monkey(target, attempt))