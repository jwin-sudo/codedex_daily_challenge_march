'''
Daylight Savings ⏰
MARCH 7, 2026

PSA: Daylight Savings starts tomorrow! You'll lose one hour of sleep. 😵‍💫

When the clock "springs forward" for Daylight Savings Time, most people end up sleeping an hour less than usual. This lost hour contributes to sleep debt, which is the cumulative gap between the sleep you planned and the sleep you actually got. Even small deficits can add up and impact mood, focus, and productivity.

sleep

At Codédex, our small but mighty team has been grinding on the Daily Challenge feature. We're tracking how much sleep debt everyone racks up before launch.

You’re given the hours each team member planned to sleep vs. actually slept over a week. 🛌💤

Sleep Debt=max(0, Planned Sleep−Actual Sleep)
Planned Sleep: Hours someone intended to sleep
Actual Sleep: Hours they actually got
max(0, x): Returns the larger of 0 or x.
Complete the function and return:

The total sleep debt for the week (including +1 Daylight Savings hour)
The longest streak of consecutive days with sleep debt
Python: Return two numbers. JavaScript: Return an array with two numbers.

⋆｡ ˚｡⋆｡ Sweet dreams ⋆｡˚｡⋆｡

Examples
Example 1: Sonny

Input:
planned = [7.5, 8, 7.5, 8, 8.5, 8, 7.5]
actual = [5, 12, 6, 6, 9, 8, 6.5]
Output:
8.0
2
Sleep debt: 2.5 + 0 + 1.5 + 2 + 0 + 0 + 1 = 7.0 hours (+1 Daylight Savings hour)
Longest streak: 2 days (day 3 and day 4)

Example 2: Asiqur

Input:
planned = [6, 6, 6, 6, 6, 8, 8]
actual = [5, 7, 2.5, 5, 5.5, 6, 4]
Output:
13.0
5
Sleep debt: 1 + 0 + 3.5 + 1 + 0.5 + 2 + 4 = 12.0 (+1 Daylight Savings hour)
Longest streak: 5 days (day 3 through day 7)
'''
def calculate_sleep_debt(planned, actual):
  # Write code below 💖
  left =  0
  right = 0
  total = 0 
  max_streak = 0 
  current_streak = 0

  while right < len(actual):
    sleep_debt = max(0, planned[right] - actual[right])
    total += sleep_debt

    if planned[right] - actual[right] > 0:
      current_streak += 1
      max_streak = max(current_streak, max_streak)
    else:
      current_streak = 0 
    
    right += 1

  return (total + 1, max_streak)

planned = [7.5, 8, 7.5, 8, 8.5, 8, 7.5]
actual = [5, 12, 6, 6, 9, 8, 6.5]

print(calculate_sleep_debt(planned, actual))