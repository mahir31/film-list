while True:
    x = input('> ')
    
    if x == 'print':
        with open("film.txt", "r") as x:
            y = [y.strip('\n') for y in (x.readlines())]
            for number, z in enumerate(y, 1):
                print(f'{number}. {z}')

    elif x == 'add':
        print('input title')
        x = input('> ')
        with open("film.txt", "a") as y:
            y.write(f'\n{x}')
        print(f'movie {x} has been added!')

    elif x == 'help':
        print("commands:\nadd - add a movie to the list\nprint - display movie list\nhelp - display command list\nexit - exit current runtime")

    elif x == 'exit':
        break

    else:
        print('invalid command! type "help" for command list')