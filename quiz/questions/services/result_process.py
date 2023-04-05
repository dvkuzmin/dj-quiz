from questions import models


def process_answers(answers: dict):
    correct_user_answers = len(answers)
    for question_id, user_answers in answers.items():
        user_answers = {k: v for k, v in user_answers.items() if v}
        question = models.Question.objects.get(pk=question_id)
        correct_answers = models.Answer.objects.filter(question=question, correct_answer=True).select_related('question')
        if len(correct_answers) == len(user_answers):
            for correct_answer in correct_answers:
                if str(correct_answer.id) in user_answers and user_answers[str(correct_answer.id)] is True:
                    continue
                else:
                    correct_user_answers -= 1
                    break
        else:
            correct_user_answers -= 1
    return correct_user_answers
