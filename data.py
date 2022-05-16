import random

dot, dash = "DOT", "DASH"

pictures = {
    dot : "static/dot.jpg",
    dash : "static/dash.jpg"
}

letters_list = ["a", "e", "i", "o", "u", "r", "t", "n", "s", "l"]
letters = {
    "a" : [dot, dash],
    "e" : [dot],
    "i" : [dot, dot],
    "o" : [dash, dash, dash],
    "u" : [dot, dot, dash],
    "r" : [dot, dash, dot],
    "t" : [dash],
    "n" : [dash, dot],
    "s" : [dot, dot, dot],
    "l" : [dot, dash, dot, dot]
}

progress_checks = {
    3 : [
        {"letter" : "i", "is_audio" : True, "options": ["a", "e", "i"]},
        {"letter" : "a", "is_audio" : False, "options": ["a", "e", "i"]},
        {"letter" : "e", "is_audio" : False, "options": ["a", "e", "i"]},
    ],
    9 : [
        {"letter" : "u", "is_audio" : True,  "options" : ["u", "r", "o"]},
        {"letter" : "o", "is_audio" : False, "options" : ["u", "r", "o"]},
        {"letter" : "r", "is_audio" : True, "options" : ["u", "r", "o"]}
    ],
    16 : [
        {"letter" : "t", "is_audio" : True, "options" : ["l", "s", "t"]},
        {"letter" : "s", "is_audio" : False, "options" : ["t", "l", "s"]},
        {"letter" : "l", "is_audio": True, "options" : ["t", "l", "u"]},
        {"letter" : "n", "is_audio": False, "options" : ["t", "r", "n"]}
    ]
}

lessons = {}
cur_id = 1
for i in range(len(letters_list)):
    letter = letters_list[i]

    # add the lesson
    cur_lesson = {
        "lesson_id"     : cur_id,
        "type"          : "lesson",
        "title"         : "xxxx",
        "letter"        : letter,
        "next_lesson"   : cur_id + 1,
    }
    lessons[cur_id] = cur_lesson

    # add the progress checks
    if cur_id in progress_checks :
        # there are progress checks to be added after this lesson
        prog_checks = progress_checks[cur_id]
        cur_id += 1
        for prog_check in prog_checks:
            cur_lesson = {
                "lesson_id"     : cur_id,
                "type"          : "progress_check",
                "title"         : "xxxx",
                "letter"        : prog_check["letter"],
                "is_audio"      : prog_check["is_audio"],
                "options"       : prog_check["options"],
                "next_lesson"   : cur_id + 1,
            }
            lessons[cur_id] = cur_lesson
            cur_id += 1
    else:
        cur_id += 1

# set the next lesson of the last lesson to -1 to indicate that there
# are no more
lessons[cur_id - 1]["next_lesson"] = -1



quiz_candidates = [
    [
        {"word" : "r", "from" : "symbol", "to" : "text"},
        {"word" : "e", "from" : "symbol", "to" : "text"},
        {"word" : "i", "from" : "symbol", "to" : "text"},
    ],
    [
        {"word" : "l", "from" : "audio", "to" : "symbol"},
        {"word" : "a", "from" : "audio", "to" : "symbol"},
        {"word" : "s", "from" : "audio", "to" : "symbol"},
    ],
    [
        {"word" : "ur", "from" : "text", "to" : "symbol"},
        {"word" : "st", "from" : "text", "to" : "symbol"},
        {"word" : "no", "from" : "text", "to" : "symbol"},
    ],
    [
        {"word" : "ui", "from" : "audio", "to" : "text"},
        {"word" : "er", "from" : "audio", "to" : "text"},
        {"word" : "as", "from" : "audio", "to" : "text"},
    ],
    [
        {"word" : "utte", "from" : "audio", "to" : "symbol"},
        {"word" : "ious", "from" : "audio", "to" : "symbol"},
        {"word" : "true", "from" : "audio", "to" : "symbol"},
    ],
    [
        {"word" : "rate", "from" : "symbol", "to" : "text"},
        {"word" : "sore", "from" : "symbol", "to" : "text"},
        {"word" : "sour", "from" : "symbol", "to" : "text"},
    ],
    [
        {"word" : "rain", "from" : "text", "to" : "symbol"},
        {"word" : "lair", "from" : "text", "to" : "symbol"},
        {"word" : "rule", "from" : "text", "to" : "symbol"},
    ],
    [
        {"word" : "ion", "from" : "audio", "to" : "text"},
        {"word" : "neo", "from" : "audio", "to" : "text"},
        {"word" : "let", "from" : "audio", "to" : "text"},
    ]
]

def new_quiz_questions():
    quiz_questions = []
    for candidates in quiz_candidates:
        cur_question = candidates[random.randint(0, len(candidates) - 1)]
        quiz_questions.append(cur_question)

    return quiz_questions

quizzes = {}
def generate_quiz():
    global quizzes

    quiz_questions = new_quiz_questions()
    quizzes.clear()
    cur_id = 0
    for i in range(len(quiz_questions)):
        quiz_question = quiz_questions[i]
        cur_quiz = {
            "quiz_id"       : cur_id,
            "word"          : quiz_question["word"],
            "from"          : quiz_question["from"],
            "to"            : quiz_question["to"],
            "next_question" : cur_id + 1
        }
        quizzes[cur_id] = cur_quiz
        cur_id += 1

    quizzes[cur_id - 1]["next_question"] = -1

# generate first version
generate_quiz()

user = {
    "quiz_answers" : {}
}

user_learn_action = {}
