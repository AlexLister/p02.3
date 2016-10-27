"""
Problem:

    Professor Oak is interested in developing a simulator for pokemon battles,
    to try and see who will win. The function 'battle' is his first attempt.

    'battle' takes 4 arguments, the names of both pokemons and their power
    level. It should print out the name of the winner, unless it is a draw
    in which case it should print "Draw"

    Professor Oak's first attempts at creating some rules for his simulator
    are very simple: the pokemon with the highest power wins UNLESS one of
    the pokemon is Mewtwo. Mewtwo is so awesome, his actual power level
    should be considered 100 more than it actually is.

Tests:

    >>> battle("Pikachu", 80, "Bulbasaur", 110)
    Bulbasaur
    >>> battle("Squirtle", 150, "Weedle", 90)
    Squirtle
    >>> battle("Pidgey", 200, "Rattata", 200)
    Draw
    >>> battle("Mewtwo", 90, "Vileplume", 150)
    Mewtwo
    >>> battle("Golduck", 170, "Mewtwo", 50)
    Golduck
    >>> battle("Abra", 120, "Mewtwo", 20)
    Draw
    >>> battle("Mewtwo", 60, "Mewtwo", 60)
    Draw

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def battle(name1, power1, name2, power2):
    
    if name1 == "Mewtwo":
        power1 = power1 + 100

    if name2 == "Mewtwo":
        power2 = power2 + 100

    if power1 == power2:
        print ("Draw")

    elif power1 > power2:
        print (name1)

    else:
        print (name2)

#I wanna be the very best
#Like no one ever was
#To catch them is my real test
#To train them is my cause

#I will travel across the land
#Searching far and wide
#Each Pokemon to understand
#The power that's inside

#Pokemon, gotta catch 'em all
#Its you and me
#I know it's my destiny
#Pokemon, oh, you're my best friend
#In a world we must defend
#Pokemon, gotta catch 'em all
#A heart so true
#Our courage will pull us through

#You teach me and I'll teach you
#Pokemon, gotta catch 'em all
#Gotta catch 'em all
#Yeah

#Every challenge along the way
#With courage I will face
#I will battle every day
#To claim my rightful place

#Come with me, the time is right
#There's no better team
#Arm in arm we'll win the fight
#It's always been our dream

#Pokemon, gotta catch 'em all
#Its you and me
#I know it's my destiny
#Pokemon, oh, you're my best friend
#In a world we must defend
#Pokemon, gotta catch 'em all
#A heart so true
#Our courage will pull us through

#You teach me and I'll teach you
#Pokemon, gotta catch 'em all
#Gotta catch 'em all
#Gotta catch 'em all
#Gotta catch 'em all
#Yeah

 













    

