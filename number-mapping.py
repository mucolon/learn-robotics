# Write the missing code to make this function work
# Having this algorithm is important for making the robot motors work
# Feel free to use the AREPL extension or the green play button
# However like we saw in class, AREPL can be buggy so try using the green play button before pulling your hair out
# Hint: Making a graph of this function help visualize what you are trying to do (y = m * x + b)
# (-100, 0) , (0, 127 or 128) , (100, 255)
# m = (y2 - y1) / (x2 - x1)
# b = y - m * x
# Hint: In order to return an int, use the round() function
# Those hints should be enough to get you guys going, have fun!

import math


def map(input1, input2):
    '''Map input number from a [-100, 100] range to a [0, 255] range
    Args:      # Args is shorthand for arguments. Arguments in programming means inputs
        input1 (int|float): Number within [-100, 100] range
        input2 (int|float): Number within [-100, 100] range
    Return:
        numbers (int): 2-index list of integers within [0, 255] range
    '''
    numbers = [input1, input2]
    for i in range(2):
        numbers[i] = round(numbers[i] * 1.275 + 127.5)
        if numbers[i] < 0:
            numbers[i] = 0
        elif numbers[i] > 255:
            numbers[i] = 255
    return numbers


# Here's some examples of using the round() function
print("round() function examples")
print(f"round(0.4) = {round(0.4)}")
print(f"round(0.5) = {round(0.5)}")
print(f"round(0.6) = {round(0.6)}")

output = map(0, 0)
print("\nInput:\t\t [0, 0]")
print("Expected Output: [127, 127] or [128, 128]")
print(f"Output:\t\t [{output[0]}, {output[1]}]\n")

output = map(100, 100)
print("\nInput:\t\t [100, 100]")
print("Expected Output: [255, 255]")
print(f"Output:\t\t [{output[0]}, {output[1]}]\n")

output = map(-100, -100)
print("\nInput:\t\t [-100, -100]")
print("Expected Output: [0, 0]")
print(f"Output:\t\t [{output[0]}, {output[1]}]\n")

output = map(-50, 50)
print("\nInput:\t\t [-50, 50]")
print("Expected Output: [64, 191]")
print(f"Output:\t\t [{output[0]}, {output[1]}]\n")

output = map(50, -50)
print("\nInput:\t\t [50, -50]")
print("Expected Output: [191, 64]")
print(f"Output:\t\t [{output[0]}, {output[1]}]")
