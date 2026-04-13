def analyze(percentages):
  # Write code below 💖
  output = []
  dips = 0
  years = len(percentages)
  last_year = percentages[-1]
  first_year = percentages[0]

  last_three_years = sum(percentages[-3:]) / 3 
  first_three_years = sum(percentages[0:3]) / 3
  net_change_per_year = round((last_year - first_year) / (years - 1), 2)

  output.append(net_change_per_year)

  if last_three_years > first_three_years:
    output.append("improving")
  
  elif last_three_years == first_three_years:
    output.append("stagnating")
  
  else:
    output.append("declining")

  for i in range(1, len(percentages)):
    if percentages[i] < percentages[i-1]:
      dips += 1
  
  output.append(dips)
  return output

percentages = [31.0, 31.0, 33.0, 35.0, 36.0, 36.0, 36.2, 36.7, 37.1]
print(analyze(percentages))