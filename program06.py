# Program06
# Austin Riggs
# 9/26/23

print('\nRequirement 1\n')

print('This is Program06 - Austin Riggs')

print('\nRequirement 2\n')

print('This program uses lists, strings, tuples, and dictionaries.')

print('\nRequirement 3\n')

print('Creating sets and lists...')

weeks = ('Week One', 'Week Two')
days = ('Thusday', 'Friday', 'Saturday')

sales_rep_names = ['Steve Kinney', 'Scott Rogers', 'Sam Smith']
sales_rep_locations = ['Flagstaff', 'Prescott', 'Sedona']

boats_sold_thursday = []
boats_sold_friday = []
boats_sold_saturday = []

print('\nRequirement 4\n')

print('########## Enter Sales Results ##########')
for week in weeks:
    print('\n***** Entering boats sold for {} ******'.format(week))
    for name in sales_rep_names:
        boats_sold_thursday.append(int(input(
            '\nThursday boats sold by {}: '.format(name))))
        boats_sold_friday.append(int(input(
            '\nFriday boats sold by {}: '.format(name))))
        boats_sold_saturday.append(int(input(
            '\nSaturday boats sold by {}: '.format(name))))


print('\nRequirement 5\n')

j = 0;

print('########## Print Sales Results ##########')
for week in weeks:
    print('\n***** {} Results ******'.format(week))
    for name in sales_rep_names:
        print('\n{} sold {} on Thursday.'.format(name,
                                                 boats_sold_thursday[j]))
        print('\n{} sold {} on Friday.'.format(name,
                                               boats_sold_friday[j]))
        print('\n{} sold {} on Saturday.'.format(name,
                                                 boats_sold_saturday[j]))
        j += 1

print('\nRequirement 6\n')

dealer_URLs = {}

print('########## Enter Dealship URLs ##########')
for loc in sales_rep_locations:
    URL = input ('\nEnter the URL for {}: '.format(loc))
    dealer_URLs[loc] = URL


print('\nRequirement 7\n')

i = 0

print('---- Contact sales reps at their email addresses: ------')
for name in sales_rep_names:
    sales_rep = name.lower()
    sales_rep = sales_rep.replace(' ', '_')
    print('\n {}@{}'.format(sales_rep,
                             dealer_URLs[sales_rep_locations[i]]))
    i += 1

print('\nRequirement 8\n')

print('''I enjoyed this lab as it was a good refresher on sets, lists and 
dictionaries in python. I honestly have not really used sets much in any 
programing language so far and I found it interesting that they could
be iterated through in a for loop in the same manner as a list.''')













































































































































