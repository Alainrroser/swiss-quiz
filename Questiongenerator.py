from Question import *
from Answer import *
import random


class Questiongenerator:

    def __init__(self, filename, encoding="utf8"):
        """
        This class reads the question file and generates the questions for the quiz.
        :param filename: The name of the question file.
        :param encoding: The name of the encoding of the question file
        """
        self.question_list = []
        self.number_of_answers = 4
        self.filename = filename
        self.encoding = encoding
        self.number_of_questions = 0
        self.lines = []

    def generate_all_questions(self):
        """
        Generates all questions with the answers to it in the file.
        :return: None
        """
        current_question = 0
        for i in range(self.number_of_questions):
            question = Question(self.lines[current_question])
            for answer_index in range(1, self.number_of_answers + 1):
                if answer_index == 1:
                    true_answer = Answer(self.lines[current_question + 1], True)
                    question.add_answer(true_answer)
                else:
                    question.add_answer(Answer(self.lines[current_question + answer_index]))
            self.question_list.append(question)
            current_question += self.number_of_answers + 1

    def get_random_questions(self, number_of_questions):
        """
        Generates a list of random questions with the answers, selected from a list of all questions and
        calls generate_all_questions() if self.question_list is empty.
        :param number_of_questions: The amount of questions to pick out of self.question_list
        :return: A new list of random questions
        """
        if len(self.question_list) == 0:
            self.generate_all_questions()
        random_questions = []
        while len(random_questions) < number_of_questions:
            random_question = random.choice(self.question_list)
            if random_question not in random_questions:
                random_questions.append(random_question)
        return random_questions

    def get_random_question(self):
        """
        Selects a random question with the answers from the question_list and
        calls generate_all_questions() if self.question_list is empty.
        :return: A new random question
        """
        if len(self.question_list) == 0:
            self.generate_all_questions()
        random_question = random.choice(self.question_list)
        return random_question

    def open_and_read_file(self):
        """
        Opens, reads and splits up the question file you entered.
        :return: None
        """
        question_file = open(self.filename, encoding=self.encoding)
        file_content = question_file.read()
        self.lines = file_content.split("\n")
        self.number_of_questions = int(len(self.lines) / (self.number_of_answers + 1))
        question_file.close()
