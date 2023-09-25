class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def get_current_question(self):
        current_question = self.question_list[self.question_number]
        return current_question

    def next_question(self):
        self.question_number += 1

    def get_current_question_number(self):
        return self.question_number

    def reset_quiz(self):
        self.question_number = 0
        self.score = 0
        self.question_list = []

    def get_total_question_number(self):
        return len(self.question_list)