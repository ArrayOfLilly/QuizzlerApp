import random
import json
import requests
from question import Question

MAX_QUESTION_NUMBER = 12


class QuestionBank:

    def __init__(self, category='General Knowledge', difficulty='easy', number_of_questions=MAX_QUESTION_NUMBER):
        self.question_bank = []
        self.category = category
        self.difficulty = difficulty
        self.MAX_QUESTION_NUMBER = number_of_questions
        self.category_dict = {'General Knowledge': 9,
                              'Entertainment: Books': 10,
                              'Entertainment: Film': 11,
                              'Entertainment: Video Games': 15,
                              'Science & Nature': 17,
                              'Science: Computers': 18,
                              'Mythology': 20,
                              'Geography': 22,
                              'History': 23,
                              'Sports': 21,
                              'Animals': 27,
                              'Politics': 24,
                              'Entertainment: Japanese Anime & Manga': 31,
                              'Entertainment: Cartoon & Animation': 32
                              }

    def new_question_bank(self):
        self.question_bank = []

        for question in self.get_data():
            question = Question(question)
            self.question_bank.append(question)

        random.shuffle(self.question_bank)
        return self.question_bank

    def get_requested_data(self, requested_number_of_question, requested_category, requested_difficulty):
        parameters = {
            'amount': requested_number_of_question,
            'category': self.category_dict[requested_category],
            'difficulty': requested_difficulty,
        }

        response = requests.get('https://opentdb.com/api.php', params=parameters)
        response.raise_for_status()
        data = response.json()
        return data['results']

    def get_data_without_difficulty_constraint(self, requested_number_of_question, requested_category):
        parameters = {
            'amount': requested_number_of_question,
            'category': self.category_dict[requested_category],
        }

        response = requests.get('https://opentdb.com/api.php', params=parameters)
        response.raise_for_status()
        data = response.json()
        return data['results']

    def get_data(self):
        # print(f'We want data where category is: {self.category} and difficulty is {self.difficulty}')

        # Check category questions count by difficulty
        parameters = {
            'category': self.category_dict[self.category]
        }
        response = requests.get('https://opentdb.com/api_count.php', params=parameters)
        response.raise_for_status()
        data = response.json()
        # print(f'How many questions are in the category: {data}')

        if self.difficulty == 'easy':
            # print(f'We want the EASY questions from category: {self.category}, original request.')
            if data['category_question_count']['total_easy_question_count'] >= self.MAX_QUESTION_NUMBER:
                new_data = self.get_requested_data(self.MAX_QUESTION_NUMBER, self.category, self.difficulty)
                return new_data

        elif self.difficulty == 'medium':
            # print(f'We want the MEDIUM questions from category: {self.category}, original request.')
            if data['category_question_count']['total_medium_question_count'] >= self.MAX_QUESTION_NUMBER:
                new_data = self.get_requested_data(self.MAX_QUESTION_NUMBER, self.category, self.difficulty)
                return new_data

        elif self.difficulty == 'hard':
            # print(f'We want the HARD questions from category: {self.category}, original request.')
            if data['category_question_count']['total_hard_question_count'] >= self.MAX_QUESTION_NUMBER:
                new_data = self.get_requested_data(self.MAX_QUESTION_NUMBER, self.category, self.difficulty)
                return new_data

        if data['category_question_count']['total_question_count'] >= self.MAX_QUESTION_NUMBER:
            # print(
            #     f"Difficulty already doesn't matter, we want questions from category: {self.category}, extended "
            #     f"search for questions.")
            new_data = self.get_data_without_difficulty_constraint(self.MAX_QUESTION_NUMBER, self.category)
            return new_data

        else:
            # print(f"We haven't enough question in the {self.category} category, we extend quiz by general questions.")
            numbers_of_question_in_selected_category = MAX_QUESTION_NUMBER - data['category_question_count']
            remaining_questions_number = MAX_QUESTION_NUMBER - numbers_of_question_in_selected_category
            data_list = self.get_data_without_difficulty_constraint(numbers_of_question_in_selected_category,
                                                                    self.category)
            data_list_remaining = self.get_requested_data(remaining_questions_number, 'General Knowledge',
                                                          self.difficulty)
            extended_data = data_list.append(data_list_remaining)
            return extended_data
