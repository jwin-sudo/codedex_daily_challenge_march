'''
Flight Vouchers 🏖️
MARCH 18, 2026
March is Spring Break madness – Miami, Cancún, Hawaii. 😎 Everyone's chasing the sun!

If you've ever flown during this season, you know the struggle: airlines sometimes overbook. Luckily, if you’re flexible, they’ll offer flight vouchers to take a later flight. ✈️

Flight Voucher

Your task is simple: Pick the voucher that gives you the most value for your time. Specifically, you want the highest dollars per hour waited (voucher amount-to-delay ratio). 🎫

dollars per hour waited= 
hours delayed
voucher amount
​	
 
But you also have a maximum number hours you're willing to wait. Any option longer is out.

Given:

vouchers: a list of voucher amounts (in dollars)
delays: a list of corresponding delay times (in hours)
max_wait: the maximum hours you're willing to wait
Complete the function and return the index of the best option.

If two options tie, return the first one.
If none qualify, return -1.
Examples
Example 1

Input:
vouchers = [50, 120, 20]
delays = [2, 4, 1]
max_wait = 3
Output: 0
Option 0 is $25/hr. ✅ Option 1 has a 4-hour wait (over limit). Option 2 is $20/hr.

Example 2

Input:
vouchers = [300, 400, 1000]
delays = [5, 6, 10]
max_wait = 4
Output: -1
Every option exceeds the max wait. No deal is worth it. 😤
'''
def pick_voucher(vouchers, delays, max_wait):
  # Write code below 💖
  if all(delay > max_wait for delay in delays):
    return -1
  output = []
  for voucher, delay in zip(vouchers, delays):
    dollars_per_hour = voucher // delay
    if delay > max_wait:
      output.append(-1)
    else:
      output.append(dollars_per_hour)

  max_val = max(item for item in output if item is not None)
  final = []
  for index, avg in enumerate(output):
    if avg == max_val:
      final.append(index)
  if len(final) == 1:
    return final[0]
  elif len(final) >= 2:
    return final[0]
  
  return -1

vouchers = [300, 400, 1000]
delays = [5, 6, 10]
max_wait = 4

print(pick_voucher(vouchers, delays, max_wait))


