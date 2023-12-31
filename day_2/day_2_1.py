# read in the input file
with open('input_day_2.txt') as f:
    lines = f.readlines()
    # dict with maximum values for each colour
    max_dict = { 'red': 12, 'green': 13, 'blue': 14}

    count = 0

    for line in lines:
        # for each line, separate the game number and the sets with the colour counts
        game_num = int(line.split(':')[0].split()[-1])
        games = line.split(':')[-1].split(';')
        valid = True

        # loop through all the sets/runs in a game
        for game in games:
            # loop through each value in the set
            for run in game.split(','):
                cube_count = int(run.split()[0])
                colour = run.split()[-1]

                # set the valid flag to false if the set exceeds the maximum possible values
                if cube_count > max_dict[colour]:
                    valid = False

        # increment the count/score if it's a valid game
        if valid:
            count += game_num

    print(f'{count=}')