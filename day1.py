# import file input
import fileinput

# open the input file and set each line as a string in a list
f = open("puzzleinput.txt", "r")
lines = f.readlines()

# sum variable
sum = 0

# go through each line in the calibration values
for line in lines:
    curr_num = ""
    # locate the first digit in the line
    for l in line:
        if l.isdigit():
            curr_num += l
            break
    # locate the last digit in the line
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            curr_num += line[i]
            break
    
    # add the 2 digit value to the sum
    sum += int(curr_num)
        
print(sum)

# don't forget to close files!
f.close()