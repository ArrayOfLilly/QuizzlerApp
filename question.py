import html

class Question:

    def __init__(self, question):
        self.question = html.unescape(question['question'])
        self.category = question['category']
        self.difficulty = question['difficulty']
        self.correct_answer = html.unescape(question['correct_answer'])
        self.incorrect_answers = question['incorrect_answers']
        self.question_type = question['type']
        self.escape_incorrect_answers()

    def escape_incorrect_answers(self):
        for answer in self.incorrect_answers:
            answer = html.escape(answer)