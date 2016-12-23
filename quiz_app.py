intro_and_difficulty_prompt = """\nHello! This is a fill-in-the-blanks style American history trivia game.\n
Please select a difficulty by typing in easy, medium, or hard. \n\n"""

easy_test = """Originally, America had __1__ colonies. The 16th president
of United States was __2__. As of 2016, the United States consists
of __3__ states. America was founded in the year __4__."""

medium_test = """O say can you see, by the dawn's early light,
What so proudly we hail'd at the twilight's last __1__,
Whose broad stripes and bright stars through the perilous fight
O'er the __2__ we watch'd were so gallantly __3__?
And the rocket's red glare, the bombs bursting in air,
Gave proof through the night that our flag was still there,
O say does that star-spangled banner yet wave
O'er the land of the free and the home of the __4__?"""

hard_test = """The first president of the United States was __1__,
his vice president was __2__, he dropped out of school at the age of __3__,
and he was the only president to go into __4__ as president."""

easy_answers = ['13', 'Abraham Lincoln', '50', '1776']

medium_answers = ['gleaming', 'ramparts', 'streaming', 'brave']

hard_answers = ['George Washington', 'John Adams', '15', 'battle']

answer_lists = [easy_answers, medium_answers, hard_answers]

list_of_tests = [easy_test, medium_test, hard_test]

user_input_start_test = raw_input(intro_and_difficulty_prompt)

list_of_blanks = ['__1__', '__2__', '__3__', '__4__']

def select_difficulty(user_input):
    #This function takes the user_input from play_game and outputs the corresponding test's string and answer list. 
    if user_input == 'easy':
        print "\nYou selected easy difficutly!"
        return list_of_tests[0], answer_lists[0]
    if user_input == 'medium':
        print "\nYou selected medium difficutly!"
        return list_of_tests[1], answer_lists[1]
    if user_input == 'hard':
        print "\nYou selected hard difficutly!"
        return list_of_tests[2], answer_lists[2]

test, answers = select_difficulty(user_input_start_test) 

def get_answer(blank, answers):
    #This function takes the string that represents the blank space
    #that the user is prompted to fill in and outputs the correct answer for that blank. 
    if '1' in blank:
        return answers[0]
    if '2' in blank:
        return answers[1]
    if '3' in blank:
        return answers[2]
    if '4' in blank:
        return answers[3]


def check_if_blank(element_in_test, list_of_blanks):
    #This function takes an element of a test string and the list containing the strings of the blank spaces
    #and then outputs True or False for whether the element is a blank space.
    for blank in list_of_blanks:
        if blank in element_in_test:
            return True
        else:
            return False

def play_game(test, answers):
    #This function takes the test string and list of answers as inputs and then outputs various prompts to the user, asks them to fill in blanks,
    #tells them if there answer is correct or incorrect, and tells them if they have completed the test.
    filled_blank_index = 0
    progress_of_user = test
    #This while loop stops if the number of blanks that are filled in by the user matches the total number of blanks in the test.
    while filled_blank_index < len(list_of_blanks):
        split_test = test.split()
        answered = False
        for element_in_test in split_test:
            """first we need to check if there is a blank in element_in_test"""
            blank = check_if_blank(element_in_test, list_of_blanks)
            if blank == True:
                """then we need to retrieve the blank that is in element_in_test"""
                blank = list_of_blanks[filled_blank_index]
                """then we get the correct answer for the current blank"""
                correct_answer = get_answer(blank, answers)
                """then we attempt to get the answer from the user"""
                while answered == False:
                    """here we tell the user what they have filled so far"""
                    """here we ask the user for what should be in the blank"""
                    user_input = raw_input("\n\nThis is what's filled in so far: \n\n" + progress_of_user + "\n\nWhat should replace " + blank + "?\n\n")
                    """here we see if they gave us the right answer"""
                    if user_input == correct_answer:
                        answer = user_input
                        print '\n' + answer + " is correct!\n"
                        answered = True
                    elif user_input != correct_answer:
                        print "\nYour answer was incorrect, please try again."
                progress_of_user = progress_of_user.replace(blank, answer)
                """replace the blank with the answer"""
                """here we count how many blanks the user has filled"""
                filled_blank_index += 1
    print "Congratulations, you have completely filled in all of the blanks!"

play_game(test, answers)
