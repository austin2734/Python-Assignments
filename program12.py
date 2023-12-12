# Program11
# Austin Riggs
# 11/08/23

import webbrowser
import pyperclip
import requests
import bs4
import openpyxl

print('\nRequirement 1\n')
print('This is Program12 - Austin Riggs')

print('\nRequirement 2\n')
print('This program demonstrates using Python '
      'to perform web scraping and working with Excel spreadsheets')

print('\nRequirement 3\n')
print('Please copy a U.S street address to the clipboard.')
pyperclip.copy('')
address = pyperclip.waitForPaste()
webbrowser.open('https://www.google.com/maps/place/' + address)

print('\nRequirement 4\n')
URL = input('Please enter a URL of a web page: ')
res = requests.get(URL)
htmlSoup = bs4.BeautifulSoup(res.text, 'html.parser')
pElements = htmlSoup.select('p')

for element in pElements:
      print(element)

print('\nRequirement 5\n')

class ExcelProcessing:
    def __init__(self, excelFile):
        self.excelFile = openpyxl.load_workbook(excelFile)

    def displaySheets(self):
        print('Sheets in excel file:\n')
        for sheet in self.excelFile.sheetnames:
            print(sheet)
        print()


    def displaySection(self):
        sheet = self.excelFile['Sheet1']
        print("Enter a rectangular section from the excel file to diplay\n"
              "the cells and their values in the section. (e.g. A1:D6)")
        section = input("Enter a section from the excel file: ")
        print()
        for rows in sheet[section]:
            for cell in rows:
                print(f"{cell.coordinate} {cell.value}")
            print("*************************************")

    def displayCellValue(self):
        sheet = self.excelFile['Sheet1']
        cellNum = input("Enter a cell number to display it's value: ")
        print("\nCell value: ", sheet[cellNum].value, end='\n\n')


print('\nRequirement 5\n')
print('Creating class object....')
excelObj = ExcelProcessing('example.xlsx')

print('\nRequirement 6\n')
excelObj.displaySheets()
print('\nRequirement 7\n')
excelObj.displayCellValue()
print('\nRequirement 8\n')
excelObj.displaySection()

print('\nRequirement 9\n')
print('''I really enjoyed this assignment as it covered really interesting
programmable features I have yet to utilize in any other programming language.
I really like the excel file features covered in this assignment and believe 
that they will come in handy in other personal projects in the future.''')





