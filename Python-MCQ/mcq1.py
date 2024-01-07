from question import Question

question_prompt = [
     "Colour of Apples?\na)Red/Green \nb)Purple \nc)Yellow\n\n"
     "Colour of Bananas?\na)Red \nb)Green/Yellow \nc)None\n\n"
     "Colour of Strawberries?\na)Green \nb)Orange \nc)Red\n\n"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " right.")

run_test(questions)

