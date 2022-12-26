class QuizBrain:

    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list

    def next_question(self):
        current_q = self.question_list[self.question_num].text
        current_ans = self.question_list[self.question_num].ans
        input(f"Q.{self.question_num+1}: {current_q}. (True/False): ")
        self.question_num += 1
