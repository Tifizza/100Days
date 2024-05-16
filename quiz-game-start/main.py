from question_model import Question
from quiz_brain import QuizBrain
import data
import requests
import html

data.show_categories()
category = int(input("Please choose which category (type the number) : "))
difficulty = input("Please choose difficulty (any/easy/medium/hard) : ")

question_bank = []
URL = f"https://opentdb.com/api.php?amount=10&category={category}&difficulty={difficulty}&type=boolean"
print(URL)
r = requests.get(URL).json()

if r["response_code"] != 0:
    print("No questions found, please choose another category !")
    exit(1)

for question in r["results"]:
    question_bank.append(Question(html.unescape(question["question"]), question["correct_answer"]))

brain = QuizBrain(question_bank)
while brain.next_question():
    pass
