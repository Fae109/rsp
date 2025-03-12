#
#
def string_checker(question, valid_ans=["yes", "no"]):

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


 # main routine

rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("do you want to see the instructions")

print("you chose:", want_instructions)
print(f"you chose: {want_instructions}")

user_choice = string_checker("choose:", rps_list)
print(f"you chose: {user_choice}")
print("you chose:", user_choice)