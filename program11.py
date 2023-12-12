# Program11
# Austin Riggs
# 11/09/23

from pathlib import Path
import pyinputplus as pyip
import pyperclip
import shutil
import zipfile
import os
import send2trash

print('\nRequirement 1\n')
print('This is Program11 - Austin Riggs')

print('\nRequirement 2\n')
print('This program demonstrates reading, writing, and organizing files.')

print('\nRequirement 3\n')
print('Current working directory:')
print(Path.cwd())

print('\nRequirement 4\n')
print('What do you wish the directory storing your files to be named?')
print('NOTE: Please do not use special characters in this name.')
# all special characters are blocked from being used for dir name
dirName = pyip.inputStr( blockRegexes=[r'[^a-zA-Z0-9]'],
                         prompt='Enter the directory name to be created: ')
newDir = Path.cwd() / Path(dirName)
newDir.mkdir()
print(f'{dirName} created!')

print('\nRequirement 5\n')
print(f'Writing files to directory:')
file_writer= open(Path(newDir) / 'file_one.txt', 'w')
file_writer.write('Line 1 from file_one wrong_text\n')
file_writer.write('Line 2 from file_one wrong_text\n')
file_writer.write('Line 3 from file_one wrong_text')
file_writer.close()

print('\nRequirement 6\n')
file_reader = open(Path(newDir) / 'file_one.txt')
for line in file_reader:
    print(line)
file_reader.close()

print('\nRequirement 7\n')
print('Editing text from orginal file and writing to new file.')
file_reader = open(Path(newDir) / 'file_one.txt')
file_writer= open(Path(newDir) / 'file_two.txt', 'w')
for line in file_reader:
    newLine= line.replace('file_one wrong_text',
                         'file_two correct_text')
    file_writer.write(newLine)

file_reader.close()
file_writer.close()

print('\nRequirement 8\n')
print('Please write out the following lines to the a text editor\n'
      'exactly and then copy them to the clipboard using Ctrl-c')
print('Line 1 from the clipboard\n'
      'Line 2 from the clipboard\n'
      'Line 3 from the clipboard\n')
print('Please write and copy the above text using Ctrl-c now.')
# method below forced program to wait for user to copy to clipboard
pyperclip.copy('')
pyperclip.waitForPaste()

print('\nRequirement 9\n')
print('Contents from clipboard:\n')
print(pyperclip.paste())

print('\nRequirement 10\n')
file_reader = open(Path(newDir) / 'file_two.txt')
print('file_two.txt contents:\n')
for line in file_reader:
    print(line)
print('\nclipboard contents:\n')
print(pyperclip.paste())

print('\nRequirement 11\n')
print('Appending content from file two with clipboard content \n'
      'and writing it to thrid file.')
# save clipboard text as string
clip = pyperclip.paste()
# add newLine character to end of string for processing
clip += '\n'
file_reader = open(Path(newDir) / 'file_two.txt')
file_writer= open(Path(newDir) / 'file_three.txt', 'w')
# index used to find newline character in clipText
startIndex = 0
for line in file_reader:
    # next index of newline character found
    newLineIndex = clip.find('\n', startIndex)
    # combination of file_two line with cliptext line
    comboLine = (f'{line.strip()} followed by {clip[startIndex: newLineIndex]}')
    # update startIndex past newLine character
    startIndex = newLineIndex + 1
    print('\nRequirement 12\n')
    print('writing combo line to file_three.txt...')
    file_writer.write(comboLine)
file_writer.close()
file_reader.close()

print('\nRequirement 13\n')
print('file_three.txt contents:\n')
file_reader = open(Path(newDir) / 'file_three.txt')
for line in file_reader:
    print(line)
file_reader.close()

print('\nRequirement 14\n')
print('Please provide another directory name to be created')
print('NOTE: Please do not use special characters in this name.')
dirName2 = pyip.inputStr(blockRegexes=[r'[^a-zA-Z0-9]'],
                         prompt='Enter the directory name to be created: ')

newDir2 = Path.cwd() / Path(dirName2)
shutil.copytree(newDir, newDir2)
print(f'{dirName2} created and contains copies '
      f'of all files from {dirName}!')

# list of file names in directory created
dir_list = os.listdir(newDir2)
# removes file ext from file name, creates zip file, and removes og file
for file in dir_list:
    new_name = file.split('.')[0]
    new_name += '.zip'
    zipItem = zipfile.ZipFile( newDir2 / new_name, 'w')
    zipItem.write( newDir2 / file, compress_type=zipfile.ZIP_DEFLATED)
    zipItem.close()
    send2trash.send2trash(newDir2 / file)

print(f'All files in {dirName2} compressed successfully and '
      f'orginal files deleted!')

print('\nRequirement 15\n')
print('''This have been my favorite assignment so far. I have not 
had a chance to dive into much file manipulation during my time here at
ACC and am happy to have gotten a chance to cover it here. I am looking
forward to the next assignment!''')









