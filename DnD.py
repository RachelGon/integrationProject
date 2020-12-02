from random import randint

print("Welcome to Rachel Gonzalez's integration project!")
print("This is a simple text and turn base fight game")
print("Your only options are to fight, run or use an item, there's no distinction between winning from running or "
      "defeating your opponent yet")


# figured out classes with https://www.w3schools.com/python/python_classes.asp
class Player:
    def __init__(self, name, armor_class, hit_points, strength_roll, hit_roll, items_list):
        self.name = name
        self.armor_class = armor_class
        self.hit_points = hit_points
        self.strength_roll = strength_roll
        self.hit_roll = hit_roll
        self.items_list = items_list


class Mob:
    def __init__(self, name, armor_class, hit_points, strength_roll, hit_roll):
        self.name = name
        self.armor_class = armor_class
        self.hit_points = hit_points
        self.strength_roll = strength_roll
        self.hit_roll = hit_roll


def roll(mob, user):
    mob.strength_roll = randint(1, 20)
    mob.hit_roll = randint(1, 10)

    user.strength_roll = randint(1, 20)
    user.hit_roll = randint(1, 10)


def items(mob, user):
    i = 1
    for x in user.items_list:
        print(str(i) + ". " + str(x))
        i += 1
    item_number = input("Enter the item number to : ")
    if item_number == "1":
        for x in player.items_list[0]:
            if x.isdigit():
                if int(x) <= 0:
                    del player.items_list[0]
                player.items_list[0] = "PokeBall(" + (str(int(x) - 1)) + "x)"
                print("You used a PokeBall!")
                pokeball(mob)

                break
    elif item_number == "2":
        player.hit_points += 20
        if player.hit_points > 50:
            player.hit_points = 50
        print("\nPlayer health bar:" + "■" * user.hit_points)
        print("You are now at " + str(player.hit_points) + " HP")
    else:
        print("Try a again, that wasn't a valid input")


def pokeball(mob):
    if mob.hit_points < 18:
        print("Caught " + mob.name + "!")
        mob.hit_points = 0


def combat(mob, user):
    count = 0
    while mob.hit_points > 0:
        roll(mob, user)
        encounter_response = input("\nEnter 'fight', 'run' or 'items': ")

        if encounter_response == "fight":
            count += 1
            # The player swings first
            if user.strength_roll >= mob.armor_class:
                print("\nYou launch your self forward in a fearsome attack")
                print(mob.name + " took " + str(user.hit_roll) + " points of damage!")  # tells damage the user took
                mob.hit_points -= user.hit_roll  # removes health from the user depending on the roll of the Mob
                print("\nOpponent health bar:" + "■" * mob.hit_points)
                if mob.hit_points <= 0:
                    break
            else:
                print("\nYour attack missed!")
            # The mob swings second
            if mob.armor_class >= user.strength_roll:
                print("\nYour opponent lands a hit on you!")
                print(user.name + " took " + str(mob.hit_roll) + " points of damage ")
                user.hit_points -= mob.hit_roll
                print("\nPlayer health bar:" + "■" * user.hit_points)
                if user.hit_points <= 0:
                    break
            else:
                print("\nYour opponents attack missed!")
        elif encounter_response == "run":
            roll(mob, user)
            if user.strength_roll >= 12:
                print("You successfully evaded the attack")
                break
            else:
                roll(mob, user)
                mob.hit_roll /= 10  # converts into a decimal
                user.hit_points = int(mob.hit_roll * user.hit_points)  # run takes a percent of the health off
                print("\nPlayer health bar:" + "■" * user.hit_points)
                print("Your health went down to " + str(user.hit_points) + "! ")
        elif encounter_response == "items":
            items(mob, user)


def input_guess():
    while True:
        try:
            guess = int(input("Guess the Number: "))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return guess


def bonus():
    print("\nBut first! Guess the random number for a some serotonin and nothing ")
    random = (randint(1, 100))
    if random % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

    guess = input_guess()

    if guess != random:
        print("You didn't guess it!")
    else:
        print("You got it")


player = Player("Charmander", 18, 39, (randint(1, 20) + 1), (randint(1, 10)), ["PokeBall(3x)", "Healing Potion"])
boar = Mob("Bulbasaur", 12, 41, (randint(1, 20) + 1), randint(1, 10))
bonus()
combat(boar, player)

if player.hit_points <= 0:
    print("You Lost!\n")
else:
    print("You Won!\n")

# yet to implement naturally
exponentiation = 2 ** 2  # raises a number to the power of another
floor = 77 // 17  # divides a number wile rounding down to a whole number

print("Exponentiation: " + str(exponentiation))
print("Floor: " + str(floor))
