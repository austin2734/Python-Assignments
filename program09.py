# Program09
# Austin Riggs
# 10/28/23

print('\nRequirement 1\n')
print('This is Program08 - Austin Riggs')

print('\nRequirement 2\n')
print('This program keeps track of Pokémon characters.')

print('\nRequirement 3\n')
print('Pokemon Class defined.')

class Pokemon:

    def __init__(self, name, ability):
        # assigns name to instance variable
        self.__name = name
        # assigns abillity to instance variable
        self.__ability = ability

    def get_name(self):
        return self.__name

    def get_ability(self):
        return self.__ability

def main():
    print('\n############### In main ################')
    pokemon_list = add_pokemon()
    display_pokemon(pokemon_list)

    print('\nRequirement 6\n')
    print('I got a lot out of this assignment as this is the first time I\n' +
          'have had a chance to use classes in python. Until now, I\n' +
          'never actually understood the __init__ and self keywords in\n' +
          'python code. I look forward to the next assignment.\n')




    print('################### Start of Program09 ############################')

    print('\nRequirement 1\n')
    print('This is Program09 - Austin Riggs')

    print('\nRequirement 2\n')
    print('This program keeps track of Pokémon characters, saves the data '
          'to a file, and displays the data from a file.')

    print('\nRequirement 3\n')
    print('Calling save_data() function.')
    save_data(pokemon_list)

    print('\nRequirement 4\n')
    print('Calling display_data() function')
    display_data()

    print('\nRequirement 5\n')
    print('I thought this assignment was intesting as it made me think\n' +
          'for a bit of how I should properly store text in a file so\n' +
          'that I could retrieve it later. I think the way I did it works\n' +
          'for this assignment but am open to feedback. Looking forward\n' +
          'to the next assignment.')


def add_pokemon():
    print('\nIn add_pokemon()\n')

    pokemon_list = []
    pokemon_number = 1

    more_pokemon = input('Do you have a pokemon to enter? (y/n) ').lower()
    while more_pokemon == 'y':
        pokemon_name = input('\nEnter name for Pokemon #{}: '
                             .format(pokemon_number))
        pokemon_ability = input('\nEnter ability for Pokemon #{}: '
                             .format(pokemon_number))

        new_pokemon = Pokemon(pokemon_name, pokemon_ability)

        pokemon_list.append(new_pokemon)

        pokemon_number += 1
        more_pokemon = input('\nAnother pokemon to enter? (y/n) '.lower())

    return pokemon_list


print('\nRequirement 4\n')
print('display_pokemon() defined.')
def display_pokemon(pokemon_list):
    print('\nRequirement 5\n')
    count = 1;
    for pokemon in pokemon_list:
        print('Name of Pokemon #{}: {}'
              .format(count, pokemon.get_name()))
        print('\nAbility of Pokemon #{}: {}'
              .format(count, pokemon.get_ability()), end='\n\n')
        count += 1


def save_data(pokemon_list):
    file = open('pokemon_file.txt', 'w')
    for pokemon in pokemon_list:
        file.write('{},{}\n'
              .format(pokemon.get_name(),pokemon.get_ability()))
    file.close()

def display_data():
    file = open('pokemon_file.txt', 'r')
    count = 1;
    print('\nPokemon from file:')
    for line in file:
        pokemonInfo = line.split(',')
        name = pokemonInfo[0]
        ability = pokemonInfo[1]
        print('\nName of Pokemon #{}: {}'
              .format(count, name))
        print('\nAbility of Pokemon #{}: {}'
              .format(count, ability), end='')
        count += 1
    file.close()





if __name__ == '__main__':
    main()

else:
    pass



