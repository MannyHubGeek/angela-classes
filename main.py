from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for q in question_data:
    question_text = q["text"]
    #print(question_text)
    question_answer = q["answer"]
    #print(question_answer)
    new_question = Question(que=question_text, ans=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
