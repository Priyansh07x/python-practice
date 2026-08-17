sentence = "Learning Python is fun!"
lower_sen = sentence.lower()
x = 0 # counter
vowels = "aeiou"
for char in lower_sen:
    if char in vowels: # don't use ==, you need to use in keyword
        # == would compare one character against the entire string "aeiou"
        x += 1

print("Number of vowels:", x)
