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


# main

# initialise game
mode = "regular"
rounds_played = 0

print()
print("🪨📄✂️ Rock / Paper / Scissors ✂️📄🪨")
print()

# instructions

# ask user for No. of round or infinite mode
num_rounds = int_check("how many rounds would you like? push <enter> of infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    print("you chose infinite")
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:
    user_choice = input("choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("rounds played:", rounds_played)

    # if
    if mode == "infinite":
        num_rounds += 1

    print("num rounds: ", num_rounds)

# game loop ends

# game history / stats area