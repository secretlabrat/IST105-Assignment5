import sys
import re
from random import randint

_, number, message  = sys.argv

html = "<html>\n<head>\n<title>Assignment 5</title>\n</head>\n<body>\n"

number = int(number)
number_output = "The number {} is {}.".format(number, "even. Its square root is {}".format(number**0.5) if number % 2 == 0 else "odd. Its cube is {}".format(number ** 3), number ** 3)
binary_message = "Binary: "
binary_message += " ".join(format(ord(char), '08b') for char in message)
vowels = "Vowel Count: {}".format(len(re.findall(r'[aeiouAEIOU]', message)))

html += "Number Puzzle:<br>\n"
html += number_output + "<br>\n"
html += "Text Puzzle:<br>\n"
html += binary_message + "<br>\n"
html += vowels + "<br>\n"

html += "Treasure Hunt:<br>\n"
secret_number = randint(1, 100)
i = 1
min = 1
max = 100
while i < 6:
    guess = randint(min,max)
    if guess == secret_number:
        html += "Attempt {}: {} (Corret!)\n You found the treasure in {} attempt{}<br>\n".format(i, guess, i, "s" if i > 1 else "")
        break
    elif guess < secret_number:
        html += "Attempt {}: {} (Too low!)<br>\n".format(i, guess)
        min = guess + 1
    elif guess > secret_number:
        html += "Attempt {}: {} (Too high!)<br>\n".format(i, guess)
        max = guess - 1
    i += 1
else:
    html += "Sorry you lost! The secret number was {}<br>\n".format(secret_number)
html += "</body>\n</html>"

print(html)
