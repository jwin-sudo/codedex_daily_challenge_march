def blood_moon(timestamp):
  h, m = map(int, timestamp.split(":"))

  output = []

  for i in range(3):
    m += 48
    h += 2 + m // 60
    h = h % 24
    m = m % 60

    output.append(f"{h:02d}:{m:02d}")
  
  return output

print(blood_moon("01:00"))
  
  

blood_moon("01:00")