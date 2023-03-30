alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = dict()
characters = dict()
for i in range(26):
    numbers[i] = alphabets[i]
    characters[alphabets[i]] = i

#Rewrite this example according to your needs
example_word = "David"

print(f"Example: {example_word}")
for i in range(len(example_word)):
    if i == len(example_word) - 1:
        print(characters[example_word[i].upper()])
    else:
        print(characters[example_word[i].upper()], end=", ")

#Rewrite this example according to your needs
example_numbers = "1 17 8 0 13"

print(f"Example: {example_numbers}")
example_numbers = example_numbers.split(" ")
for number in example_numbers:
    print(numbers[int(number)], end="")
