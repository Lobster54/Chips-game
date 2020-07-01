"""
--------------------------------------------------------------------------------
    Project: Chips Game
    Standard: 91883 (AS1.7) v.1
    Date: 26.03.20
    Python: 3.8
------------------------------------------------------~-------------------------

--------------------------------------------------------------------------------
    This program runs a game, the game is called 'Chips Game', and is like poker, but not quite.
    the aim of the game is to go from 21 chips at the start of the round, to 0, the winner is
    the one that has their turn last (when the chips = 0 ), they win. You have the ability to play
    singleplayer or multiplayer, both you can play by yourself, but that's weird playing the
    multiplayer one by yourself.

    the code below, is structured in functions, that are looped, and are called from other functions,
    the only function that is called to start the chain is the menu() function, this is the only one
    that is needed to be called. there are many comments that are there for to tell you what it is
    that they do, such as; chips_taken the comment is highlighted by the '#' and then the comment to
    the right of that.

    I hope that you enjoy this game, and play it thoroughly, have a nice day.

            - Lobster
--------------------------------------------------------------------------------
"""
#~~=~~# IMPORTS #~~=~~#
import random
import time

#~~=~~# INITIALISATIONS OF THE INPUTS, CONSTANT, AND VARIABLES #~~=~~#
        #=# INPUTS #=#

    # Names of the players, entered into through an input, currenty '...' as it is a string.
player1 = 'Phred'
player2 = 'Arnold Ingledon'

    # Number of rounds, will also be an input for the players to decide how much gruelling pain they are going to put themselves through, typically 1~5
rounds = 0

    # The number of chips_taken by a player on their round.
chips_taken = 0


        #=# CONSTANTS #=#

    # the Number of chips that are in the 'pool' at the start of each rounds.
CHIPPOOL = 21


        #=# VARIABLES #=#

    # The number of rounds succesfully
rounds_played = 1

    # The player who's turn it happens to be at that turn.
player = player1  #Will flip between player1 and player2

    # the total number of chips left after each players turn.
chips_left = CHIPPOOL

    # the score of the person who is playing as the player of 1.
player_score1 = 0

    # The score of the person who is playing as the player of 2, not 1.
player_score2 = 0

    # Random chance for the introduction of the game
narrator_voice_chance = random.randint(1, 100)

    # The voice for the narrator/AI. shhhh don't tell it...
voice = 0

    # The Game type that is being played, will either be singleplayer or multiplayer when the game is running
game_setting = 0


        #=# LOCALISED TEXT #=#

    # Horizontal Line of "-" repeated over and over again
HL = "------------------------------------------------------~-------------------------\n"

    # Different Greetings based on what voice you get
intro1 = "\n    Welcome to the Game, player! \n We hope you have a lovely time here \n      playing the chips game! \n" # Perfectly fine Greeting
intro2 = "\n     Welcome to the Game, pl-y-er!\n W-we hope you have a l-ovely time here\n       playing the chi-ips game!\n" # Slightly glitchy Greeting
intro3 = "\n    We-elco-me to t-th e Ga-me, p-y er!\n W-we h-ope you h-h-ave a-a l-v-el-y-y h-e-er\n             pl-a-y-y-y-i .....\n" # Really glitchy Gretting
intro4 = "\n 01010111 01100101 01101100 01100011 01101111 01101101 01100101 00100000 01110100 01101111 00100000 01110100 01101000 01100101 00100000 01000111 01100001 01101101 01100101 00101100 00100000 01110000 01101100 01100001 01111001 01100101 01110010 00100001 01010111 01100101 00100000 01101000 01101111 01110000 01100101 00100000 01111001 01101111 01110101 00100000 01101000 01100001 01110110 01100101 00100000 01100001 00100000 01101100 01101111 01110110 01100101 01101100 01111001 00100000 01110100 01101001 01101101 01100101 00100000 01101000 01100101 01110010 01100101 01110000 01101100 01100001 01111001 01101001 01101110 01100111 00100000 01110100 01101000 01100101 00100000 01100011 01101000 01101001 01110000 01110011 00100000 01100111 01100001 01101101 01100101 00100001 " # Absolutley binary Greeting


#~~=~~# GAME BODY #~~=~~#

#=# FUNCTIONS #=#

def menu():
    global game_setting
    game_type = str(input( "[S]ingle player, or [M]ultiplayer: "))              # Ask what game type the player(s) want to play
    if game_type == "S" or game_type == "s":
        game_setting += 1
        greeting()
    elif game_type == "M" or game_type == "m":
        game_setting += 2
        greeting()
    else:
        print("\n That's not right, try again\n")                                 # Get it right man
        menu()

def greeting():
    global voice
    if narrator_voice_chance <= 40:
        print(intro1)                                                           # Perfectly Fine Greeting
        voice = 1
        player_names()
    elif narrator_voice_chance <= 70:
        print(intro2)                                                           # Slightly Glitchy Greeting
        voice = 2
        player_names()
    elif narrator_voice_chance <= 90:
        print(intro3)                                                           # Really Glitchy Greeting
        voice = 3
        player_names()
    elif narrator_voice_chance <= 100:
        print(intro4)                                                           # It's Just binary
        voice = 4
        player_names()

def player_names():
    global game_setting
    global player1
    global player2
    if game_setting == 1:
        player1 = str(input("\n What is your name? "))                          # Asking for a name
        if player1.isalpha() == True:                                           # checking to see whether the name uses only letters from the english alphabet
            rounds_to_play()
        else:
            print(" please try again")                                          # Please try again
            player_names()
    elif game_setting == 2:
        player1 = str(input("\n What is your name player 1? "))
        player2 = str(input("\n What is your name player 2? "))
        if player1.isalpha() == True and player2.isalpha() == True:
            rounds_to_play()
        else:
            print(" please try again")
            player_names()

