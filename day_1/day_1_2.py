INFILE = 'input_day_1.txt'

# dictionary with word-number mappings
num_dict = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
    }

# read in the input file
with open(INFILE, 'r') as f:
    lines = f.readlines()
    # list containing the digits found in the whole file
    num_list = []
    
    # loop through each line in the input file
    for line in lines:
        # list containing the digits found in each line
        numbers = []
        # string buffer for each line
        s = ''

        # loop through each character in the line
        for char in line:
            if char.isdigit():
                # if the character is a number, add it to the numbers list
                numbers.append(char)
            else:
                # if not a number, add it to the string buffer
                s += char
                for k,v in num_dict.items():
                    # check to see if the most recently added characters are
                    # found in the number mapping dict (aka spell a digit)
                    if s.endswith(k):
                        numbers.append(v)
        if numbers:
            # if there are numerical digits in the line, add the first and last
            # digits to the num_list
            num_list.append(int(numbers[0] + numbers[-1]))
    # add up all the values and print result
    print(sum(num_list))