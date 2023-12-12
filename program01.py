
print('\nRequirement 1\n')

print('This is Program 1 - Austin Riggs')

print('\nRequirement 2 \n')

print('Please enter the information requested\n')
lastName = input('Last name: ')
hometown = input('Hometown: ')
occupation = input('Occupation: ')
hobby = input('Hobby: ')


print('\nRequirement 3\n')

print('Hello {}!'.format(lastName))
print('From {}.'.format(hometown))
print('I hope you like being a(n) {}.'.format(occupation)) 
print('{} sounds like an interesting hobby.'.format(hobby))


print('\nRequirement 4\n')

print('Alternative Output\n')
print('Hello', lastName, '!')
print('From',hometown, '.')
print('I hope you like being a(n)', occupation) 
print( hobby + ' sounds like an interesting hobby.')

print('\nRequirement 5\n')

print('More Options\n')
print('Hello1 ', lastName, '!')
print('Hello2 ', lastName, '!', sep='')
print('Hello3 ', lastName, '! ', end = '', sep = '') 
print('Hello4 ', lastName, '! ', end = '', sep = '') 
print('Hello5 ', lastName, '! ', sep = '') 


print('\nRequirement 6\n')

print('''This program was a simple but it was helpful as I have not written   
anything in python for sometime now. In this program, I learned a few new 
print formatting methods such as the .format() method that makes printing text 
a lot eaiser. I look forward to continuing to refresh my python skills and hopefully
learn a lot more throughout the semester.''')

