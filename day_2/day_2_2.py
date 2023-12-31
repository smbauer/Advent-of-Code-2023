# read in the input file
with open('input_day_2.txt') as f:
    lines = f.readlines()

    count = 0

    # for each line, separate the game number and the sets with the colour counts
    for line in lines:
        games = line.split(':')[-1].split(';')
        max_dict = { 'red': 0, 'green': 0, 'blue': 0}
        power = 1

        # loop through all the sets/runs in a game
        for game in games:
            # loop through each value in the set
            for run in game.split(','):
                cube_count = int(run.split()[0])
                colour = run.split()[-1]

                # update the dictionary to maintain the minimum number of each
                # colour required for each game
                if cube_count > max_dict[colour]:
                    max_dict[colour] = cube_count

        # calculate the power (product) of the min required colours for each game
        for num in max_dict.values():
            power *= num
        # sum up the powers of each game
        count += power
    print(f'{count=}')