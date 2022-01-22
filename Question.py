import random


class Question:
    answer_one = "a"
    answer_two = "b"
    answer_three = "c"
    answer_four = "d"

    def __init__(self, content):
        """
        This class is responsible for the management of the questions.
        :param content: The content of the question
        """
        self.content = content
        self.answers = []
        self.is_shuffled = False

    def __str__(self):
        """
        Sets the text of an answer.
        if self.answers are not shuffled yet, shuffle_answers() is called.
        :return: The question with a new line at the end and the four the answers
        """
        answertext = ""
        if not self.is_shuffled:
            self.shuffle_answers()
        for answer in self.answers:
            answertext += str(answer)
        return self.content + "\n" + answertext

    def add_answers(self, answers):
        """
        Extends the answer list with answers.
        :param answers: The list of answers which gets extended with the answers
        :return: None
        """
        self.answers.extend(answers)

    def add_answer(self, answer):
        """
        Appends one answer to a question
        :param answer: The list of answers where one answer is appended to
        :return: None
        """
        self.answers.append(answer)

    def set_content(self, content):
        """
        Sets the text of a question.
        :param content: The text of a question
        :return: None
        """
        self.content = content

    def shuffle_answers(self):
        """
        Shuffles the answers to a question.
        :return: None
        """
        random.shuffle(self.answers)
        self.is_shuffled = True

    def get_shuffled_answers(self):
        """
        Gets the shuffled answers to a question and
        if self.answers are not shuffled yet, shuffle_answers() is called.
        :return: The question text with all the answer texts
        """
        if not self.is_shuffled:
            self.shuffle_answers()
        return self.answers

    def get_answer_by_letter(self, letter_input):
        """
        Gets the answer to the letter entered.
        :param letter_input: The letter entered in the input field
        :return: The answer associated to the letter or None if something else than a, b, c or d was entered
        """
        if letter_input.lower() == self.answer_one.lower():
            return self.answers[0]
        elif letter_input.lower() == self.answer_two.lower():
            return self.answers[1]
        elif letter_input.lower() == self.answer_three.lower():
            return self.answers[2]
        elif letter_input.lower() == self.answer_four.lower():
            return self.answers[3]
        else:
            return None

    def get_correct_answer(self):
        """
        Gets the correct answer of a question.
        :return: The correct answer
        """
        for answer in self.answers:
            if answer.is_correct:
                return answer
