def prompt_input_options(option_list):
    # Use when a user must select an option
    valid_list = [x+1 for x in range(len(option_list))]
    
    i = 0
    for option in option_list:
        i+=1
        print(f'({i}) {option}')

    while True:
        try:
            # value = input('Select an option: ').strip().upper()
            value = int(input('Select an option: '))
        except ValueError:
            print('Please enter a valid option.')
            continue

        if value not in valid_list:
            print('Please enter a valid option.')
            continue
        else:
            break

    user_choice = option_list[value-1]
    
    return user_choice
