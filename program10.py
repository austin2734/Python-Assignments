# Program10
# Austin Riggs
# 11/08/23

print('\nRequirement 1\n')
print('This is Program10 - Austin Riggs')

print('\nRequirement 2\n')
print('This program works with strings, uses regular expressions, '
      'and performs input validation tasks.')

print('\nRequirement 3\n')
print('String with 5 escape characters: \\ \\ \\ \\ \\')
print(r'Raw string with 5 escape characters: \ \ \ \ \ ')
print('''triple quotes example: "I'm doing well!"''')
print("""Mutliline comments example:
        Here is some text on a new line.
        Here is some more. No new line characters needed!""")

print('\nRequirement 4\n')
word = 'Howdy, earth!'
print('Character at [0]: %s' % (word[0]))
print('Character 5th index from end: %s' % word[-5])
print('Characters from index 3 to end: %s' % word[3:])
print('Characters up to but not including 7: %s' % word[:7])

print('\nRequirement 5\n')
if ('Howdy' in word):
    print("'Howdy' is located in the string!")
if('Hello' not in word):
    print("'Hello' is not located in the string.")

print('\nRequirement 6\n')
together = 'putting strings together'
plusOp = 'the + operator.'
interp = 'string interpolation.'
fString = 'f-strings.'
print( 'Example of ' + together + ' using ' + plusOp)
print('Example of %s using %s' % (together, interp))
print(f'Example of {together} using {fString}')

print('\nRequirement 7\n')
alpha = 'word'
alnum = 'word123'
num = '123'
space = ' '
title = 'This Is A Title'
print('isalpha() on string: ', alpha.isalpha())
print('isalnum() on mixed string: ', alnum.isalnum())
print('isdecimal() on string number: ', num.isdecimal())
print('isspace() on white space character: ', space.isspace())
print('istitle() on a string that is title cased: ', title.istitle())

print('\nRequirement 8\n')
aplhaList = ['apple', 'orange', 'banana', '123']
for i in aplhaList:
    if  i.isalpha():
        print(i)
    else:
        print('%s failed the isalpha() method.\n' % (i))

numList = ['1', '2', '3', 'blah']
for j in numList:
    if j.isdecimal():
        print(j)
    else:
        print('%s failed the isdecimal() method' % (j))


print('\nRequirement 9\n')
wordList = ['These', 'words', 'were', 'connected', 'together',
            'using', 'the', 'join', 'method']
print(' '.join(wordList))

print('\nRequirement 10\n')
wordString = 'These words were put into a list using the split method.'
listOfStrings = wordString.split()
print(listOfStrings)

print('\nRequirement 11\n')
word2 = ' Howdy '
print('Example of the partition() method: ', word2.partition('o'))
print('Example of the center() method: ', word2.center(20, '$'))
print('Example of the strip() method: ', word2.strip())
print("Example of ord() method on char: 'H': ", ord('H') )
print("Example of chr() method on num: '42': ", chr(42))

print('\nRequirement 12\n')
import pyperclip
pyperclip.copy('I copied this text.')
print('Here I paste some text: ', pyperclip.paste())

print('\nRequirement 13\n')
import re

validating = True
validList = ['gdrt-8493', 'DBTF-6253', 'UyHt-8326', 'YYrv-5329', 'qzrb-8264']
idRegex = re.compile(r'[a-zA-Z]{4}-\d{4}')
print('Please enter a user id with the first four characters being\n'
      'alphabetical, a hyphen, and four numeric charcters.\n')
print('Example: AbCd-1234\n')

while(validating):
    id = input('Please enter a user id in the requested format: ')
o
    print('\nRequirement 14\n')
    print('Checking if user id is in correct format...')
    valid = idRegex.search(id)
    if valid:
        print('\nRequirements 15 and 16\n')
        print('Checking if user id is valid...')
        if id in validList:
            print('\nRequirement 17\n')
            print('Thank you for entering your user id!')
            validating = False;
        else:
            print('ERROR: That is not a valid user id.\n')
    else:
        print('ERROR: Please enter a user id in the requested format.\n')


print('\nRequirement 18\n')
validatingNum = True;
countryCodes = {'376': 'Andorra', '591': 'Bolivia', '253': 'Djibouti',
                '995': 'Georgia', '370': 'Lithuania'}
phoneRegex = re.compile(r'(\d{3})-(\d{3})-(\d{3})-(\d{4})')
print('Enter a 13 digit phone number in the following format: ')
print('###-###-###-####')
print('Example: 365-771-456-2345')

while (validatingNum):
    phoneNum = input('Please enter a phone number: ')
    print('\nRequirement 19\n')
    print('Checking if phone number is in valid format...')
    validPhone = phoneRegex.search(phoneNum)
    if validPhone:
        print('\nRequirements 20 and 21\n')
        print('Checking if country code is valid...')
        code = validPhone.group(1)
        if code in countryCodes.keys():
            print('\nRequirement 22\n')
            print('Your call has been placed. Thank you '
                  'for calling %s' % countryCodes.get(code))
            validatingNum = False
        else:
            print('ERROR: That is not an accepted country code.\n'
                  'Please try again.\n')
    else:
        print('ERROR: That is not a valid phone number.\n'
              'Please enter number in the requested format\n')


print('\nRequirement 23\n')
import pyinputplus as pyip

pyip.inputStr(prompt='Enter a string: ')
pyip.inputInt(prompt='Enter a number: ')
pyip.inputYesNo(prompt="Enter word 'yes' or 'no': ")
pyip.inputBool(prompt="Enter word 'True' or 'False': ")
pyip.inputEmail(prompt='Enter a valid email address: ')

print('\nRequirement 24\n')

pyip.inputNum('Enter num a minimum of 5: ', min=5)
pyip.inputNum('Enter num a maximum of 10: ', max=10)
pyip.inputNum('Enter num greater than 3: ', greaterThan=3)
pyip.inputNum('Enter num less than 7: ', lessThan=7)
pyip.inputNum(prompt='You have two chances to enter a valid num: ', limit=2)
pyip.inputNum(prompt='You have 7 seconds to enter a valid num: ', timeout=7)
pyip.inputNum(prompt='Two chances to enter valid num or\n'
                     'one will be provided for you: ', limit=2, default='42')
pyip.inputNum(allowRegexes=[r'(null)'], prompt='Enter number or null: ')
pyip.inputNum(blockRegexes=[r'[23]'], prompt=('Enter num that does not '
                                               'contain numbers 2 or 3: '))

print('\nRequirement 25\n')
print('''I really enjoyed this assignment as it covered a lot of material I have 
not gone over before. I especially enjoyed the regular expression portion of this
assignment as was just working with these in another course and was not able to 
understand them at all. I learned a lot and am looking forward to 
the next assignment.''')




