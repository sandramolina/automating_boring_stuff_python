# English to Pig Latin
# print('Enter the English message to translate into Pig Latin: ')
message = 'My .name is AL SWEIGART and I am 4,000 years old.'

# This is a tuple of strings
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatinWords = []

# The isalpha() method returns True if all the characters are alphabet letters (a-z).
for word in message.split():

    # Separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatinWords.append(prefixNonLetters)
        continue

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

print(pigLatinWords)