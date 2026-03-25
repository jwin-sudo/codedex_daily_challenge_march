def wordle_guess(secret, guess):
  # Write code below 💖
  
  count = 0 
  for i in range(5):
    if secret[i] == guess[i]:
      count += 1
  
  return count 

print(wordle_guess('CODEX', 'COINS'))