def rounds_to_play():                                                           # Ask How many Rounds the player(s)
    global rounds
    rounds = int(input("\n How many rounds would you like to play? chose between 1-6 rounds: "))
    if rounds > 6:                                                              # Check if it's more than 6 rounds
        print(" Try entering less rounds")
        rounds_to_play()
    elif rounds < 1:                                                            # Check if it's less than 1 round
        print(" Try entering more rounds")
        rounds_to_play()                                                        # Loops back to the start of the function
    else:
        print_out()                                                             # move on to the next function

def print_out():
    global chips_left
    chips_left = CHIPPOOL                                                       # Make sure the 'chips_left' is equal to 'CHIPPOOL'
    print(HL)                                                                   # Horizontal line
    print(" Player 1 ( {} ) score: {}".format(player1, player_score1))
    print(" Player 2 ( {} ) score: {} \n".format(player2, player_score2))
    global player
    player = player1                                                            # set the player to player 1
    print(HL)
    if game_setting == 1:
        player_turn_single()                                                    # Run the singleplayer function
    elif game_setting == 2:
        player_turn_multi()                                                     # Run the multiplayer function

def player_turn_single():
    global player
    global chips_taken
    global chips_left
    print("\n It is ", player, "'s turn")
    print(" You can choose between 1-3 chips to take,")
    if player == player2:                                                       # If it's the AI then it checks what voice to use
        print(" so how many will you take?")
        if voice == 1:
            voice_1()
        elif voice == 2:
            voice_2()
        elif voice == 3:
            voice_3()
        elif voice == 4:
            voice_4()
        if chips_left == 0:
            winner()                                                            # Run the Winner function
        else:
            player = player1                                                    # Switch to Player 1
            player_turn_single()                                                # Run Again
    elif player == player1:
        chips_taken = int(input(" so how many will you take? "))
        if chips_taken > 3 or chips_taken < 1:                                  # Check for the appropriate amount of chips to be taken
            print("\n Choose a number between 1-3 please")
            player_turn_single()
        else:
            print("\n Nice move taking ", chips_taken, " chips")
            chips_left -= chips_taken
            print(" There are now ", chips_left, " chips left")
            if chips_left <= 0:
                winner()                                                        # Run The Winner Function
            else:
                player = player2                                                # Change to Player 2
                player_turn_single()                                            # Run again

# Ai Voices for the ^ Function ( they all do the same thing)
def voice_1():                                                                  # Perfectly fine voice
    global chips_left
    global chips_taken
    chips_taken = random.randint(1, 3)
    print(" I'll take ", chips_taken, " chips")
    chips_left -= chips_taken
    print(" There are now {} chips left \n".format(chips_left))
def voice_2():                                                                  # Slightly Glitchy
    global chips_left
    global chips_taken
    chips_taken = random.randint(1, 3)
    print(" I-i'll t-ake ", chips_taken, " chips")
    chips_left -= chips_taken
    print(" There are now {} chips left \n".format(chips_left))
def voice_3():                                                                  # More glitchy
    global chips_left
    global chips_taken
    chips_taken = random.randint(1, 3)
    print(" I-I'll T-ak-e ", chips_taken, " ch-i-ps-s-s")
    chips_left -= chips_taken
    print(" There are now {} chips left \n".format(chips_left))
def voice_4():                                                                  # Binary
    global chips_left
    global chips_taken
    chips_taken = random.randint(1, 3)
    print(" 01001001 00100111 01101100 01101100 00100000 01110100 01100001 01101011 01100101 00100000 ", chips_taken, " 01100011 01101000 01101001 01110000 01110011 ")
    chips_left -= chips_taken
    print(" There are now {} chips left \n".format(chips_left))

def player_turn_multi():                                                        # The multiplayer function
    global player
    global chips_left
    global chips_taken
    print("\n It is ", player, "'s turn")
    print(" You can choose between 1-3 chips to take,")
    chips_taken = int(input(" so how many will you take? "))
    if chips_taken > 3 or chips_taken < 1:                                      # Check if they've taken the appropriate amount of chips
        print("\n Choose a number between 1-3 please")
        player_turn_multi()
    else:
        print("\n Nice move taking ", chips_taken, " chips")
        chips_left -= chips_taken                                               # Take the chips from the remaining chips
        print(" There are now ", chips_left, " chips left")
        if chips_left <= 0:
            winner()
        else:                                                                   # Switch the player
            if player == player1:                                               # To Player 2
                player = player2
            elif player == player2:                                             # To Player 1
                player = player1
            player_turn_multi()

def winner():                                                                   # Winner Winner Chicken Dinner
    global player
    global player_score1
    global player_score2
    global chips_left
    global rounds_played
    print("\n Congragulation! {} you have won this round!".format(player))      # Congrats Mate!
    if player == player1:                                                       # If it was player 1's turn
        player_score1 += 1
    elif player == player2:                                                     # If it was player 2's turn
        player_score2 += 1
    if rounds_played != rounds:                                                 # if rounds_played is not equal to rounds then keep going
        rounds_played += 1
        print_out()
    elif rounds_played == rounds:                                               # if it is, finish
        print_out_2()

def print_out_2():
    print(HL)
    print(" Player 1 ( {} ) score: {}".format(player1, player_score1))
    print(" Player 2 ( {} ) score: {} \n".format(player2, player_score2))
    print(HL)

#=# MAIN GAME BODY #=#

menu()                                                                          # The **only** function that is needed to be called

time.sleep(360)                                                                  # Wait for a minute, so they can look at their score, and how the round(s) was played
