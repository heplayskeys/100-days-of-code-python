from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(data["text"], data["answer"]) for data in question_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()

print("That's a wrap! Thanks for playing!")
print(f"Your final score is: {quiz.score} {"pt" if quiz.score == 1 else "pts"}")
print("Goodbye!")