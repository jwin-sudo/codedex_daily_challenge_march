'''
Caesar Cipher 🏛️
MARCH 15, 2026
Oh snap! Today was Julius Caesar's assasination! ...In 44 BC, that is.

A Caesar Cipher, named after Julius himself, is a simple encryption technique where each letter in a message is shifted by a fixed number of positions in the alphabet.

caesar cipher

For example, with a shift of 3:

a becomes d
b becomes e
c becomes f
...
x becomes a
y becomes b
z becomes c
You can hide all sorts of things using a Caesar Cipher! 🤯

Complete the function that decodes a message that has been encoded using a Caesar Cipher.

It should accept the scrambled message and the shift value, and return the original text.

The message include only lowercase letters and spaces.

Examples
Battle Message

Input:
message = "dwwdfn dw gdzq"
shift = 3
Output: "attack at dawn"
The Beatles Conspiracy Theory

Input:
message = "ymj bfqwzx bfx ufzq"
shift = 5
Output: "the walrus was paul"
Secret Note

Input:
message = "ai wlsyph womt kcq gpeww"
shift = 4
Output: "we should skip gym class"
'''
def decode_message(message, shift):
  # Write code below 💖
  output = ''
  for char in message:
    if char != ' ':
      if 'a' <= char <= 'z':
        original = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        output += original
      elif 'A' <= char <= 'Z':
        original = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        output += original
    else:
      output += ' '
  
  return output 

print(decode_message('ai wlsyph womt kcq gpeww', 4))


