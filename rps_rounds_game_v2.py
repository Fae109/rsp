import random


#
def string_checker(question, valid_ans=("yes", "no")):
    error = f"pls enter a valid option from the following list: {valid_ans}"

    while True:

        #
        user_responce = input(question).lower()

        for item in valid_ans:
            # check if user responce is a word in list
            if item == user_responce:
                return item

            # check if the user responce is the same as
            # the first letter of an item in the list
            elif user_responce == item[0]:
                return item

        #
        print(error)
        print()


def instructions():
    """prints instructions"""

    print("""
*** Instructions ***


    """)


def int_check(question):
    """checks user enters an int more than or equal to 1"""

    while True:
        error = "pls enter an integer more then or equal to 1"

        to_check = input(question)

        #
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


def rps_compare(user, comp):
    if user == comp:
        round_result = "tie"

    # there are three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"

    # if it's not win/tie
    else:
        round_result = "lose"

    return round_result


# main

# initialise game
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print()
print("🪨📄✂️ Rock / Paper / Scissors ✂️📄🪨")
print()

# instructions

# ask viewer if they want (cheek they say yes / no)
want_instructions = string_checker("do you want to see the instructions?")

# display the instructions wants to see them...
if want_instructions == "yes":
    instructions()

# ask user for No. of round or infinite mode
num_rounds = int_check("how many rounds would you like? push <enter> of infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    # round heading
    if mode == "infinite":
        round_heading = f"\n♾️♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ️♾️♾️♾️♾️"
    else:
        round_heading = f"\n 💿💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿💿"

    print(round_heading)
    print()

    comp_choice = random.choice(rps_list[:-1])
    print("comp choice", comp_choice)

    user_choice = string_checker("choose: ", rps_list)
    print(f"you chose: {user_choice}")

    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    # adjust game lost / tied counters and add results to history
    if result == "tie":
        rounds_tied += 1
        feedback = "👔👔👔👔 It's a tie. 👔👔👔👔"
    elif result == "lose":
        rounds_lost += 1
        feedback = "👎👎👎👎 You Lose. 👎👎👎👎"
    else:
        feedback = "🎉👏🎉👏 You won. 👏🎉👏🎉"

    # set up round feedback
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)


    rounds_played += 1

    # if
    if mode == "infinite":
        num_rounds += 1

# game loop ends

# game history / stats area
if rounds_played > 0:
    # calculate stats
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # out put Stats
    print("📊📊📊📊 Game Stats 📊📊📊📊")
    print(f"🎉👏 Won: {percent_won:.2f}% \t "
          f"👎👎 Lost: {percent_lost:.2f}% \t "
          f"👔👔 Tied: {percent_tied:.2f}%")

    # ask if they want history
    see_history = string_checker("\nDo you want to see the game history?")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("thx for playing")

else:
    print("🐔🐔🐔🐔 Opps - You chickened out 🐔🐔🐔🐔")