# rock paper scissors
def yes_no(question):
    """checks user response a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # make sure user says yes or no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(" pls enter yes or no")

def instructions():
    """prints instructions"""

    print("""
*** Instructions ***


    """)


# main routine

# ask viewer if they want (cheek they say yes / no)
want_instructions = yes_no("do you want to see the instructions?")

# display the instructions wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("program continues")