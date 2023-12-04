EncodedInputlines = []

# Open the file
with open('input.text', 'r') as file:
    for line in file:
        EncodedInputlines.append(line.strip())

calibrationValues = []
# Loop through the list and find the first and last digit of each line and concatenate them.
for line in EncodedInputlines:
    digits = [char for char in line if char.isdigit()]
    if digits:
        # Concatenate the first and last digit to form a two-digit number
        calibrationValue = int(digits[0] + digits[-1])
        calibrationValues.append(calibrationValue)

# Calculate the total sum of the calibration values
total = sum(calibrationValues)
print(total)