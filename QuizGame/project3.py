import random

# Quiz dictionary (question: [options, correct_answer])
quiz = {
    "What is the output of print(2 ** 3)?":
        (["1. 6", "2. 8", "3. 5"], "2"),

    "Which keyword is used to define a function in Python?":
        (["1. function", "2. fun", "3. def"], "3"),

    "What data type is the result of input()?":
        (["1. str", "2. int", "3. float"], "1"),

    "What does len() do in Python?":
        (["1. Returns length", "2. Adds numbers", "3. Defines string"], "1"),

    "Which of the following is a valid variable name?":
        (["1. 2value", "2. my-name", "3. _score"], "3")
}

# Convert to list and shuffle questions
questions = list(quiz.items())
random.shuffle(questions)

# Initialize score and wrong answers
score = 0
wrong_answers = []

# Quiz loop
for i, (question, (options, correct)) in enumerate(questions, 1):
    print(f"\nQ{i}: {question}")
    for option in options:
        print(option)
    
    answer = input("Enter your choice (1/2/3): ").strip()

    if answer == correct:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        wrong_answers.append((question, correct))

# Final results
print("\n Quiz Complete!")
print(f"Your score: {score} out of {len(quiz)}")

if wrong_answers:
    print("\nQuestions you got wrong:")
    for q, correct in wrong_answers:
        print(f"- {q} (Correct answer: Option {correct})")
else:
    print("You got all questions correct!")