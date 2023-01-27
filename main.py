import sys

# Get input and output file paths from command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]
result_lines = []

# Get list of all multiples of a number, which are less than a goal number
def getMultiples(number, goal):
    division = goal / number
    int_division = int(division)
    max_multiple = int_division if division == int_division else int_division + 1
    multiples = [number * i for i in range(1, max_multiple)]
    return multiples

# Prepare result list of numberA's and numberB's multiples
# 1. Concatenate 2 lists
# 2. Sort resulting in ascending order
# 3. Convert to string for later printing purposes to match the exact format, specified in the task
def getResultMultiples(numberA, numberB, goal):
    multiples = getMultiples(numberA, goal) + getMultiples(numberB, goal)
    multiples.sort()
    multiples = [str(a) for a in multiples]
    return multiples

# Open input file and read all its lines
with open(input_file, "r") as file:
    # Read all lines from the input file
    lines = file.readlines()

# Generate result lines list
for line in lines:
    numbers = list(map(int, line.strip().split()))
    multipliers = getResultMultiples(numbers[0], numbers[1], numbers[2])
    result_line = (numbers[2], multipliers)
    result_lines.append(result_line)

# Sort result lines list by total amount of multipliers
result_lines.sort(key=lambda a: len(a[1]))

# Open output file for writing
with open(output_file, "w") as file:
    for line in result_lines:
        # format line as specified in the task
        line_to_wright = f'{line[0]}:' + ' '.join(line[1])
        # Print formatted result line to the screen
        print(line_to_wright)
        # Write formatted result line to the output file
        file.write(line_to_wright + "\n")



