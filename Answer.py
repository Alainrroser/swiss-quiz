class Answer:

    def __init__(self, content, is_correct=False):
        """
        This class is responsible for the management of the answers.
        :param content: The content of the answer
        :param is_correct: If the answer is the correct one or not
        """
        self.content = content
        self.is_correct = is_correct

    def __str__(self):
        """
        Adds a new line at the end of the answer.
        :return: The answer with a new line at the end
        """
        return self.content + "\n"

    def set_content(self, content):
        """
        Sets the content of an answer.
        :param content: The text of an answer
        :return: None
        """
        self.content = content

    def is_correct(self, is_correct):
        """
        Sets the is_correct value of an answer.
        :param is_correct: If the answer is the correct one or not
        :return: None
        """
        self.is_correct = is_correct
