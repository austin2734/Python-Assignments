
# Program02
# Austin Riggs
# 8/28/23

print('\nRequirement 1\n')
print('This is Program02 - Austin Riggs')

print('\nRequirement 2 \n')
print('This program calculates strawberry sales for the month.')

print('\nRequirement 3 \n')
response = input('Do you have strawberry sales data to '
                 'add to this months sales total? (y/n) ')


totalPintsSold = 0

while(response.lower() == 'y'):

    print('\nRequirement 4 \n')
    qty = int(input('Enter the number of pints sold ' 
                    'to add to this months total: '))
    
    print('\nRequirement 5 \n')
    print('Updating pint sales total...')
    totalPintsSold += qty

    print('\nRequirement 6 \n')
    response = input('Do you have any more sales data to '
                     'add? (y/n) ')
    
print('\nRequirement 7 \n')
print('Total strawberry sales in pints: {}'.format(totalPintsSold))

print('\nRequirement 8 \n')
print('''My experience with Program02 went quite well. 
This assignment was pretty easy but helpful as I am still trying get back
into the swing of writing in python. I am looking forward to Program03.\n\n''')