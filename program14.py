# Program14
# Austin Riggs
# 12/04/23

import bs4
import requests
import validators
import os.path

print('\nRequirement 1\n')
print('This is Program14 - Austin Riggs')

print('\nRequirement 2\n')
print('''This program demonstrates using Python to perform web scraping to 
create a text file. This program also demonstrates how to create a dictionary 
from a text file so that information about the file can be 
reviewed quickly.\n\n''')

class WebScraper:
      def __init__(self):
            self.url = ""

      def setURL(self, url):
          self.url = url

      def scrapData(self):
        res = requests.get(self.url)
        htmlSoup = bs4.BeautifulSoup(res.text, 'html.parser')
        pElements = htmlSoup.select('p')
        file = open("output.txt", "w", encoding = 'utf-8')
        for element in pElements:
          print(element.getText())
          file.write(element.getText())
        file.close()
        print('\n\nText from the file has successfully be saved to output.txt\n')


class TextFileToDictionary:
    def __init__(self):
        self.dic = {}
        self.totalWordCount = 0
        self.uniqueWordCount = 0
        self.mostFrequentCount = 0
        self.mostFrequentWord = ''


    def createDictionary(self, fileName):
        if os.path.isfile(fileName):
          file = open(fileName, 'r')
          for line in file:
              textArr = line.split(' ')
              for word in textArr:
                if word in self.dic:
                  self.dic[word] += 1
                  if self.dic[word] > self.mostFrequentCount:
                      self.mostFrequentCount = self.dic[word]
                      self.mostFrequentWord = word
                else:
                  self.dic[word] = 1
                  self.uniqueWordCount += 1

                self.totalWordCount += 1
        else:
            print(f'ERROR: {fileName} not found.')

    def getTotalWordCount(self):
        return self.totalWordCount

    def getUniqueCount(self):
        return self.uniqueWordCount

    def getFrequentCount(self):
        return self.mostFrequentCount

    def getMostFrequentWord(self):
        return self.mostFrequentWord

    def searchDictionary(self, searchWord):
        if searchWord in self.dic:
            return self.dic[searchWord]
        else:
            return 0



myScraper = WebScraper()

invalid = True
url = ''
while(invalid):
  userInput = input('Please enter a URL of a web page: ')
  if validators.url(userInput):
    url = userInput
    invalid = False
  else:
    print("ERROR: That is not a valid URL.\n")

myScraper.setURL(url)
myScraper.scrapData()

textDic = TextFileToDictionary()
textDic.createDictionary('output.txt')
totalWords = textDic.getTotalWordCount()
uniqueWords = textDic.getUniqueCount()
frequentWord = textDic.getMostFrequentWord()
frequentCount = textDic.getFrequentCount()
occurrences = textDic.searchDictionary('and')

print(f'Total number of words in text file: {totalWords}')
print(f'Total number of unique words in text file: {uniqueWords}')
print(f'Word with most occurances in text file: {frequentWord}')
print(f"Number of occurances of word '{frequentWord}': {frequentCount}")
print(f"Number of occurrences of word 'and': {occurrences}")


print('\nRequirement 3\n')
print('''I would give myself an A for this assignment as I have successfully 
utilized many of the concepts that we have covered in this course to make what I 
believe could be a useful tool.''')

print('\nRequirement 4\n')
print('''I enjoyed this assignment as it got me to think outside the box to 
create something without any direction. Over the break, I am planning on 
creating other projects that I can present to companies that will showcase my 
skillsets. I think I will include this project. I enjoyed this course and 
learned a lot from taking it. Happy holidays.''')