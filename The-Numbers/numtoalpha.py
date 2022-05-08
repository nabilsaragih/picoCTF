from string import ascii_lowercase

letters = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start = 1)}
inv_letters = {str(index): letter for index, letter in enumerate(ascii_lowercase, start = 1)}
x = []
decoded = []

text = open("the-numbers/numbers.txt", "r")
x.append(text.read())
text.close()

for i in x: x_split = (i.split())

for i in x_split:
    if i in inv_letters:
        decoded.append(inv_letters[i])

print("".join(decoded))

