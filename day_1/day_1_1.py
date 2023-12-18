INFILE = 'input_day_1.txt'

# read in the input file
with open(INFILE, 'r') as f:
    lines = f.readlines()
    # list containing the digits found in the whole file
    num_list = []
    
    # loop through each line in the input file
    for line in lines:
        # list containing the digits found in each line
        numbers = []

        # loop through each character in the line
        for char in line:
            if char.isdigit():
                # if the character is a number, add it to the numbers list
                numbers.append(char)
            else: pass
        if numbers:
            # if there are numerical digits in the line, add the first and last
            # digits to the num_list
            num_list.append(int(numbers[0] + numbers[-1]))
    # add up all the values and print result
    print(sum(num_list))