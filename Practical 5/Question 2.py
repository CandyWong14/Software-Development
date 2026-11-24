message = input("Enter a string: ").strip()

# Count the num
words = message.split()
print("\nNo. of words:", len(words))

# Count the number of vowels
vowel = "aeiou"
message = message.lower()
print()
for character in vowel:
    print("No. of {}: {:d}".format(character, message.count(character)))

# Count average word length
total = 0
for word in words:
    total += len(word)
print("\nAverage: {:.2f}".format(total / len(words))) 