from Quizgenerator import *

quiz = Quizgenerator()
while not quiz.play_again_input == "exit":
    quiz.print_start_and_explanation()
    quiz.ask_for_other_question_file()
    quiz.start_game()
    quiz.question_generator.open_and_read_file()
    quiz.get_number_of_questions()
    quiz.print_question_and_receive_answer()
    quiz.get_and_print_score()
    quiz.play_again_or_exit()
    quiz.start_input = ""
    quiz.play_again_input = ""
    quiz.score = 0
    quiz.actual_question = 0
