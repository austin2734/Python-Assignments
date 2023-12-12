# Program08
# Austin Riggs
# 10/19/23

print('\nRequirement 1\n')
print('This is Program08 - Austin Riggs')

print('\nRequirement 2\n')
print('This program keeps track of Pokémon characters.')

print('\nRequirement 3\n')
print('Defining Pokemon Class...')

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
print('Defining display_pokemon()')
def display_pokemon(pokemon_list):
    print('\nRequirement 5\n')
    count = 1;
    for pokemon in pokemon_list:
        print('Name of Pokemon #{}: {}'
              .format(count, pokemon.get_name()))
        print('\nAbility of Pokemon #{}: {}'
              .format(count, pokemon.get_ability()), end='\n\n')
        count += 1

if __name__ == '__main__':
    main()

else:
    pass




