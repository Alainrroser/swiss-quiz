from Questiongenerator import *


class Quizgenerator:

    def __init__(self):
        """
        This class generates the whole quiz, the questions with the answers, the score, ...
        and also receives all the inputs.
        """
        self.start = "Hello to the Swiss-Quiz!"
        self.explanation = """A short explanation how the game works: 
There is a question and then there are four answers. 
The first answer is answer a, the second is answer b, the third is answer c and the fourth is answer d. 
You only have to enter a, b, c or d (That depends on which one is the right answer). Good Luck!
"""
        self.file_format = """The file must be formatted as following:
The first line has to be the question and the next four lines must be the answers.
For example:
Question 1
Answer 1.1
Answer 1.2
Answer 1.3
Answer 1.4
Question 2
Answer 2.1...
And the file must be in the same directory as the game is. 
"""
        self.number_of_questions_input = 0
        self.actual_question = 0
        self.score = 0
        self.play_again_input = ""
        self.question_generator: Questiongenerator = None
        self.start_input = ""
        self.count_of_times_played = 1

    def print_start_and_explanation(self):
        """
        Counts the times played in a row and prints the start and the explanation the first time.
        :return: None
        """
        if self.count_of_times_played == 1:
            print(self.start)
            print(self.explanation)
        self.count_of_times_played += 1

    def ask_for_other_question_file(self):
        """
        Asks if you want to use another question file and checks if it exists in this folder.
        :return: None
        """
        another_file_input = ""
        while not another_file_input.lower() == "y" or "n":
            another_file_input = input("If you want to use your own question file, type in \"y\". Else enter \"n\": ")
            if another_file_input.lower() == "y":
                print(self.file_format)
                correct_file_name = False
                self.enter_other_file_name(correct_file_name)
                break
            elif another_file_input.lower() == "n":
                self.question_generator = Questiongenerator("Questions.txt")
                break
            else:
                print("That is a wrong input. You have to type in \"n\" or \"y\".")

    def enter_other_file_name(self, correct_file_name):
        while not correct_file_name:
            try:
                question_file_name_input = input("Enter the name of the .txt-file, for example "
                                                 "\"Questions.txt\": ")
                file = open(question_file_name_input)
                file.close()
                self.question_generator = Questiongenerator(question_file_name_input)
                correct_file_name = True
            except IOError:
                print("This file doesn't exist in this directory. Move your file to the right path or enter "
                      "the correct path and file name.")

    def start_game(self):
        """
        Receives the input to start the game when you are ready for it.
        :return: None
        """
        while not self.start_input.lower() == "s":
            self.start_input = input("Enter \"s\" if you're ready for the game: ")
            if not self.start_input.lower() == "s":
                print("This was not a valid input. Enter \"s\"to start when you're ready.")

    def get_number_of_questions(self):
        """
        Prints out the minimum and the maximum of questions you can play with.
        :return: None
        """
        correct_input = False
        while not correct_input:
            try:
                self.number_of_questions_input = int(
                    input("Type in with how many questions you want to play (The maximum is " +
                          str(self.question_generator.number_of_questions) + " and the minimum is 3): "))
                if self.number_of_questions_input > 40 or self.number_of_questions_input < 3:
                    raise ValueError
                correct_input = True
            except ValueError:
                print("This was not a valid input. Enter a number smaller than " +
                      str(self.question_generator.number_of_questions) + " and bigger than 2.")

    def print_question_and_receive_answer(self):
        """
        Prints the question, receives your answer and
        calls check_answers to check if the answer is correct or not and to adjust the score.
        :return: None
        """
        question_list = self.question_generator.get_random_questions(self.number_of_questions_input)
        for question in question_list:
            self.actual_question += 1
            answer = None
            times_asked = 0
            while answer is None:
                print(str(self.actual_question) + ". Question: " + str(question))
                letter_input = input("Enter an answer (a, b, c or d): ")
                answer = question.get_answer_by_letter(letter_input)
                if times_asked == 0 and answer is None:
                    print("This was a wrong input. Enter a, b, c or d.")
            self.check_answers(answer, question)

    def check_answers(self, answer, question):
        """
        Checks if the given answer is correct or not and accordingly adjusts the score.
        :param answer: The answer to the question dependent on the letter
        :param question: The question the answer belongs to
        :return: None
        """
        if answer.is_correct:
            print("Your answer was correct, congratulations!")
            self.score += 1
            print("Your score is: " + str(self.score))
        elif not answer.is_correct:
            print("Your answer was sadly not the correct one. You will have more luck with the next question.")
            question.get_correct_answer()
            print("The correct answer would be: " + str(answer), end="")
            self.adjust_score_when_wrong()
        self.get_next_question()

    def adjust_score_when_wrong(self):
        if self.score >= 2:
            self.score -= 1
            print("Your score is " + str(self.score))
        else:
            self.score = 0
            print("Your score is " + str(self.score))

    def get_next_question(self):
        """
        Goes to the next question when you are ready.
        :return: None
        """
        next_question_input = ""
        while not next_question_input.lower() == "c" or next_question_input.lower() == "e":
            next_question_input = input("If you're ready, enter \"c\" or \"e\" to show the "
                                        "explanation again: ")
            if next_question_input.lower() == "e":
                print(self.explanation)
            elif not next_question_input.lower() == "c":
                print("That was not a valid input. Enter \"c\" to continue when you're ready or \"e\" to show the "
                      "explanation again.")

    def get_and_print_score(self):
        """
        Calculates if you were good in the quiz or not and prints the result.
        :return: None
        """
        if self.score == 0:
            print("You have got " + str(self.score) + " points. You should definitely go over your answers again.")
        elif self.number_of_questions_input >= (self.score / 3) * 2:
            print("You have got " + str(self.score) + " points. That is very good, congratulations.")
        elif (self.score / 2) <= self.number_of_questions_input <= (self.score / 3) * 2:
            print(
                "You have got " + str(self.score) + "points. That is not bad. It could be better but this is a "
                                                    "beginning.")
        else:
            print(
                "You have got " + str(self.score) + "points. You have a few points but should go over your answers "
                                                    "again.")

    def play_again_or_exit(self):
        """
        Takes the input you enter at the end of the game and checks if you want to continue or exit the game.
        :return: None
        """
        while not self.play_again_input.lower() == "a" or self.play_again_input.lower() == "exit":
            self.play_again_input = input("If you want to play the game again, enter \"a\", if not, enter \"exit\" to "
                                          "stop playing: ")
            if self.play_again_input.lower() == "exit":
                exit(0)
            elif self.play_again_input.lower() == "a":
                break
            else:
                print("This was not a valid input. Enter \"a\" or \"exit\" to continue.")
