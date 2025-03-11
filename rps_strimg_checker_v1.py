#
#
def string_checker(user_responce, valid_ans):
    while True:

        #
        user_responce = user_responce.lower()

        for item in valid_ans:
            # check if user responce is a word in list
            if item == user_responce:
                return item

            # check if the user responce is the same as
            # the first letter of an item in the list
            elif user_responce == item[0]:
                return item

        return "invalid"


#
to_test = [
    ("yes", "yes"),
    ("Y", "yes"),
    ("No", "no"),
    ("N", "no"),
    ("YeS", "yes"),
    ("Maybe", "invalid"),
]

#
for item in to_test:
    # fg
    case = item[0]
    expected = item[1]

    #
    actual = string_checker(case, ["yes", "no"])

    #
    if actual == expected:
        print(f"passed! case: {case}, expected:{expected} received: {actual}")
    else:
        print(f"FAILED! case: {case}, expected:{expected} received: {actual}")