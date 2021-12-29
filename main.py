# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


cars = ["ok", "ok" , "ok", "faulty", "ok", "ok"]

# break and continue
print("for loops with break:")
for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This cars is {status}")

#########################################
print("for loops with continue --skip:")
for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        continue
    print(f"This cars is {status}")
###########################################
    # for loop with else
#########################################
cars = ["ok", "ok" , "ok", "ok", "ok"]
for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        print(f"This cars is {status}")
    else:
        print("All cars built successfully. No faulty cars!")



#################################

    for i in range(20):
      print(i)

###################

    kid_ages = (3, 7, 12)
    for age in kid_ages:
      print(f'I have a {age} year old kid.')

#prime numbers
##################
for number in range(2, 10):
    for x in range(2, number):
        if number % x == 0:
            print(f"{number} equals {x} * {number//x}")
            break
        else:
            print(f"{number} is a prime number.")

###########
#Slising
friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
# start from position 2 to 4. exclude 4
print(friends[2:4])
# from position 1 to till the end
print(friends[1:])
# from the end to beginning excluding the position 4
print(friends[:4])



s = slice(1, 4)
print(s)
t = (1, 2, 3, 4, 5)  # tuple
l = [1, 2, 3, 4, 5]  # list
c = "12345"          # string

print(t[s])  # (2, 3, 4)
print(l[s])  # [2, 3, 4]
print(c[s])  # 234



def palindrome_check(word):
	if word == word[::-1]:  # check against full sequence in reverse order
		return True
	return False

print(palindrome_check("kayak"))  # True
print(palindrome_check("lemon"))  # False


# list comprehension
numbers = [0, 1, 2, 3, 4, 5, 6]
doubled_numbers = []
for number in numbers:
    doubled_numbers.append(number * 2)
print(doubled_numbers)
 # one liner
doubled_numbers = [number * 2 for number in numbers]
doubled_numbers = [number * 2 for number in range(5)]


friend_ages = [22, 31, 35, 37]
age_strings = [f" My friend is {age} years old." for age in friend_ages]

print(age_strings)

names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)


ages = [22, 35, 27,  21, 20]
odds = [age for age in ages if age % 2 == 1]
print(odds)

# dictionary comprehensions
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]
long_timers = {
    friends[i]:time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}
print(long_timers)
 # zip function to create dictionertis
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]
print("example of dict(zip())")
long_timers = dict(zip(friends, time_since_seen))
print(long_timers)

 #enumerate
print("###ENUMERATE##")
friends = ["Rolf", "Bob", "Jen", "Anne"]
counter = 0
for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1
print("shorter version")
for counter, friend in enumerate(friends, start=1):
    print(counter)
    print(friend)

print(list(enumerate(friends)))
print(list(zip([0, 1, 2, 3], friends)))

print("test")
guests = [('rolf', 25), ('adam', 28), ('jen', 24)]

import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 22, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

top_player = players[0]  # start by saying "the top matching player is the first one"

for player in players:  # Go over each player
    matched_numbers = len(player["numbers"].intersection(lottery_numbers))  # Calculate how many numbers they matched
    if matched_numbers > len(
            top_player["numbers"].intersection(lottery_numbers)):  # If they matched more than the current top player...
        top_player = player  # Say this player is the new top player

# Calculate their winnings using the formula!
winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers))

print(f"{top_player['name']} won {winnings}.")