class QuizBrain:

    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def has_questions(self):
        size = len(self.question_list)
        return self.question_num < size

    def next_question(self):
        current_q = self.question_list[self.question_num].text

        user_answer = input(
            f"Q.{self.question_num+1}: {current_q}. (True/False): ").lower()
        self.check_answer(user_answer)
        self.question_num += 1

    def check_answer(self, user):

        current_ans = self.question_list[self.question_num].ans.lower()
        if user == current_ans:
            self.score += 1
            print('You got it right!')
            print(
                f'Your current score is: {self.score}/{self.question_num+1}\n')
        else:
            print("That\'s wrong.")
            print(
                f'Your current score is: {self.score}/{self.question_num+1}\n')
