EncodedInputlines = []

# Open the file
with open('input.text', 'r') as file:
    for line in file:
        EncodedInputlines.append(line.strip())

dictionaryOfNumbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

# Create a new list for the strings of digits from each line
modifiedDigits = []
for line in EncodedInputlines:
    # Replace the words with numbers
    for key, value in dictionaryOfNumbers.items():
        line = line.replace(key, value)

    # Create a string to hold all digits from this line
    digitString = ''.join([char for char in line if char.isdigit()])
    modifiedDigits.append(digitString)

calibrationValues = []
# Loop through the modifiedDigits list
for digitString in modifiedDigits:
    if digitString:
        # Concatenate the first and last digit to form a two-digit number
        calibrationValue = int(digitString[0] + digitString[-1])
        calibrationValues.append(calibrationValue)

# Calculate the total sum of the calibration values
total = sum(calibrationValues)
print(total)