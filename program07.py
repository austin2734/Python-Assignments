# Program07
# Austin Riggs
# 10/6/23

def main():

    rep_names = ['Steve Kinney', 'Scott Rogers', 'Sam Smith']
    rep_locations = ['Flagstaff', 'Prescott', 'Sedona']

    sold_thursday = []
    sold_friday = []
    sold_saturday = []

    dealer_URLs = {}

    requirement_1()
    requirement_2()
    weeks, days = requirement_3()
    requirement_4(weeks, days, rep_names, rep_locations, sold_thursday,
                  sold_friday, sold_saturday)
    requirement_5(weeks, rep_names, rep_locations, sold_thursday,
                  sold_friday, sold_saturday)
    requirement_6(dealer_URLs, rep_locations)
    requirement_7(rep_names, rep_locations, dealer_URLs)
    requirement_8()

def requirement_1():
    print('\nRequirement 1\n')
    print('This is Program07 - Austin Riggs')

def requirement_2():
    print('\nRequirement 2\n')
    print('This program provides practice working with lists, strings,'
          'tuples, and dictionaries.')

def requirement_3():
    print('\nRequirement 3\n')
    print('Creating sets and lists...')

    weeks = ('Week One', 'Week Two')
    days = ('Thusday', 'Friday', 'Saturday')
    return weeks, days

def requirement_4(weeks, days, rep_names, rep_locations, sold_thursday,
                  sold_friday, sold_saturday):
    print('\nRequirement 4\n')

    print('########## Enter Sales Results ##########')
    for week in weeks:
        print('\n***** Entering boats sold for {} ******'.format(week))
        for name in rep_names:
            sold_thursday.append(int(input(
                '\nThursday boats sold by {}: '.format(name))))
            sold_friday.append(int(input(
                '\nFriday boats sold by {}: '.format(name))))
            sold_saturday.append(int(input(
                '\nSaturday boats sold by {}: '.format(name))))


def requirement_5(weeks, rep_names, rep_locations, sold_thursday,
                  sold_friday, sold_saturday):
    print('\nRequirement 5\n')

    j = 0;

    print('########## Print Sales Results ##########')
    for week in weeks:
        print('\n***** {} Results ******'.format(week))
        for name in rep_names:
            print('\n{} sold {} on Thursday.'.format(name,
                                                 sold_thursday[j]))
            print('\n{} sold {} on Friday.'.format(name,
                                               sold_friday[j]))
            print('\n{} sold {} on Saturday.'.format(name,
                                                 sold_saturday[j]))
            j += 1

def requirement_6(dealer_URLs, rep_locations):
    print('\nRequirement 6\n')

    print('########## Enter Dealship URLs ##########')
    for loc in rep_locations:
        URL = input ('\nEnter the URL for {}: '.format(loc))
        dealer_URLs[loc] = URL

def requirement_7(rep_names, rep_locations, dealer_URLs):
    print('\nRequirement 7\n')

    i = 0

    print('---- Contact sales reps at their email addresses: ------')
    for name in rep_names:
        sales_rep = name.lower()
        sales_rep = sales_rep.replace(' ', '_')
        print('\n {}@{}'.format(sales_rep,
                                 dealer_URLs[rep_locations[i]]))
        i += 1

def requirement_8():
    print('\nRequirement 8\n')

    print('This lab was a good refresher on python functions and functional\n' +
         'scopes. The biggest challenge of this assignment was trying to\n' +
         'figure out where to create and store the lists needed in various\n' +
         'functions in this program. I look forward to the next assignment.')



if __name__ == '__main__':
    main()

else:
    pass









































































































































