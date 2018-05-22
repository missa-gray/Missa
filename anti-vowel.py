def anti_vowel(text):
  word = ""
  length = len(text)-1
  while length >= 0:
    for char in text:
      if char != "a" and char != "e" and char != "i" and char != "o" and \
      char != "u" and char != "A" and char != "E" and char != "I" and \
      char != "O" and char != "U":
        word += char
      length -= 1
  return word
