#from main import Question


def create_list(question_one):
    question = question_one["q"]
    hard = question_one['d']
    correct_answer = question_one['a']
    return question, hard, correct_answer


#def statistic():
#
#    sum_correct_answer = len(Question.sum_correct_answer)
#    sum_balls = Question.sum_balls
#    sum_answer = len(Question.sum_user_answer)
#    return sum_correct_answer, sum_answer, sum_balls
