with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def number_words(contents):
    words = contents.split()
    return len(words)

def number_character(contents):
    contents = contents.lower()
    count = {}
    for character in contents:
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    return count

print("--- Report of books/frankenstein.txt ---")
print(f"{number_words(file_contents)} words found in the document")

character_count = number_character(file_contents)

charkeys = list(character_count.keys())
charvalues = list(character_count.values())

alphakeys = []
alphavalues = []

for i in range(len(charkeys)):
    if charkeys[i].isalpha():
        alphakeys.append((charvalues[i], charkeys[i]))

alphakeys.sort(reverse = True)
for i in alphakeys:
    print(f"The '{i[1]}' character was found {i[0]} times")
print("--- End report ---")