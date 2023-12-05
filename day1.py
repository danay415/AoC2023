# import file input and regex module
import fileinput
import re
from enum import Enum

class Numbers(Enum):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'

# open the input file and set each line as a string in a list
f = open("puzzleinput.txt", "r")
lines = f.readlines()

# sum variable
sum = 0

# go through each line in the calibration values
for line in lines:
    num = ""
    # use regex lookahead to account for overlapping matches being consumed
    number_matches = re.findall(r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))', line)
    # check if the first number is a digit or written
    if number_matches[0].isdigit():
        num += number_matches[0]
    else:
        num += Numbers[number_matches[0].upper()].value
    # check if the last number is a digit or written
    if number_matches[-1].isdigit():
        num += number_matches[-1]
    else:
        num += Numbers[number_matches[-1].upper()].value
    # add the concatenated number to the sum
    sum += int(num)
print(sum)

# don't forget to close files!
f.close()

