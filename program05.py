# Program05
# Austin Riggs
# 9/18/23

print('\nRequirement 1\n')
print('This is Program05 - Austin Riggs')

print('\nRequirement 2\n')
print('This program records Book People product data.')

print("\nRequirement 3\n")
numOfAuthors = int(input('Please enter number of authors you wish to '
                         'process: '))

print("\nRequirement 4\n")
for authors in range(numOfAuthors):
    name = input("Please enter the author's full name: ")
    url = input("Please enter the author's website URL: ")


    userInput = ''
    book_name_list = []
    book_isbn_list = []
    book_order_quantity_list = []

    print("\nRequirement 5\n")

    while userInput != '-1':

        print("Would you like to add a book to the list?")
        userInput = input ("Enter any key to add a book or -1 to quit: ")

        if (userInput != '-1'):

            book_name_list.append(input('Enter the name of the book: '))
            book_isbn_list.append(input('Enter the ISBN of the book: '))
            book_order_quantity_list.append(input('Enter the quantity to '
                                                  'order: '))
            print('\n')

    print("\nRequirement 6\n")
    print('\n' + name)
    print(url, end='\n\n')

    print("\nRequirement 7\n")
    for i in range (len(book_name_list)):

        print('Book Title {}: '.format(i + 1) + book_name_list[i])
        print('Book ISBN {}: '.format(i + 1) + book_isbn_list[i])
        print('Amount to order {}: '.format(i + 1) + book_order_quantity_list[i]
              , end='\n\n')


print("\nRequirement 8\n")
print('''I enjoyed this lab as it was a good refresher on python lists. I
haven't used them since programming 1. I did spend a little time trying to
remember how to iterate through them as I am so use to for loops with java.''')

