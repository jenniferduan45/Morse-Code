import json
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import abort, redirect, url_for
from flask import Flask, url_for
from data import *
from utils import *
import re

import logging
app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html', answers_given=len(user['quiz_answers']))
#Morse Code Info
@app.route('/info')
def info_welcome():
    return render_template('info.html', answers_given=len(user['quiz_answers']))

#Flashcards
@app.route('/flashcards')
def flashcards():
    return render_template('flashcards.html', answers_given=len(user['quiz_answers']))

@app.route('/flash/<learn_id>')
def flash(learn_id=None):
    if learn_id in {"4", "5", "6", "10", "11", "12", "17", "18", "19", "20"}:
        return render_template('progress_check.html', progress_check=lessons[int(learn_id)],
                                                      letters2symbols=letters2symbols,
                                                      answers_given=len(user['quiz_answers']))
    else:
        return render_template('flashexten.html', lessons=lessons[int(learn_id)],
                                             letters2symbols=letters2symbols,
                                            answers_given=len(user['quiz_answers']))
# Learn section
@app.route('/learn')
def learn_welcome():
    return render_template('learn_welcome.html', answers_given=len(user['quiz_answers']))

@app.route('/learn/<learn_id>')
def learn(learn_id=None):
    if learn_id in {"4", "5", "6", "10", "11", "12", "17", "18", "19", "20"}:
        return render_template('progress_check.html', progress_check=lessons[int(learn_id)],
                                                      letters2symbols=letters2symbols,
                                                      answers_given=len(user['quiz_answers']))
    else:
        return render_template('learn.html', lessons=lessons[int(learn_id)],
                                             letters2symbols=letters2symbols,
                                           answers_given=len(user['quiz_answers']))

@app.route('/learnaction', methods=['GET', 'POST'])
def record_user_learnaction():
    json_data = request.get_json()

    lesson_id = json_data["lesson_id"]
    if lesson_id not in user_learn_action:
        user_learn_action[lesson_id] = [json_data]
    else:
        user_learn_action[lesson_id].append(json_data)

    print("Record user learning action in lesson ", lesson_id)

    return jsonify("")

# Test section
@app.route("/quiz")
def quiz_default():
    return render_template("quiz_welcome.html",
                           answers_given=len(user['quiz_answers']))

@app.route('/quiz/<quiz_id>')
def quiz(quiz_id=0):
    # if it's a new beginning, regenerate the questions
    if request.args.get("restart", None):
        generate_quiz()

    id = int(quiz_id)
    if id not in quizzes:
        id = 0
    return render_template('quiz.html', quiz=quizzes[id], quizzes=quizzes,
                           letters2symbols=letters2symbols)


@app.route('/submit',  methods=['GET', 'POST'])
def submit():
    json_data = request.get_json()

    # extract the user's answer from the json request
    quiz_id = json_data["quiz_id"]
    cur_answer = {}
    if "text_answer" in json_data:
        cur_answer["text_answer"] = json_data["text_answer"]
    if "symbol_answer" in json_data:
        cur_answer["symbol_answer"] = json_data["symbol_answer"]

    # check if the answer is correct
    quiz = quizzes[quiz_id]
    if quiz["to"] == "text":
        if cur_answer["text_answer"].lower() == quiz["word"]:
            cur_answer["is_correct"] = 1
        else:
            cur_answer["is_correct"] = 0
    else:
        if letters2symbols(quiz["word"]) == cur_answer["symbol_answer"]:
            cur_answer["is_correct"] = 1
        else:
            cur_answer["is_correct"] = 0


    user["quiz_answers"][quiz_id] = cur_answer

    print("current answer: ", cur_answer)

    return jsonify("")

@app.route("/result")
def result_default():
    return redirect("/result/0")

@app.route("/result/<quiz_id>")
def result(quiz_id=0):
    quiz_id = int(quiz_id)
    if quiz_id not in quizzes:
        quiz_id = 0
    return render_template("result.html", quiz_answers=user["quiz_answers"],
                           quizzes=quizzes, quiz_id=quiz_id,
                           answers_given=len(user['quiz_answers']))

@app.route("/answer/<quiz_id>")
def answer(quiz_id=0):
    quiz_id = int(quiz_id)
    if quiz_id not in quizzes:
        quiz_id = 0
    if quiz_id in user["quiz_answers"]:
        answer = user["quiz_answers"][quiz_id]
    else:
        answer = {"text_answer" : "", "symbol_answer" : [], "is_correct" : 0}
    return render_template("answer.html", quizzes=quizzes, quiz=quizzes[quiz_id], answer=answer,
                           letters2symbols=letters2symbols,
                           answers_given=len(user['quiz_answers']))


# AJAX FUNCTIONS
if __name__ == '__main__':
    app.run(debug=True)
