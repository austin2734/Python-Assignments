# Program03
# Austin Riggs
# ITSE-1359
# 8/28/23

print("\nRequirement 1\n")

print("This is Program03 - Austin Riggs")

print("\nRequirement 2 \n")

print("This program records goals for soccer players and points for "
      "basketball players.")

print("\nRequirement 3 \n")

print("Enter three names of soccer players.\n")

player1 = input("Enter the first soccer players name: ")
player2 = input("Enter the second soccer players name: ")
player3 = input("Enter the third soccer players name: ")

print("\nRequirement 4 \n")

print("Enter the career goals for each of the soccer players.\n")

goals1 = input("Enter the number of {}'s career goals: ".format(player1))
goals2 = input("Enter the number of {}'s career goals: ".format(player2))
goals3 = input("Enter the number of {}'s career goals: ".format(player3))


print("\nRequirement 5 \n")

print("Sorting data...")

if (int(goals1) > int(goals2) and int(goals1) > int(goals3)):

      highest = player1 + "-" + goals1

      if (int(goals2) > int(goals3)):
            middle = player2 + "-" +goals2
            lowest = player3 + "-" + goals3
      else:
            middle = player3 + "-" + goals3
            lowest = player2 + "-" +goals2

elif (int(goals2) > int(goals1) and int(goals2) > int(goals3)):

      highest = player2 + "-" + goals2

      if (int(goals1) > int(goals3)):
            middle = player1 + "-" + goals1
            lowest = player3 + "-" + goals3
      else:
            middle = player3 + "-" + goals3
            lowest = player1 + "-" + goals1

else:
      highest = player3 + "-" + goals3

      if (int(goals1) > int(goals2)):
            middle = player1 + "-" + goals1
            lowest = player2 + "-" + goals2
      else:
            middle = player2 + "-" + goals2
            lowest = player1 + "-" + goals1


print("\nRequirement 6 \n")

print("Soccer players names and career goals sorted from highest to "
      "lowest goals scored.\n")

print(highest)
print(middle)
print(lowest)


print("\nRequirement 7 \n")

print("Enter the names of three basketball players.\n")

bPlayer1 = input("Enter the name of the first basketball player: ")
bPlayer2 = input("Enter the name of the second basketball player: ")
bPlayer3 = input("Enter the name of the third basketball player: ")


print("\nRequirement 8 \n")

print("Enter the career points for each of the basketball players.\n")

points1 = input("Enter the number of {}'s career points: ".format(bPlayer1))
points2 = input("Enter the number of {}'s career points: ".format(bPlayer2))
points3 = input("Enter the number of {}'s career points: ".format(bPlayer3))


print("\nRequirement 9 \n")

print("Sorting data....")

if (int(points1) > int(points2) and int(points1) > int(points3)):

      first = bPlayer1 + "-" + points1

      if (int(points2) > int(points3)):
            second = bPlayer2 + "_" + points2
            third = bPlayer3 + "-" + points3
      else:
            second = bPlayer3 + "-" + points3
            third = bPlayer2 + "-" + points2

elif (int(points2) > int(points1) and int(points2) > int(points3)):

      first = bPlayer2 + "-" + points2

      if (int(points1) > int(points3)):
            second = bPlayer1 + "-" + points1
            third = bPlayer3 + "-" + points3
      else:
            second = bPlayer3 + "-" + points3
            third = bPlayer1 + "-" + points1
else:
      first = bPlayer3 + "-" + points3

      if (int(points1) > int(points2)):
            second = bPlayer1 + "-" + points1
            third = bPlayer2 + "-" + points2
      else:
            second = bPlayer2 + "-" + points2
            third = bPlayer1 + "-" + points1

print("\nRequirement 10\n")

print("Basketball players names and career points sorted from highest to "
      "lowest points scored.\n")

print(first)
print(second)
print(third)


print("\nRequirement 10\n")

print('''While this lab was not very difficult in concept, it did take me a
bit longer than I thought it would due to a bug that I found in my program.
When testing, I was getting very strange results but after using the debugger
I noticed that my goal and point counts were being saved as type str I fixed
this by casting all of these str to int throughout my selection statements.''')






