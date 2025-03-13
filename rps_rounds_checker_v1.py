def int_check(to_check):
    """checks user enters an int more than or equal to 1"""

    while True:
        error = "pls enter an integer more then or equal to 1"

        #
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                # print(error)
                return "invalid"
            else:
                return response

        except ValueError:
            # print(error)
            return "invalid"


#
to_test = [
    ('xlil', 'invalid'),
    ('0.5', 'invalid'),
    ('0', 'invalid'),
    (1, 1),
    (2, 2),
    ('', 'infinite'),
]

#
for item in to_test:
    #
    case = item[0]
    expected = item[1]

    #
    actual = int_check(case)

    #
    if actual == expected:
        print(f"✅✅✅✅passed! case: {case}, expected:{expected} received: {actual}✅✅✅✅")
    else:
        print(f"❌❌❌❌FAILED! case: {case}, expected:{expected} received: {actual}❌❌❌❌")
