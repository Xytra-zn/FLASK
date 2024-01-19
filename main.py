from flask import Flask
import database
from database import questions
import random
app= Flask(__name__)

@app.route("/")
def home():
    return "WELCOME to api by @coders_zone"


def get_random_question():
    return random.choice(questions)


@app.route("/quiz")
def quiz():
    question = get_random_question()
    question_text = question["question"]
    options = question["options"]
    correct_option_id = question["correct_option_id"]
    response = f"Question: **{question_text}**\n\n"
    for i, option in enumerate(options):
        response += f"{i+1}. {option}\n"
    response += f"\nCorrect option: **{correct_option_id+1}**"
    return response
