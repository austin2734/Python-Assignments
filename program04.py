
# Program04
# Austin Riggs
# 9/10/23


print("\nRequirement 1\n")
print("This is Program04 - Austin Riggs")

print("\nRequirement 2\n")
print("This program provides concert seat assignments")

print("\nRequirement 3\n")
preference = input("What is your musical preference? ")

if (preference.lower() == "classical"):

    print("\nRequirement 4\n")

    fName = input("What is your first name? ")
    lName = input("What is your last name? ")


    needLevelInfo  = True
    level = ""
    needSeatInfo = True
    seat = ""
    needMealInfo = True
    meal = ""

    while (needLevelInfo):
        print("What is your membership level?\n")
        level = input("Enter the word composer, conductor, or musician: ")
        level = level.lower()

        if (level== "composer" or level == "conductor" or level == "musician"):
            needLevelInfo = False
        else:
            print("Error: Please enter one of the vaild membership options.\n")

    while (needSeatInfo):
        print("What is your seat preference?\n")
        seat = input("Enter the word orchestra, main, or balcony: ")
        seat = seat.lower()

        if (seat == "orchestra" or seat == "main" or seat == "balcony"):
            needSeatInfo = False
        else:
            print("Error: Please enter one of the vaild seat "
                  "preference options\n")

    while (needMealInfo):
        print("What is your meal preference?\n")
        meal = input("Enter the word chicken, fish, or vegan: ")
        meal = meal.lower()

        if (meal == "chicken" or meal == "fish" or meal == "vegan"):
            needMealInfo = False
        else:
            print("Error: Please enter one of the vaild meal "
                  "preference options\n")


    print("\nRequirement 5\n")
    print("\nThank you {} {}. ".format(fName, lName), end="")

    if (level == "composer"):

        if (seat == "orchestra"):
            print("You qualify for these exceptional seats!\n")
        elif (seat == "main"):
            print("Main is ok, let us know if you want closer seats.\n")
        else:
            print("Interesting, let us know if you want closer seats.\n")

    elif (level == "conductor"):
        if (seat == "orchestra"):
            print("Unfortunately, composer level membership is required "
                  "to sit in the orchestra section.\n")
        elif(seat == "main"):
            print("The seats in the main section are very good.\n")
        else:
            print("Interesting, let us know if you want closer seats.")

    else:
            if(seat == "orchestra"):
                print("Unfortunately, composer level membership "
                      "is required to sit in the orchestra section.\n")
            elif(seat == "main"):
                print("Member level of Composer or Conductor required if "
                      "you want to sit in the main section.\n")
            else:
                print("Your balcony seats are confirmed.\n")


    print("\nRequirement 6\n")

    totalScore = 0

    print("Please complete our survey and provide scores between 1 - 5 "
          "(1 = strongly disagree; 5 = strongly agree) in response to "
          "these three statements: ")

    needScores = True
    concertScore = 0
    foodScore = 0
    seatScore = 0

    while (needScores):

        concertScore = int (input("The concert was wonderful: "))
        foodScore = int (input("The food was fantasic: "))
        seatScore = int (input("The seats were superb: "))

        if (concertScore in range(1, 6) and foodScore in range(1, 6) and
            seatScore in range(1, 6)):

            needScores = False

        else:
            print("Error: Please enter numbers between 1 to 5\n")

    print("\nRequirement 7\n")
    totalScore = concertScore + foodScore + seatScore

    if (level == "composer"):
        if (totalScore < 12 or concertScore < 4 or foodScore < 4  or
            seatScore < 4):
            print("Dear Composer, Your survey score of {} was lower "
                  "than we would like. Please give us another opportunity "
                  "soon.".format(totalScore))
        else:
            print("Thank you for being a Composer member and for "
                  "having a good time!")

    elif (level == "conductor"):
        if (totalScore < 11 or concertScore < 3 or foodScore < 3 or
                seatScore < 3):
            print("Dear Conductor, Your survey score of {} was lower than "
                  "we would like. The next time you attend we will be "
                  "nicer.".format(totalScore))
        else:
            print("Thank you for being a Conductor member and for having "
                  "a good time!")

    else:
        if (totalScore < 10 or concertScore < 2 or foodScore < 2 or
                seatScore < 2):
            print("Dear Musician, Your survey score of {} was lower than "
                  "we would like. You will have more fun next "
                  "time.".format(totalScore))
        else:
            print("Thank you for being a Musician member and for having a "
                  "good time!")




else:

    print("\nSorry we do not recognize the {} genre.".format(preference))


print("\nRequirement 8\n")
print('''I enjoyed this program as it really had me think about the best way
to structure section statements efficiently. While you did not say anything 
about vadidating user inputs, I took it upon myself to validate them. I hope
that doing so is ok.''')