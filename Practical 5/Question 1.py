message = input("Enter a string: ").strip() # Remove the space at the beginning and end of the string

words = message.split() # Split the string into a list of words
acronym = ""

for word in words:
    acronym += word[0].upper()

print("The acronym for '{}' is '{}'".format(message.strip(), acronym))